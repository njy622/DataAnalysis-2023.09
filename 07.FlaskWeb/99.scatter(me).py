import os 
import numpy as np
import matplotlib.pyplot as plt
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>산점도 그리기</h1>'

@app.route('/scatter',methods=['GET','POST'])
def scatter_res():
    if request.method == 'GET':                
        return render_template('99.scatter.html')
    else:
        count = int(request.form['count'])
        min = int(request.form['min'])
        max = int(request.form['max'])
        mean = int(request.form['mean'])
        std = int(request.form['std'])

        x = np.random.normal(min, max, count)
        y = np.random.uniform(mean, std, count)

        plt.scatter(x,y)
        img_file = os.path.join(app.root_path, 'static/img/scatter.png')
        plt.savefig(img_file)
        mtime = int(os.stat(img_file).st_mtime)

        return render_template('99.scatter_res.html')


if __name__ == '__main__':
    app.run(debug=True)     # debug=True 변경한 사항이 바로 적용