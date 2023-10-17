from flask import Flask, render_template, request, flash, session
from bp.crawling import crawl_bp
from bp.map import map_bp
from bp.user import user_bp
from bp.chatbot import chatbot_bp
from bp.schedule import schdedule_bp
import os, random
import util.map_util as mu
import util.weather_util as wu

app = Flask(__name__)
app.secret_key = 'qwert12345'       # flash와 session을 사용하려면 반드시 설정해야 함
app.config['SESSION_COOKIE_PATH'] = '/'

app.register_blueprint(crawl_bp, url_prefix='/crawling')    # localhost:5000/crawling/* 는 crawl bp가 처리
app.register_blueprint(map_bp, url_prefix='/map')
app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(chatbot_bp, url_prefix='/chatbot')
app.register_blueprint(schdedule_bp, url_prefix='/schedule')


@app.before_first_request
def before_first_request():         # 최초 1회 실행
    global quotes
    filename = os.path.join(app.static_folder, 'data/todayQuote.txt')
    with open(filename, encoding='utf-8') as file:
        quotes = file.readlines()
    session['quote'] = random.sample(quotes, 1)[0]
    session['addr'] = '서울시 영등포구'

# for AJAX ###################################################
@app.route('/change_quote')
def change_quote():
    quote = random.sample(quotes, 1)[0]
    session['quote'] = quote
    return quote

@app.route('/change_addr')
def change_addr():
    addr = request.args.get('addr')
    session['addr'] = addr
    return addr

@app.route('/weather')
def weather():
    # 서울시 영등포구 + '청' -> 도로명 주소 -> 카카오 로컬 -> 좌표 획득
    addr = request.args.get('addr') 
    lat, lng = mu.get_coord(app.static_folder, addr + '청')
    html = wu.get_weather(app.static_folder, lat, lng)
    return html

###################################################

@app.route('/')
def home():
    menu = {'ho':1, 'us':0, 'cr':0, 'ma':0, 'cb':0, 'sc':0}
    # flash('Welcome to my Web!!!')
    return render_template('home.html', menu=menu)


if __name__ == '__main__':
    app.run(debug=True)









"""
내 메모



from flask import Flask, render_template, request, flash, session
from bp.crawling import crawl_bp
from bp.map import map_bp
from bp.user import user_bp
import os, random
import util.map_util as mu
import util.weather_util as wu

app = Flask(__name__)
app.secret_key = 'qwert12345'                   # flash와 session을 사용하려면 반드시 설정해야 함
app.config['SESSOION_COOKIE_PATH'] = '/'


app.register_blueprint(crawl_bp, url_prefix='/crawling')   # localhost:5000/crawling/* 는 crawl_bp가 처리
app.register_blueprint(map_bp, url_prefix='/map')
app.register_blueprint(user_bp, url_prefix='/user')


@app.before_first_request       # 어떤 요청이 들어올때, 제일 처음 실행할것
def before_first_request():     # 최초 1회 실행
    global quotes, addr               # 다른곳에서도 수정할 수 있도록 global변수를 만듦
    filename = os.path.join(app.static_folder, 'data/todayQuote.txt')
    with open(filename, encoding='utf-8') as file:
        quotes = file.readlines()       # 파일을 리스트형태로 읽음
    session['quote'] = random.sample(quotes, 1)[0]
    session['addr'] = '서울시 영등포구'

# for AJAX #######################수정버튼 누르면 어사이드에 명언텍스트만 변경되는것
@app.route('/change_quote')
def change_quote():
    quote = random.sample(quotes, 1)[0]
    session['quote'] = quote
    return quote


@app.route('/change_addr')
def change_addr():
    addr = request.args.get('addr')
    session['addr'] = addr
    return addr

@app.route('/weather')
def weather():
    # 서울시 영등포구 + '청' -> 도로명 주소 -> 카카오 로컬 -> 좌표 획득
    addr = request.args.get('addr')
    lat, lng = mu.get_coord(app.static_folder, addr + '청')
    html = wu.get_weather(app.static_folder, lat, lng)
    #html = f'<img src="http://api.openweathermap.org/img/w/04d.png" height="32"><strong>튼구름</strong>, 온도: <strong>24.0</strong>&#8451'
    return html
    


######################################################################

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
    app.run(debug=True)"""