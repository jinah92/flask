from flask import Flask, g, request, make_response, Response, session, render_template
from flask import Markup
from datetime import date, datetime, timedelta

# g : 글로벌 변수

app = Flask(__name__)

app.config.update(
    SECRET_KEY='abcde',
    SESSION_COOKIE_NAME='pyweb_flask_session',
    PREMANENT_SESSION_LIFETIME=timedelta(minutes=30)  # 30분간 세션 유지
)


# request 처리 용 함수
def ymd(fmt):
    def trans(date_str):
        return datetime.strptime(date_str, fmt)

    return trans


@app.route('/t')
def t():
    tit = Markup('<strong>Title</strong>')
    mu = Markup('<h1>iii = <i>%s</i></h1>')
    h = mu % 'Italic'
    print('h = ', h)
    return render_template('index.html', title=tit, mu=h)


@app.route('/wc')
def wc():
    key = request.args.get('key')
    val = request.args.get('val')
    res = Response('SET COOKIE')
    res.set_cookie(key, val)
    session['Token'] = '123X'
    return make_response(res)


@app.route('/rc')
def rc():
    key = request.args.get('key')
    val = request.cookies.get(key)
    return 'cookie[ %s ] = %s, session: %s' % (key, val, session.get('Token'))


@app.route('/del')
def delete():
    if session.get('Token'):
        del session['Token']
    return 'Session 삭제완료'


@app.route('/dt')
def dt():
    datestr = request.values.get('date', date.today(), type=ymd('%Y-%m-%d'))
    return "우리나라 시간 형식: " + str(datestr)


@app.route('/test_wsgi')
def wsgi_test():
    def application(environ, start_response):
        body = 'The request method was %s' % environ['REQUEST_METHOD']
        headers = [('Content-Type', 'text/plain'),
                   ('Content-Length', str(len(body)))]
        start_response('200 OK', headers)
        return [body]

    return make_response(application)


@app.route("/res1")
def res1():
    custom_res = Response("Custom Response", 200, {'test': 111})
    return make_response(custom_res)


# @app.before_request
# def before_request():
#     print("before request!")
#     g.str = "한글"
#
#
# @app.route("/gg")
# def gg():
#     return 'Hello world' + getattr(g, 'str', '111')


@app.route("/")
def helloWorld():
    return "Hello Flask World!"


if __name__ == '__main__':
    # host 지정
    app.run(host="127.0.0.1", port="5000", debug=True)
