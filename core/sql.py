from twisted.enterprise import adbapi
from twisted.internet.defer import inlineCallbacks
import config
import __builtin__

__builtin__.PYOT_RUN_SQLOPERATIONS = True
# Our own methods.
def runOperationLastId(self, *args, **kw):
    if PYOT_RUN_SQLOPERATIONS:
        return self.runInteraction(self._runOperationLastId, *args, **kw)
    return random.randint(1, 1000)

def _runOperationLastId(self, trans, *args, **kw):
    trans.execute(*args, **kw)
    return trans.lastrowid

# Patch adbapi.ConnectionPool
adbapi.ConnectionPool._runOperationLastId = _runOperationLastId
adbapi.ConnectionPool.runOperationLastId = runOperationLastId

# Connection function.
def connect(module = config.sqlModule):
    if module == "MySQLdb":
        if config.sqlSocket:
            return adbapi.ConnectionPool(module, host=config.sqlHost, unix_socket=config.sqlSocket, db=config.sqlDatabase, user=config.sqlUsername, passwd=config.sqlPassword, cp_min=config.sqlMinConnections, cp_max=config.sqlMaxConnections, cp_reconnect=True, cp_noisy=config.sqlDebug)
        else:
            return adbapi.ConnectionPool(module, host=config.sqlHost, db=config.sqlDatabase, user=config.sqlUsername, passwd=config.sqlPassword, cp_min=config.sqlMinConnections, cp_max=config.sqlMaxConnections, cp_reconnect=True, cp_noisy=config.sqlDebug)
    elif module == "mysql-ctypes":
        return adbapi.ConnectionPool("MySQLdb", host=config.sqlHost, port=3306, db=config.sqlDatabase, user=config.sqlUsername, passwd=config.sqlPassword, cp_min=config.sqlMinConnections, cp_max=config.sqlMaxConnections, cp_reconnect=True, cp_noisy=config.sqlDebug)

    elif module == "oursql":
        try:
            import oursql
        except ImportError:
            print "Falling oursql back to MySQLdb"
            return connect("MySQLdb")

        if config.sqlSocket:
            return adbapi.ConnectionPool(module, host=config.sqlHost, unix_socket=config.sqlSocket, db=config.sqlDatabase, user=config.sqlUsername, passwd=config.sqlPassword, cp_min=config.sqlMinConnections, cp_max=config.sqlMaxConnections, cp_reconnect=True, cp_noisy=config.sqlDebug)
        else:
            return adbapi.ConnectionPool(module, host=config.sqlHost, db=config.sqlDatabase, user=config.sqlUsername, passwd=config.sqlPassword, cp_min=config.sqlMinConnections, cp_max=config.sqlMaxConnections, cp_reconnect=True, cp_noisy=config.sqlDebug)

    elif module == "pymysql": # This module is indentical, but uses a diffrent name
        try:
            import pymysql
        except ImportError:
            print "Falling pymysql back to MySQLdb"
            return connect("MySQLdb")          

        if config.sqlSocket:
            return adbapi.ConnectionPool(module, host=config.sqlHost, unix_socket=config.sqlSocket, db=config.sqlDatabase, user=config.sqlUsername, passwd=config.sqlPassword, cp_min=config.sqlMinConnections, cp_max=config.sqlMaxConnections, cp_reconnect=True, cp_noisy=config.sqlDebug)
        else:
            return adbapi.ConnectionPool(module, host=config.sqlHost, db=config.sqlDatabase, user=config.sqlUsername, passwd=config.sqlPassword, cp_min=config.sqlMinConnections, cp_max=config.sqlMaxConnections, cp_reconnect=True, cp_noisy=config.sqlDebug)
    elif module == "sqlite3":
        import sqlite3

        # Implode our little hack to allow both sqlite3 and mysql to work together!
        # This is a bit slower I guess, but it works :)
        def runQuery(self, *args, **kw):
            args = list(args)
            args[0] = args[0].replace('%s', '?').replace('%f', '?').replace('%d', '?') # String, float and digit support
            args = tuple(args)
            return self.runInteraction(self._runQuery, *args)
        adbapi.ConnectionPool.runQuery = runQuery

        return adbapi.ConnectionPool(module, config.sqlDatabase, isolation_level=None, check_same_thread=False)

    else:
        raise NameError("SQL module %s is invalid" % module)
    
# Setup the database pool when this module is imported for the first time
conn = connect()

def runOperation(*argc, **kwargs):
    return conn.runOperation(*argc, **kwargs)
    
def runQuery(*argc, **kwargs):
    return conn.runQuery(*argc, **kwargs)
    
# A custom call we got. Not in the twisted standard.
def runOperationLastId(*argc, **kwargs):
    return conn.runOperationLastId(*argc, **kwargs)
    