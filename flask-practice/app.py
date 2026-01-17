from flask import Flask
from flask import render_template

app = Flask(__name__)

memo_list = [
    {'title': "test01", 'body': "チャッピーです。"},
    {'title': "test02", 'body': "GPTです。"}
]


@app.route("/")
def top():
    return render_template('index.html', memo_list=memo_list)

if __name__ == "__main__":
    app.run(debug=True)
