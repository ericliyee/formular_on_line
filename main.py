from tornado import gen,web
from tornado import ioloop
import os
from __init__ import *

class MainHandler(web.RequestHandler):
    @gen.coroutine
    def get(self):
        timus = session.query(timu).all()
        self.render('main.html',timus=timus)

class tigan_Edit(web.RequestHandler):
    @gen.coroutine
    def post(self):
        new_tigan = self.get_argument('tigan_edit')
        tm_id = self.get_argument('timu_id')
        start = '<ul class=" list-paddingleft-2"><li><p>'
        end = '</p></li></ul>'
        print(tm_id)
        if start in new_tigan:
            new_tigan = new_tigan.replace(start,'').replace(end,'')
            print(new_tigan)
        for tm in session.query(timu).filter(timu.id==tm_id):
            tm.tigan = new_tigan
        session.commit()
        self.write('保存成功!')

class jieda_Edit(web.RequestHandler):
    @gen.coroutine
    def post(self):
        new_jieda = self.get_argument('jieda_edit')
        tm_id = self.get_argument('timu_id')
        start = '<ul class=" list-paddingleft-2"><li><p>'
        end = '</p></li></ul>'
        print(tm_id)
        if start in new_jieda:
            new_jieda = new_jieda.replace(start,'').replace(end,'')
            print(new_jieda)
        for tm in session.query(timu).filter(timu.id==tm_id):
            tm.jieda = new_jieda
        session.commit()
        self.write('保存成功!')

class jiexi_Edit(web.RequestHandler):
    @gen.coroutine
    def post(self):
        new_jiexi = self.get_argument('jiexi_edit')
        tm_id = self.get_argument('timu_id')
        start = '<ul class=" list-paddingleft-2"><li><p>'
        end = '</p></li></ul>'
        print(tm_id)
        if start in new_jiexi:
            new_jiexi = new_jiexi.replace(start,'').replace(end,'')
            print(new_jiexi)
        for tm in session.query(timu).filter(timu.id==tm_id):
            tm.jiexi = new_jiexi
        session.commit()
        self.write('保存成功!')

        
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
        [
        (r'/',MainHandler),
        (r'/timuedit/',EditTimu),
        (r'/tigan_edit',tigan_Edit),
        (r'/jieda_edit',jieda_Edit),
        (r'/jiexi_edit',jiexi_Edit)
        ],
        **settings)


if __name__=='__main__':
    app = make_app()
    app.listen('8000')
    ioloop.IOLoop.instance().start()
