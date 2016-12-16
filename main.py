from tornado import gen,web
from tornado import ioloop
import os
from __init__ import *

class MainHandler(web.RequestHandler):
    @gen.coroutine
    def get(self):
        self.render('index.html')


settings={
    'static_path' :os.path.join(os.path.dirname(__file__),'static'),
    'template_path' :os.path.join(os.path.dirname(__file__),'templates'),
    'debug':True
    }
        
def make_app():
    return web.Application(
        [(r'/',MainHandler)],
        **settings)


if __name__=='__main__':
    app = make_app()
    app.listen('8888')
    ioloop.IOLoop.instance().start()
