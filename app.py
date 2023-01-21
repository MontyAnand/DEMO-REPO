from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///project.db"
db = SQLAlchemy(app)
class data:
    def __init__(self,grade,age):
        self.grade= grade
        self.age= age
        
        
@app.route("/",methods=['GET', 'POST'])
def call():
    if(request.method=='POST'):
        a = [request.form['grade'],request.form['age']]
        print (a)
        
        
    return render_template('index.html')


@app.route("/result",methods=['GET', 'POST'])
def result():
    return render_template("abc.html") 

if __name__=="__main__":
    app.run(port=8000)