import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session
import secrets

app = Flask(__name__)

# In order to use "sessions",you need a "secret key".
# This is something random you generate.  
# For more info see: https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY
key = secrets.token_urlsafe(16)
app.secret_key = os.environ["SECRET_KEY"]#This is an environment variable.  
#run set SECRET_KEY=your_random_secret_key to get cmd prompt to run it.
                                     #The value should be set on the server. 
                                     #To run locally, set in env.bat (env.sh on Macs) and include that file in gitignore so the secret key is not made public.

@app.route('/')
def renderMain():
    return render_template('home.html')

@app.route('/startOver')
def startOver():
    session.clear() #clears variable values and creates a new session
    return redirect(url_for('renderMain')) # url_for('renderMain') could be replaced with '/'

@app.route('/page1')
def renderPage1():
    return render_template('page1.html')

@app.route('/page2',methods=['GET','POST'])
def renderPage2():
    if "firstQuestion" not in session:
        session["firstQuestion"]=request.form['firstQuestion']
    return render_template('page2.html')

@app.route('/page3',methods=['GET','POST'])
def renderPage3():
    if "SecondQuestion" not in session:
        session["SecondQuestion"]=request.form['SecondQuestion']
    return render_template('page3.html')
    
@app.route('/page4',methods=['GET','POST'])
def renderPage4():
    if "ThirdQuestion" not in session:
        session["ThirdQuestion"]=request.form['ThirdQuestion']
    points=0
    if session["firstQuestion"] == str(10):
        reply1 = "Correct"
        points += 1
    else:
        reply1= "Wrong"
        
    if session["SecondQuestion"] == str(16):
        reply2 = "Correct"
        points += 1
    else:
        reply2= "Wrong"
        
    if session["ThirdQuestion"] == str(50):
        reply3 = "Correct"
        points += 1
    else:
        reply3 = "Wrong"
        
    return render_template('page4.html', response1 = reply1, response2 = reply2, response3 = reply3, points = points)
    
if __name__=="__main__":
    app.run(debug=True)
