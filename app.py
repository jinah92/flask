# 실행 시 서버가 가동될 파이썬 파일

from flask import Flask, render_template

# Flask 객체 인스턴스 생성
app = Flask(__name__)


@app.route('/')  # 접속하는 url
def index():
    return render_template('index.html', user="진아", data={'level': 60, 'point': 360, 'exp': 45000})


if __name__ == '__main__':
    app.run(debug=True)  # 서버 가동
    # host 지정
    # app.run(host="127.0.0.1", port="5000", debug=True)
