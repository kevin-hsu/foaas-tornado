import tornado.web
import json

"""
TO DO:
BaseHandler class
- standard get/put/post/delete methods
- debug info decorator

Models 
- define SQLAlchemy models for objects
- pass model to handler?
- how could we design that way?
"""


class TestHandler(tornado.web.RequestHandler):
    def get(self):
        qs_args = self.request.arguments
	if len(qs_args) == 0:
		self.write('empty query string')
	else:
		self.write(qs_args)


    def post(self):
        data = json.loads(self.request.body)
        
        for key, value in data.iteritems():
            self.write(key + " " + value + "\n")
        
