# Clyde 'Thluffy' Sinclair
# SoftDev
# September 2024

# Runs a flask app locally, displays "No hablo queso!" on the server, and
# prints the module name in console. 

from flask import Flask
app = Flask(__name__)          # ...

@app.route("/")                # ...
def hello_world():
    print(__name__)            # ...
    return "No hablo queso!"   # ...

app.run()                      # ...
                
