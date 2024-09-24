'''
Daniel Park
Blue Stuff
SoftDev
K08: Understanding flask
2024-09-24
time-spent: 0.5 HR
'''

'''
DISCO:
We discovered that flask runs python scripts on the web, more specifically on servers.

QCC:
0. I have seen similar syntax in Java (Creating an instance of an object)
1. I think the "/" represents the root directory of your computer.
2. It will print to the console.
3. It will print the name of the module flask is running on, in this case it is __main__
4. It will appear on the web server the local host provides. I know this because I clicked on the link flask gave me after running the app.
5. I have seen similar function calls in Java. For example, .length()
 ...

INVESTIGATIVE APPROACH:
We first created a venv and installed flask there. Then we ran the flask app, and we followed the link it provided us. 
We then discovered that it displayed "No hablo queso!", which is what the hello_world function returns. From there, we put piece
with piece together and came to the conclusions.
'''


from flask import Flask

app = Flask(__name__)                    # Q0: Where have you seen similar syntax in other langs?

@app.route("/")                          # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__)                      # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"             # Q4: Will this appear anywhere? How u know?

app.run()                                # Q5: Where have you seen similar constructs in other languages?


