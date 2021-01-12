from flask import Flask, g

# g : 글로벌 변수

app = Flask(__name__)


@app.before_request
def before_request():
    print("before request!")
    g.str = "한글"


@app.route("/gg")
def gg():
    return 'Hello world' + getattr(g, 'str', '111')


@app.route("/")
def helloWorld():
    return "Hello Flask World!"


if __name__ == '__main__':
    # host 지정
    app.run(host="127.0.0.1", port="5000", debug=True)
