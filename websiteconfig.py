import os

_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False
tst_psw = "your password"
DATABASE_URI = "mysql+pymysql://root:" + tst_psw + "@localhost/gitar"
del os
