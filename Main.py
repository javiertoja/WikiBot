'''
Created on 2 sept. 2016

@author: Javier Toja Alamancos
'''

from flask import Flask
from flask_restful import Api
from WikiBot import WikiBot

if __name__ == '__main__':

    app = Flask(__name__)
    api = Api(app)

    api.add_resource(WikiBot, '/wikibot/')
    
    app.run(None,9080,debug=True)