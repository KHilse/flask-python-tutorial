from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import random
client = MongoClient(‘localhost’, 27017)
db = client.python_tutorial


# Declare app variable
app = Flask(__name__)

# Declare routes
@app.route("/")
def home_route():
    return "Hello world"

@app.route('/loops')
def loops():
    return render_template('/loops.html')

@app.route('/operators', methods = ['GET', 'POST'])
def operators():
    if request.method == 'GET':
        db.operators.find()
        return render_template('/operators.html', operators=operators)
    elif request.method == 'POST':
        # TODO: Add form data to database
        pass

# Listener
if __name__ == "__main__":
    app.run()
