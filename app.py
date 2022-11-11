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

""" from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/index")
def index():
    return render_template("index.html")
   


if __name__=='__main__':
    app.run(debug=True) """


#html requests and forms
#by using html requests we can transfer data from client side to server side.(Get and Post)


""" from flask import Flask,redirect,url_for,render_template,request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home1.html")

@app.route("/login",methods=["POST","GET"])
def login():
    if request.method == 'POST':
        user = request.form['usr_name']
        return redirect(url_for("user",usr=user))
    return render_template("login.html")

@app.route('/<usr>')
def user(usr):
    return f"Hello {usr}!"

if __name__=='__main__':
    app.run(debug=True) """

#sessions--session data stored on the server.session is the interval at which client logs on the server and logs out the server.
#the data required to be stored in the temporary directory on the server.

""" from flask import Flask,redirect,url_for,render_template,request,session
from datetime  import timedelta

app = Flask(__name__)
app.secret_key ="Flask"
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route("/")
def home():
    return render_template("home1.html")

@app.route("/login",methods=["POST","GET"])
def login():
    if request.method == 'POST':
        session.permanent = True
        user = request.form['usr_name']
        session['user'] =user
        return redirect(url_for("user"))
    else:
           if "user" in session:
            return redirect(url_for("user"))
    return render_template("login.html")

@app.route('/user')
def user():
    if 'user' in session:
        user = session['user']
        return f"You logged in as {user}!"
    else:
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user",None)
    return redirect(url_for("login"))

if __name__=='__main__':
    app.run(debug=True) """

#----------------------------------------------------------------------flash alerts

""" from flask import Flask,redirect,url_for,render_template,request,session
from datetime  import timedelta
from flask import flash

app = Flask(__name__)
app.secret_key ="Flask"
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route("/")
def home():
    return render_template("home1.html")

@app.route("/login",methods=["POST","GET"])
def login():
    if request.method == 'POST':
        session.permanent = True
        user = request.form['usr_name']
        session['user'] =user
        flash("Login Successful !!")
        return redirect(url_for("user"))
    else:
           if "user" in session:
               flash("You are already logged in !!")
               return redirect(url_for("user"))
    return render_template("login.html")

@app.route('/user')
def user():
    if 'user' in session:
        user = session['user']
        return render_template("user.html")
    else:
        flash("You are not logged in !")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user",None)
    flash ("You have been logged out!" ,'info')
    return redirect(url_for("login"))

if __name__=='__main__':
    app.run(debug=True)
 """


#Flask Wt forms

""" from flask import Flask,render_template
from flask_wtf import Form
from wtforms import StringField,SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'Flask'

class ContactForm(Form):
    name =StringField('What is your name?')
    submit = SubmitField('Submit')

@app.route('/',methods = ['GET','POST'])
def index():

    contact = ContactForm()
    name = False

    if contact.validate_on_submit():
        name = contact.name.data
        contact.name.data =' '
    return render_template('index1.html', contact = contact, name=name)

if __name__=='__main__':
    app.run(debug=True) """


#-------------------------------
from flask import Flask,render_template,request,flash
from form import ContactForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Flask'

@app.route('/')
def home():
    return "Welcome to wt forms"

@app.route('/contact',methods= ['GET','POST'])
def contact():
    form = ContactForm()

    if request.method == 'POST':
        if form.validate() == False:
            flash('All Fields are required')
            return render_template('contact.html',form = form)
        else:
            return 'Form Posted Successfully'
    return render_template('contact.html',form=form)

if __name__ =='__main__':
    app.run(debug=True)
           







