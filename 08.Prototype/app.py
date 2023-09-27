from flask import Flask, render_template, request, flash, session
from bp.crawling import crawl_bp
from bp.map import map_bp
from bp.user import user_bp
import os, random

app = Flask(__name__)
app.secret_key = 'qwert12345'                   # flash와 session을 사용하려면 반드시 설정해야 함
app.config['SESSOION_COOKIE_PATH'] = '/'


app.register_blueprint(crawl_bp, url_prefix='/crawling')   # localhost:5000/crawling/* 는 crawl_bp가 처리
app.register_blueprint(map_bp, url_prefix='/map')
app.register_blueprint(user_bp, url_prefix='/user')


@app.before_first_request       # 어떤 요청이 들어올때, 제일 처음 실행할것
def before_first_request():     # 최초 1회 실행
    global quotes, quote        # 다른곳에서도 수정할 수 있도록 global변수를 만듦
    global addr
    filename = os.path.join(app.static_folder, 'data/todayQuote.txt')
    with open(filename, encoding='utf-8') as file:
        quotes = file.readlines()       # 파일을 리스트형태로 읽음
    quote = random.sample(quotes, 1)[0]
    session['quote'] = quote
    addr = '서울시 영등포구'
    session['addr'] = addr

@app.route('/')
def home():
    menu = {'ho':1, 'us':0, 'cr':0, 'ma': 0, 'sc':0}
    # flash('Welcome to my Web')                  # flash 이용하면 해당 alert메세지 쓸수 있음 
    return render_template('home.html', menu=menu)



@app.route('/schedule')
def schedule():
    menu = {'ho':0, 'us':0, 'cr':0, 'ma': 0, 'sc':1}
    return render_template('schedule.html', menu=menu)




if __name__ == '__main__':
    app.run(debug=True)