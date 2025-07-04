from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to my website. I am Andrew Adel."

@app.route("/index")
def index():
    return "Welcome to index page."

if __name__ == "__main__":
    app.run(debug=True)
