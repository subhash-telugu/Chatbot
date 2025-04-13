#intergratio=ng html with py and adding post tags


from flask import Flask,redirect,url_for,render_template,request
app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')



@app.route('/Success/<int:score>')
def Success(score):
    return f"<html><body><h1>Congrats you got pass and your score is {score}<h1><body><html>"
@app.route('/Fail/<int:score>')
def Fail(score):
    return f'<html><body><h1>better luck next time you got failed and your score is {score}<h1><body><html>'
@app.route('/submit',methods=['POST','GET'])
def submit():
    avg_score=0
    if request.method=='POST':
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        datascience=float(request.form['datascience'])
        c=float(request.form['c'])
        avg_score=(maths+science+datascience+c)/4
        return redirect(url_for('result',score=avg_score))

@app.route('/result/<int:score>')
def result(score):
    if score>35:
        result='Success'
    else:
        result='Fail'
    return render_template('result.html',result=result,score=score)

if __name__=='__main__':
    app.run(debug=True)