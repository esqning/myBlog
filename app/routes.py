from app import app
from flask import render_template, flash, redirect
from app.forms import LoginFrom


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'ning'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginFrom()
    if form.validate_on_submit():
        msg = 'Login requested for user {},remember_me={}'.format(form.username.data, form.remember_me.data)
        flash(msg)
        return redirect('/index')
    return render_template('login.html', title='login', form=form)
