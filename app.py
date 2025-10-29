from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# Route 1: Greeting Page using Jinja2 Template
@app.route("/hello/<username>")
def hello(username):
    return render_template("hello.html", name=username)

# Route 2: Welcome Page
@app.route("/welcome")
def welcome():
    return "Welcome to the Flask App!" 

# Route 3: Square of a Number
@app.route("/square/<int:number>")
def square(number):
    result = number ** 2
    return f"The square of {number} is {result}."

# Route 4: Repeat Word
@app.route("/repeat/<string:word>/<int:times>")
def repeat(word, times):
    return (word + " ") * times

# Route 5: Current Date and Time
@app.route("/info")
def info():
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return f"Current Date and Time: {current_time}"

if __name__ == "__main__":
    app.run(debug=True)