#!/usr/bin/env python

import config
import sys

#### Setup Reactor ####
if config.reactorStyle is "poll":
    from twisted.internet import pollreactor
    pollreactor.install()

elif config.reactorStyle is "epoll":
    from twisted.internet import epollreactor
    epollreactor.install()

elif config.reactorStyle is "kqueue" and sys.platform is 'freebsd':
    from twisted.internet import kqreactor
    kqreactor.install()

elif config.reactorStyle is "iocp" and sys.platform is 'win32':
    from twisted.internet import iocpreactor
    iocpreactor.install()

else: # This is the default reactor, "select"
    from twisted.internet import selectreactor
    selectreactor.install()

from twisted.internet import reactor

#### Suggest reactor thread pool size ####
reactor.suggestThreadPoolSize(config.suggestedGameServerThreadPoolSize)

#### Initialize OTCrypto module ####
import core.otcrypto
core.otcrypto.setkeys(config.RSAKeys["n"], config.RSAKeys["e"], config.RSAKeys["d"], config.RSAKeys["p"], config.RSAKeys["q"])

#### Import the LoginServer ####
from twisted.application import internet, service
from core.service.gameserver import GameProtocol, GameFactory, GameService



topService = service.MultiService()

GameServiceInstance = GameService()
GameServiceInstance.setServiceParent(topService)

factory = GameFactory(GameServiceInstance)
tcpService = internet.TCPServer(config.gamePort, factory, interface=config.gameInterface)
tcpService.setServiceParent(topService)

application = service.Application("pyot-game-server")

topService.setServiceParent(application)
