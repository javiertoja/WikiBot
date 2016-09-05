# WikiBot
Simple Python Bot to interact with Mattermos local server and generate wiki content.

This bot responds to a http request made from a mattermos slash command 
and send a http request to an incoming hook with a message.

### Installation
Before execute the program you should have install installed the required dependecies:

1. flask (pip install flask)([flask](https://github.com/pallets/flask/releases/tag/0.11.1))
2. flask-restful (pip install flask-restful)([flask-restfull](https://github.com/flask-restful/flask-restful/releases/tag/0.2.12))
3. requests (pip install requests) ([requests](https://github.com/kennethreitz/requests/releases/tag/v2.11.1))
 
After that download the py/pyc file.

### Usage
In order to execute the program you should provide the requires arguments

- -lp listening ip, 0.0.0.0 tells your operating system to listen on all public IPs.
- -p port, listening port.
- -hk hook, mattermos hook with the url http://<mattermost ui>/hooks/<mattermost hook id>
 
python Wikibot.py -lp 0.0.0.0 -p 9080 -hk http://mattermost.domain.org/hooks/a7d8a9sda79sda7fdasd8a9d7f

### How it works
In order to get the complete solutions working with mattermost you need to follow the next steps:

1. Create a incomming hook on mattermos pointing to a channel with name wiki, if no mane is provided the program will try to post the message in a channel with name "wiki"
2. Run the program like on the Usage section with the hook uri genereated on the first step.
3. create a slash command on mattermost which send a POST http requests, to the public ip of the server where the bot is running to the endpoint "/wikibot/"
4. Try it!, on your mattermost installation run /wiki whatever , don't forget the where on a delete from.
5. Enjoy.
