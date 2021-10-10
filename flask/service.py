import os 

from flask import Flask, render_template, request

from functions import birthday_msg
from functions_db import post_usernamedob_db

app = Flask(__name__)

@app.route("/")
def renderIndex():
    return render_template("index.html")

@app.route('/hello/<username>', methods = ["PUT", "GET"])
def username_dob(username):

    if request.method == "PUT" and username.isalpha():
        post_usernamedob_db(username, request.json)
        return f"{username} created"
    elif request.method == "GET":
        return birthday_msg(username, 'YYYY-MM-DD')
    else:
        return "Only GET/PUT allowed. Username only letters"

if __name__ == '__main__':
	app.run(host="0.0.0.0", port=8080, debug=True)