import tornado.web
import json

class BaseHandler(tornado.web.RequestHandler):
	def get(self):
		self.write('<h2>Fuck.</h2>')

class YouHandler(tornado.web.RequestHandler):
    def get(self):
		qs_args = self.request.arguments
		keys = qs_args.keys()
		print 'to' in keys
		if ('to' in keys):
			self.write('<h2>Fuck you, %s.</h2>' % qs_args['to'][0])
			if ('from' in keys):
				self.write('<br> - From <i>%s</i>' % qs_args['from'][0])
			else:
				self.write('<br> - From <i>anonymous</i>')


class OffHandler(tornado.web.RequestHandler):
    def get(self):
		qs_args = self.request.arguments
		keys = qs_args.keys()
		print 'to' in keys
		if ('to' in keys):
			self.write('<h2>Fuck off, %s.</h2>' % qs_args['to'][0])
			if ('from' in keys):
				self.write('<br> - From <i>%s</i>' % qs_args['from'][0])
			else:
				self.write('<br> - From <i>anonymous</i>')

class EverythingHandler(tornado.web.RequestHandler):
	def get(self):
		self.write('<h2>Fuck everything.</h2>')

class GenericHandler(tornado.web.RequestHandler):
	def get(self):
		qs_args = self.request.arguments
		keys = qs_args.keys()
		if ('message' in keys):
			self.write("<h2>Fuck %s.</h2>" % qs_args['message'][0])
		else:
			self.write("<h2>Fuck, you didn't give me a message</h2>")
