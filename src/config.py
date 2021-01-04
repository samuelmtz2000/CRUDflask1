import os
import urllib

class Config(object):
	SECRET_KEY = 'Abril2000'

class Developementconfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'mysql://root:''@localhost/crudflask'
	SEQUELALCHEMY_TRACK_MODIFICATIONS = False
	CACHE_TYPE: 'simple'
	CAHCE_DEFAULT_TIMEOUT: 10


