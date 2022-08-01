from market import app
from flask import render_template,redirect,url_for,flash
from market.model import Item,User
from market.forms import RegisterForm
from market import db




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
        user_to_create = User(user=form.username.data,
                              email_address=form.email_address.data,
                              password_hash= form.password1.data)
        db.session.add(user_to_create)  
        db.session.commit()
        return redirect(url_for('home_page'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was a error creating your account: {err_msg}', category='danger')

    return render_template('register.html',form=form)
