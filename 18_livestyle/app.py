# Blue Stuff: Daniel Park and Will Nzeuton
# SoftDev
# October 2024

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def disp_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.debug = True 
    app.run()