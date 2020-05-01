# -*- coding: utf-8 -*-
"""
Created on Fri May  1 13:23:09 2020

@author: Gebruiker
"""


from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from app import app
import os

port = int(os.getenv('PORT', 4200))
http_server = HTTPServer(WSGIContainer(app))
http_server.listen(port)
IOLoop.instance().start()