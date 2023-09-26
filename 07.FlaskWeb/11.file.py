from flask import Flask, render_template, request   

app = Flask(__name__)          

@app.route('/')                 # localhost:5000/   을 서비스하기 위한 코드
def index():                    
    return '<h1>파일 업로드</h1>'

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return render_template('11.file_form.html')
    else:
        file_image = request.files['image']
        return '<h1>환영합니다 </h1>'

if __name__ == '__main__':
    app.run(debug=True)         