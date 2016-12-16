from sqlalchemy import create_engine
from sqlalchemy import Column,Integer,VARCHAR,TEXT,FLOAT
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class timu(Base):
    __tablename__ = 'timu'
    id = Column(Integer(),primary_key=True)
    tigan = Column(TEXT())
    dana = Column(TEXT())
    danb =Column(TEXT())
    danc = Column(TEXT())
    dand = Column(TEXT())
    dane = Column(TEXT())
    txid = Column(Integer())
    txgsh = Column(Integer())
    ckdan = Column(TEXT())
    jieda = Column(TEXT())
    jiexi = Column(TEXT())
    xkid = Column(Integer())
    kulei = Column(Integer())
    ndxs = Column(FLOAT())
    zhkg = Column(Integer())
    fenzhi = Column(Integer())
    isyx = Column(VARCHAR())
    gxr = Column(VARCHAR())
    gxrq = Column(VARCHAR())
    shycsh = Column(Integer())
    cwcsh = Column(Integer())
    smcsh = Column(Integer())
    beizhu = Column(VARCHAR())
    zhang = Column(TEXT())
    jie = Column(TEXT())
    zhishidian = Column(TEXT())
    tixing = Column(VARCHAR())
    excelid = Column(VARCHAR())

engine = create_engine('mysql+pymysql://root:root@127.0.0.1:3306/shuati_kfk?charset=utf8', encoding='utf-8', echo=False)
DBsession = sessionmaker(bind=engine)
session = DBsession()
