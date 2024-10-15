# Blue Stuff: Daniel Park and Will Nzeuton
# SoftDev
# October 2024

import os
from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route("/")
def disp_loginpage():
    if 'username' not in session.keys():
        return render_template( 'login.html' )
    else:
        return response()

@app.route("/response")
def response():
    if 'username' not in session.keys():
        session['username'] = request.args['username']
    return render_template('response.html', username = session['username'], request_method = request.method)

@app.route("/logout")
def disp_logoutpage():
    session.pop('username')
    return render_template('logout.html')

if __name__ == "__main__":
    app.debug = True 
    app.run()