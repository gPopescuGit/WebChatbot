from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


app = Flask(__name__)

chatbot = ChatBot('ChatBot')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.romana")

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/get")
def get_bot_response():
    usertext = request.args.get("msg")
    return str(chatbot.get_response(usertext))


if __name__ == "__main__":
    app.run()


