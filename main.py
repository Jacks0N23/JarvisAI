import os
import json
import tensorflow as tf

# https://habr.com/ru/post/326380/ & https://habr.com/ru/post/249215/ &
# https://www.geeksforgeeks.org/python-word-embedding-using-word2vec/
import gensim
import pymorphy2
from flask import Flask, request


HOST = "0.0.0.0"
PORT = os.environ.get('PORT', 8443)

server = Flask(__name__)


def process_command(response):
    data = json.loads(response)
    print(data)
    #intent_name = data['result']['metadata']['intentName']


@server.route('/', methods=['POST'])
def post_message():
    req = request.stream.read().decode("utf-8")
    print(req)
    return '/bot', 200


@server.route('/', methods=['GET'])
def get_message():
    req = request.stream.read().decode("utf-8")
    print(req)
    process_command(req)
    return '/', 200
