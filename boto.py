"""
This is the template server side for ChatBot
"""
from bottle import route, run, template, static_file, request
import json

instructions = {
    "hi": {"animation": "dancing", "msg": "Hello gorgeous, how are you?"},
    "How old are you ?": {"animation": "dancing", "msg": "I am young and 27 years old"}
}

@route('/', method='GET')
def index():
    return template("chatbot.html")

def handleCompleteSentences(user_message):
    if user_message in instructions:
        return json.dumps(instructions[user_message])
    return None

@route("/chat", method='POST')
def chat():
    user_message = request.POST.get('msg')
    #Changing the humor of the bot
    result = handleCompleteSentences(user_message)
    if not result:
        
        return json.dumps({"msg":"I don't understand","animatoin":"no"})


@route("/test", method='POST')
def chat():
    user_message = request.POST.get('msg')
    return json.dumps({"animation": "inlove", "msg": user_message})


@route('/js/<filename:re:.*\.js>', method='GET')
def javascripts(filename):
    return static_file(filename, root='js')


@route('/css/<filename:re:.*\.css>', method='GET')
def stylesheets(filename):
    return static_file(filename, root='css')


@route('/images/<filename:re:.*\.(jpg|png|gif|ico)>', method='GET')
def images(filename):
    return static_file(filename, root='images')


def main():
    run(host='localhost', port=7000)

if __name__ == '__main__':
    main()
