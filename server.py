import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from api.FuckHandler import *

from tornado.options import define, options
define("port", default=8000)

class ApiApplication(tornado.web.Application):
    def __init__(self):
        handlers = [
		        (r"/", BaseHandler),
			(r"/you", YouHandler),
			(r"/off", OffHandler),
			(r"/everything", EverythingHandler),
			(r"/custom", GenericHandler)
		]
        
        tornado.web.Application.__init__(self, handlers, debug=True)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(ApiApplication())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
