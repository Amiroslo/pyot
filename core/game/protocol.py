from twisted.python import log
import sys

protocolsAvailable = (860, 910)
protocolsUsed = {}

def getProtocol(version):
    try:
        return protocolsUsed[version]
    except:
        log.msg("Protocol %d unsupported" % version)
    return None

def loadProtocol(version):
    if not version in protocolsAvailable:
        log.msg("Protocol (Base) %d doesn't exist!" % version)
        return
        
    protocol = __import__('game.protocols.%d' % version, globals(), locals())
    protocol = sys.modules['game.protocols.%d' % version]
    for x in protocolsUsed:
        if not x in protocol.compatible_protocols:
            log.msg("Can't load protocol %d do to incompatibility")
            return
            
    protocol.vertify()
    protocolsUsed[version] = protocol.Protocol()
    for x in protocol.provide:
        protocolsUsed[x] = protocolsUsed[version]