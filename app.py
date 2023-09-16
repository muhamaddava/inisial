from flask import Flask, render_template, request, jsonify, redirect, url_for
import certifi
from pymongo import MongoClient

app = Flask(__name__)

cxn_str = 'mongodb+srv://muhamaddavaalrasid:d1a2v3a4@cluster0.7rxa4op.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(cxn_str)
db = client.dbsparta

@app.route('/')
def main():
    return render_template("index.html")



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)