from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "hello,world!"

@app.route("/<name>")
def hello(name):
    return f"hello,{name}!"

if __name__ == "__main__":
    app.run(debug=True)
