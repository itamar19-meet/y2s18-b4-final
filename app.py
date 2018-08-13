# Flask-related imports
from flask import Flask, render_template, url_for, redirect, request, session
# Add functions you need from databases.py to the next line!
from databases import add_user, get_all_msgs, get_user_by_name, check_password, add_message
from model import *
# Starting the flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdf movies'

# App routing code here
@app.route('/home')
def home():
    if 'user_name' in session:
        username = session['user_name']
        print ("hello "+username)
        if request.method == 'GET':

            return render_template('home.html', posts = get_all_msgs(), username = username)
        else:
            name = request.form['name']
            msg = request.form['message']
            add_message(name,msg)
            return render_template(

                "home.html",
                posts = get_all_msgs(),
                username = username


                )
    else:
        return redirect(url_for('login'))

#register route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        add_user(request.form['user_name'],
            request.form['password'])
        return redirect(url_for('login'))
#login route
@app.route('/', methods=(['GET' , 'POST']))
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        render_template('login.html')

        print("trying to login")

        username = request.form['user_name']
        password = request.form['password']
        if check_password(username,password) == True:
            print("good password")
            session['user_name'] = username
            return(redirect(url_for('home')))
        else:
            return(redirect(url_for('login')))
@app.route('/about_us')
def about_us():
    return render_template('about_us.html')


# Running the Flask app
if __name__ == "__main__":
    app.run(debug=True)
