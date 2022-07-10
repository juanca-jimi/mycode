from flask import jsonify, Flask, request, redirect, render_template, url_for
from django.shortcuts import render


GOATS = {
    "red hot chili peppers" : {
        "up_there" : False,
        "numberOnes" : 100
        },
    "the wiggles" : {
        "up_there" : True,
        "numberOnes" : 30
        },
    "metallica" : {
        "up_there" : True,
        "numberOnes" : 40
        } ,
    "the beatles" : {
        "up_there" : True,
        "numberOnes" : 50
        } 
    }

app = Flask(__name__)

@app.route("/")
def start():
    return render_template("index.html")

@app.route("/your-in/<name>", methods = ["GET"])
def your_in(name):
    return render_template("yourin.html", name = name)

@app.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "GET":
        if request.args.get("nm"):
            user = request.args.get("nm")
        else:
            user = "anonymous"
    elif request.method == "POST":
        if request.form.get("nm"):
            user = request.form.get("nm")
        else:
            user = "anonymous"
    return redirect(url_for("your_in", name = user))

@app.route("/your-in/the-truth")
def the_truth():
    return jsonify(GOATS)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3333)
