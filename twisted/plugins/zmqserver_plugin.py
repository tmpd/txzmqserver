from zope.interface import implements

from twisted.python import usage
from twisted.plugin import IPlugin
from twisted.application.service import IServiceMaker, Service

from twisted.internet import reactor

import txzmq
from zmqserver.zmqserver import ZMQServer

class Options(usage.Options):
	optParameters = [['endpoint', 'e', 'tcp://127.0.0.1:5555', 'zeromq server endpoint']]

class ZMQServerService(Service):
	def __init__(self, endpoint):
		self.endpoint = endpoint

	def startService(self):
		zmq_factory = txzmq.ZmqFactory()
		zmq_endpoint = txzmq.ZmqEndpoint("bind", self.endpoint)
		self.zmqserver = ZMQServer(zmq_factory, zmq_endpoint)
		print "Start ZMQServer service"

	def stopService(self):
		print "Stop ZMQServer service"
		self.zmqserver.shutdown()

class ZMQServerServiceFactory(object):
	implements(IServiceMaker, IPlugin)
	tapname = "zmqserver"
	description = "txzmq as twistd example"
	options = Options

	def makeService(self, options):
		endpoint = options['endpoint']
		return ZMQServerService(endpoint)

## Now construct an object which *provides* the relevant interfaces
## The name of this variable is irrelevant, as long as there is *some*
## name bound to a provider of IPlugin and IServiceMaker.
serviceMaker = ZMQServerServiceFactory()
