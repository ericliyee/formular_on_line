from tornado import gen,web
from tornado import ioloop
import os
from __init__ import *

class MainHandler(web.RequestHandler):
    @gen.coroutine
    def get(self):
        timus = session.query(timu).limit(10)
        self.render('main.html',timus=timus)

class EditTimu(web.RequestHandler):
    @gen.coroutine
    def get(self):
        timu_id = self.get_argument('timu_id')
        tm = session.query(timu).filter(timu.id==timu_id)
        self.render('timuEdit.html',timus=tm)
        
settings={
    'static_path' :os.path.join(os.path.dirname(__file__),'static'),
    'template_path' :os.path.join(os.path.dirname(__file__),'templates'),
    'debug':True,
    'autoescape':None
    }
        
def make_app():
    return web.Application(
        [(r'/',MainHandler),(r'/timuedit/',EditTimu)],
        **settings)


if __name__=='__main__':
    app = make_app()
    app.listen('8000')
    ioloop.IOLoop.instance().start()
