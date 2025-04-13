from flask import Flask,redirect,url_for,render_template
app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/result/<int:score>')
def result(score):
    if score>30:
        result='Success'
    else:
        result='Fail'
    return redirect(url_for(result,score=score))

@app.route('/Success/<int:score>')
def Success(score):
    return f"<html><body><h1>Congrats you got pass and your score is {score}<h1><body><html>"
@app.route('/Fail/<int:score>')
def Fail(score):
    return f'<html><body><h1>better luck next time you got failed and your score is {score}<h1><body><html>'



if __name__=='__main__':
    app.run(debug=True)