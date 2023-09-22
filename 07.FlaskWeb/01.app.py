from flask import Flask, render_template            # rendering : 표현(jsp파일을 HTML로 만드는것)

app = Flask(__name__)           # __name__ 내가 실행하는 것의 이름

@app.route('/')                 # localhost:5000/   을 서비스하기 위한 코드
def index():                    # 이름 아무렇게 줘도 됨
    return '<h1>Hello Falsk</h1><h2>Flask 좋아요!!!</h2>'

@app.route('/hello')
def hello():
    return render_template('01.hello.html')

@app.route('/sub/hello')
def sub_hello():
    return render_template('sub/01.hello.html')       
    # 통상적으로 route 괄호안과 template 안의 괄호는 동일하게 맞춰줌

if __name__ == '__main__':
    app.run(debug=True)         
# debug=True: py파일 내용을 추가하고 저장하면 
# 자동으로 서버 리로드되서 브라우저에서 새로고침하면 바로 적용됨(False는 자동 리로드 안됨)


# cmd에서 컨트롤+C는 서버닫는것