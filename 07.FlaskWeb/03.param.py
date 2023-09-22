from flask import Flask, render_template, request

app = Flask(__name__)          

@app.route('/')                 # localhost:5000/   을 서비스하기 위한 코드                 
def index():                    
    return '<h1>파라메터 전달값 받기</h2>'

# localhost:5000/area?pi=3.14&radius=10
@app.route('/area')
def area():
    # 이렇게 두가지 방법으로 파라메터에 읽을 수 있음

    pi = request.args.get('pi', '3.14159')  # 1
    # requsest.args.get은 디폴트 값을 지정 가능
    # (디폴트값 없이 넣으면 result 계산식에서 오류남)

    radius = request.values['radius']       # 2
    # request.values는 디폴트값 지정 불가
    # GET/POST 모두 사용할 수 있음

    result = float(pi) * float(radius) ** 2
    return f'<h1> pi={pi}, radius={radius}, area={result}</h1>'
# 구식으로 받는 방식..    


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('02.login.html')
    else:       # POST이면
        uid = request.form['uid']           # login.html에서 name으로 지정한 이름 불러오기
        pwd = request.values['pwd']
        return f'<h1>uid={uid}, pwd={pwd} 환영합니다.</h1>'
    
@app.route('/sample', methods=['GET', 'POST'])
def sample():
    if request.method == 'GET':
        return render_template('02.sample.html')
    else:       # POST이면
        a = int(request.form['a'])
        b = int(request.values['b'])
        return f'<h1> a={a}, b={b}, a * b ={a * b}</h1>'
 


if __name__ == '__main__':
    app.run(debug=True)         

