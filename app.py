from flask import Flask, render_template, request, send_file
from get_news import get_news

app = Flask(__name__)


@app.route("/home")
@app.route("/")
def index():
    return render_template('home.html')


@app.route('/getnews', methods=['POST'])
def analyse():
    try:
        key_word = request.form['keyword']
        return get_news(key_word)
    except:
        return "Can't find news"


@app.route('/news.js', methods=['GET'])
def getNews():
    return send_file('news.js')


if __name__ == "__main__":
    app.run(debug=True)
