# IMPORTS
from flask import Flask
from flask import render_template, url_for, flash, redirect
from forms import RegForm, LogForm

app = Flask(__name__)

# SECURITY
app.config['SECRET_KEY'] = 'a233ef22439532d85a2eceb78db7c777'
# key : a233ef22439532d85a2eceb78db7c777

# CHATS
chats =[
    {
        'author':'Shabad',
        'title':'First chat',
        'content':'I like to chat',
        'date_posted':'Dec 29, 2019'
    },
    {
        'author':'Agam',
        'title':' Chatting with friends',
        'content':'I like to chat',
        'date_posted':'Dec 29, 2019'
    }

]

# URLS :

# HOME 
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',chats=chats)

# ABOUT
@app.route('/about')
def about():
    return render_template('about.html', title='About')

# REGISTRATION
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Registration', form=RegForm)

# LOGIN
@app.route('/login')
def login():
    form = LogForm()
    return render_template('login.html', title='Login', form=form)




# run  without restarting server
if __name__ == '__main__':
    app.run(debug=True)

