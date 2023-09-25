import os
import numpy as np
import numpy as np
import matplotlib.pyplot as plt
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def index():
    return '''<h1>산점도 그리기</h1>
                <button onclick="location.href='/scatter'">실행</button>'''

@app.route('/scatter/', methods=['GET', 'POST'])
def scatter():
    if request.method == 'GET':
        return render_template('99.scatter_form.html')
    else:
        num = int(request.form['num'])          # 함수이름으로 변수를 두는건 좋지않음
        avg = float(request.form['avg'])
        std = float(request.form['std'])
        min = float(request.form['min'])
        max = float(request.form['max'])
        xs = np.random.normal(avg, std, num)        # 평균, 표준편차, 갯수
        ys = np.random.uniform(min, max, num)       # 최소, 최대, 갯수
        plt.figure()                                # 그래프 그릴때마다 해주기
        plt.scatter(xs, ys)                         # 산점도 그림
        # plt.savefig('../static/img/scatter.png')    # 권하지 않는 방법
        filename = os.path.join(app.static_folder, 'img/scatter.png')      # static_folder => static위치로 바로 지정
        plt.savefig(filename)
        #return render_template('99.scatter_res.html', avg=avg, std=std, min=min, max=max) 파라메타 하나하나 직접 전달
        params = {'avg':avg, 'std':std, 'min':min, 'max':max}
        return render_template('99.scatter_res.html', params=params)    # 딕셔너리로 파라메타 전달(파라메타 많을 경우 이 방법 추천)


if __name__ == '__main__' :
    app.run(debug=True)