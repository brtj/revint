import os 

from flask import Flask, render_template, request, jsonify

from functions import birthday_msg

app = Flask(__name__)


@app.route("/")
def renderIndex():
    return render_template("index.html")

@app.route('/hello/<username>', methods = ["PUT", "GET"])
def username_dob(username):
    print(request)
    print(request.method)
    if request.method == "PUT":
        return f"{username} created"
    elif request.method == "GET":
        return birthday_msg(username, 'YYYY-MM-DD')
    else:
        return "Only GET/PUT allowed"

if __name__ == '__main__':
	app.run(host="0.0.0.0", port=8080, debug=True)