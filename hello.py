from flask_bootstrap import Bootstrap
from flask import Flask, render_template
from datetime import date, datetime
from flask_moment import Moment
app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    print(datetime.utcnow())
    return render_template('user.html',name=name, current_time = datetime.utcnow())
