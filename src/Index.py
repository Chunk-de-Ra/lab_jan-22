import tornado.web

class Handler(tornado.web.RequestHandler):
    def get(self):
        self.write('<a href"/fancy">Get a quote</a')