# Blue Stuff: Daniel Park and Will Nzeuton
# SoftDev
# October 2024

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def disp_loginpage():
    return render_template( 'login.html' )

@app.route("/response")
def authenticate():
    return render_template('response.html', username = request.args['username'], request_method = request.method)

if __name__ == "__main__":
    app.debug = True 
    app.run()