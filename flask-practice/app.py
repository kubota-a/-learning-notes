from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Home page"

@app.route("/about")
def about():
    return "About page"

@app.route("/hello")
def hello():
    return "Hello Flask"

if __name__ == "__main__":
    app.run(debug=True)
