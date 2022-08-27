import os
from market import app
from flask import render_template,redirect,url_for,flash,request
from market.model import Item,User
from market.forms import LoginForm, RegisterForm
from market import db,mail
from flask_login import login_user
from flask_mail import Message
import smtplib
from threading import Thread


def send_async_email(app,msg):
    with app.app_context():
        mail.send(msg)


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/store')
def store_page():
    items = Item.query.all()
    return render_template('store.html', items=items)


@app.route('/register',methods=['GET','POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(user=form.username.data,
                              email_address=form.email_address.data,
                              password= form.password1.data)
        email_address = request.form.get("email_address") 
        msg = Message('Registration successful !', sender =   'Oayeni139@gmail.com',
         recipients = [email_address])
        msg.body = render_template('welcome.md')
        
        msg.attach = ("waterfall.jpg")

        thr =Thread(target=send_async_email,args=[app,msg])
        thr.start()
        db.session.add(user)  
        db.session.commit()
        return redirect(url_for('store_page'))
       
    
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was a error creating your account: {err_msg}', category='danger')

    return render_template('register.html',form=form)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.get(form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            
            login_user(attempted_user)
            flash(f'Successfully login as : {attempted_user.username}', category='success' )
            return redirect(url_for('store_page'))
        
        else:
            flash('Username and password are incorrect! Try again',category='danger')


    return render_template('login.html', form=form) 
    

    