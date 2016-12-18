from tornado import gen,web
from tornado import ioloop
import os
from __init__ import *

class MainHandler(web.RequestHandler):
    @gen.coroutine
    def get(self):
        timus = session.query(timu).all()
        self.render('main.html',timus=timus)

class EditTimu(web.RequestHandler):
    @gen.coroutine
    def get(self):
        timu_id = self.get_argument('timu_id')
        timu = session.query(timu).filter(timu.id==timu_id)
        self.render('timuEdit.html',timu=timu)
        
settings={
    'static_path' :os.path.join(os.path.dirname(__file__),'static'),
    'template_path' :os.path.join(os.path.dirname(__file__),'templates'),
    'debug':True,
    'autoescape':False
    }
        
def make_app():
    return web.Application(
        [(r'/',MainHandler)],
        **settings)


if __name__=='__main__':
    app = make_app()
    app.listen('8000')
    ioloop.IOLoop.instance().start()
