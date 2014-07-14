from txzmq import ZmqREPConnection, ZmqEndpoint, ZmqFactory

class ZMQServer(ZmqREPConnection):
	def __init__(self, zmqfactory, zmqendpoint):
		ZmqREPConnection.__init__(self, zmqfactory, zmqendpoint)

	def gotMessage(self, messageId, message):
		print "Receive request %s from %s" % (message, messageId)
		self.reply(messageId, "Echo %s" % message)
