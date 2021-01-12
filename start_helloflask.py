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

@app.route('/main')
def main():
    return render_template('main.html', title="MAIN!!")


# request 처리 용 함수
def ymd(fmt):
    def trans(date_str):
        return datetime.strptime(date_str, fmt)

    return trans

class Nav:
    def __init__(self, title, url="#", children=[]):
        self.title = title
        self.url = url
        self.children = children

@app.route('/tmpl3')
def templ3():
    py = Nav('파이썬', 'https://search.naver.com')
    java = Nav('자바', 'https://search.naver.com')
    prg = Nav('프로그래밍 언어', 'https://search.naver.com', [py, java])

    jinja = Nav('jinja', 'https://search.naver.com')
    gc = Nav('Genshi, Cheetah', 'https://search.naver.com')
    flask = Nav('플라스크', 'https://search.naver.com', [jinja, gc])
    spring = Nav('스프링', 'https://search.naver.com')
    node = Nav('노드js', 'https://search.naver.com')
    web = Nav('웹 프레임워크', 'https://search.naver.com', [flask, spring, node])

    my = Nav('나의 일상', 'https://search.naver.com')
    issue = Nav('이슈 게시판', 'https://search.naver.com')
    others = Nav('기타', 'https://search.naver.com', [my, issue])

    return render_template('index.html', navs=[prg, web, others])

@app.route('/tmpl2')
def templ2():
    a = (1, '만남1', '김건모', False, [])
    b = (2, '만남2', '노사연', True, [a])
    c = (3, '만남3', '익명', False, [a, b])
    d = (4, '만남4', '익명', False, [a, b, c])

    return render_template('index.html', lst2=[a, b, c, d])

@app.route('/t')
def t():
    tit = Markup('<strong>Title</strong>')
    mu = Markup('<h1>iii = <i>%s</i></h1>')
    h = mu % 'Italic'
    print('h = ', h)
    
    lst = [('만남1', '김건모'), ('만남2', '노사연'), ('만남1', '김건모'), ('만남2', '노사연')]
    return render_template('index.html', title=tit, mu=h, lst=lst)


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
