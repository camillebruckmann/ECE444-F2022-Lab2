from flask_bootstrap import Bootstrap
from flask import Flask, render_template, session, redirect, url_for, flash
from datetime import date, datetime
from flask_moment import Moment

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField
from wtforms.validators import DataRequired

class NameForm(FlaskForm):
    name = StringField('What is your name?',validators=[DataRequired()])
    email = EmailField('What is your UofT email address?',validators=[DataRequired()])
    submit = SubmitField('Submit')

app = Flask(__name__)
app.config['SECRET_KEY']= 'QETUOadgjlZCBM'
bootstrap = Bootstrap(app)
moment = Moment(app)
@app.route('/', methods=['GET', 'POST']) 
def index(): 
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name') 
        if old_name is not None and old_name != form.name.data: 
            flash('Looks like you have changed your name!') 
            session['name'] = form.name.data 
            form.name.data = ''
        old_email = session.get('email') 
        if old_email is not None and old_email != form.email.data: 
            flash('Looks like you have changed your email!') 
            if ("utoronto" in form.email.data):
                session['email'] = form.email.data
                form.email.data = ''
            else:
                session['email'] = ''
                form.email.data = ''
    
    return render_template('index.html', form=form,email=session.get('email'), name=session.get('name'))

@app.route('/user/<name>')
def user(name):
    print(datetime.utcnow())
    return render_template('user.html',name=name, current_time = datetime.utcnow())
