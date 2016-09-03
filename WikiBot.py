'''
Created on 2 sept. 2016

@author: Javier Toja Alamancos
'''
from flask_restful import Resource, reqparse

class WikiBot(Resource):
    
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('text')

    def post(self):
        args = self.parser.parse_args()
        print("adiendo entrada a la wiki -- ["+args["text"]+"]")
        return  {"text":"Entrada realizada correctamente !"}