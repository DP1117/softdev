# Clyde 'Thluffy' Sinclair
# SoftDev
# September 2024

# Runs flask app locally, prints the module name, and displays "No hablo queso!"
from flask import Flask
app = Flask(__name__)             #create instance of class Flask

@app.route("/")                   #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)               #where will this go?
    return "No hablo queso!"

app.run()

