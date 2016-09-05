'''
MIT License

Copyright (c) 2016 Javier Toja

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Created on 2 sept. 2016

@author: Javier Toja Alamancos
'''
from flask_restful import reqparse, Resource
import requests
import json
from flask import Flask
from flask_restful import Api
import argparse

class WikiBot(Resource):
    
    def __init__(self,**kwargs):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('text')
        self.channel = kwargs['channel']
        self.hook = kwargs['hook']
        self.message = kwargs['message']

    def post(self):
        args = self.parser.parse_args()
        payload = {"text": "[WIKI] "+args["text"], "channel": self.channel,"username": "wikiBot", "icon_url": "https://d13yacurqjgara.cloudfront.net/users/10958/screenshots/271458/librarian.jpg"}
        requests.post(self.hook, json.dumps(payload) , verify = False)        
        return  {"text": self.message, "response_type":"in_channel"}, 200

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='WikiBot 1.0')
    
    # Add arguments
    parser.add_argument(
        '-lp', '--listenIp', type=str, help='Ip linstening range', required=False, default='127.0.0.1')
    parser.add_argument(
        '-p', '--port', type=int, help='Port number', required=True)
    parser.add_argument(
        '-c', '--channel', type=str, help='Mattermos channel to respond', required=False, default='wiki')
    parser.add_argument(
        '-hk', '--hook', type=str, help='Mattermos hook url', required=True)
    parser.add_argument(
        '-m', '--message', type=str, help='Thanks message', required=False, default='Gracias por registrar su entrada')    
    
    args = parser.parse_args()

    app = Flask(__name__)
    api = Api(app)

    api.add_resource(WikiBot, '/wikibot/', resource_class_kwargs={'channel': args.channel,'hook':args.hook, 'message':args.message})
    app.run(args.listenIp,args.port)
