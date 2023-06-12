#!/usr/bin/python3
import os
from flask import Flask, render_template, redirect, flash, url_for, flash
from flask_wtf import FlaskForm
from forms import LoginForm, RegisterForm
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, Conditions, Strategies, User
from routes import api_db
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'mindpal.db')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql:///admin:admin123@localhost/mindpal_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secrete secret key'
migrate = Migrate(app, db)
app.register_blueprint(api_db)
login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = 'login'
db.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/logout')
def logout():
    if current_user.is_authenticated:
        logout_user()
        flash('Logged out successfully..')
    return redirect(url_for('home'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('Logged in successfully')
            return redirect(url_for('all_condions'))
        else:
            flash('invalid password')
    return render_template('login.html', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(
            form.password.data, method='sha256')
        new_user = User(name=form.name.data,
                        surname=form.surname.data,
                        username=form.username.data,
                        password=hashed_password,
                        email=form.email.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successfully')
        return redirect(url_for('login'))
    return render_template('signup.html', form=form)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/services')
def services():
    return render_template('services.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/users')
def get_users():
    users = User.query.all()
    user_data = []
    for user in users:
        user_info = {
            'name': user.name,
            'surname': user.surname,
            'username': user.username,
            'email': user.email
        }
        user_data.append(user_info)
    return render_template('users.html', users=user_data)


@app.route('/all_condions')
@login_required
def all_condions():
    conditions = Conditions.query.all()
    strategies = {}
    for condition in conditions:
        strategies[condition.id] = condition.strategy
    return render_template('conditions.html', conditions=conditions, strategies=strategies)


@app.route('/strategy/<int:condition_id>')
@login_required
def strategy(condition_id):
    condition = Conditions.query.get(condition_id)
    if condition:
        strategies = Strategies.query.filter_by(
            condition_id=condition.id).all()
        return render_template('strategy.html', condition=condition, strategies=strategies)
    else:
        flash('Condition not found.', 'error')


@app.route('/strategy_details/<int:strategy_id>')
@login_required
def strategy_details(strategy_id):
    strategy = Strategies.query.get(strategy_id)
    if strategy:
        return render_template('strategy_details.html', strategy=strategy)
    else:
        flash('Strtegy not found.', 'error')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
