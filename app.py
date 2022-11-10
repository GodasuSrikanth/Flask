#Basic flask program
""" from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1> Hello world</h1>"

if __name__=='__main__':
    app.run(debug = True) """

    #change default address

""" from flask import Flask

app = Flask(__name__)

@app.route("/courses")
def courses():
    return "python,java"
    

if __name__=='__main__':
    app.run(debug = True) """

    #dynamic routing---whatever you type in url it will print in web page
""" from flask import Flask

app = Flask(__name__)

@app.route("/<name>")
def name(name):
    return f"Hello {name}!"
    

if __name__=='__main__':
    app.run(debug = True) """

#Redirect,url_for
""" from flask import Flask,redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1> Hello world</h1>"

@app.route("/admin")
def admin():
   # return redirect('/')
     return redirect(url_for("home")) 
    

if __name__=='__main__':
    app.run() """ 

    #html
""" from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html",content = ['java', 'python','c#'])
    
@app.route("/index")
def index():
    return render_template("index.html")

if __name__=='__main__':
    app.run(debug = True) """


    #template inheritance

from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/index")
def index():
    return render_template("index.html")
   


if __name__=='__main__':
    app.run(debug=True)





