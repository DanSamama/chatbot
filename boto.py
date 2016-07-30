"""
This is the template server side for ChatBot
"""
from bottle import route, run, template, static_file, request
import datetime
import json

instructions = {
    "how are you?": {"animation": "dancing", "msg": "Hello gorgeous, how are you?"},
    "How old are you ?": {"animation": "dancing", "msg": "I am young and 27 years old"}
}

boto_words = {
    "hi": {"animation": "dancing", "msg": "Hello gorgeous, how are you?"},
    "dan": {"animation":"giggling","msg":"Wow, what a beautiful name!!!"},
    "shit": {"animation": "dancing", "msg": "Don't swear like that!!"},
    "family": {"animation": "dancing", "msg": "I have a family of 4 little robots"},
    "good": {"animation": "ok", "msg": "I am happy for you"}

}

@route('/', method='GET')
def index():
    return template("chatbot.html")

def handleCompleteSentences(user_message):
    if user_message in instructions:
        return instructions[user_message]
    return None


def handleAskingForTime(user_message):
    if "time" in user_message:
        return {"animation": "bored", "msg": str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))}
    else:
        return None


def handleCommands(user_message):
    if user_message.endswith("!"):
        return {"animation": "no", "msg": "I am not your slave!"}
    else:
        return None


def handleWords(user_message):
    for word in user_message.split(" "):
        if word in boto_words:
            return boto_words[word]
    return None


@route("/chat", method='POST')
def chat():
    user_message = request.POST.get('msg')
    result = handleCommands(user_message)
    if not result:
        result = handleAskingForTime(user_message)
    if not result:
        result = handleCompleteSentences(user_message)
    if not result:
        result = handleWords(user_message)
    if not result:
        result = {"msg": "I don't understand","animation": "no"}
    return json.dumps(result)


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
