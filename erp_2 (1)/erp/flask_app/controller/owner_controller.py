from flask_app import app
from flask import render_template,session,redirect,request,flash
from flask_app.model.owner_model import Owner
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/login')
def home_page():
    return render_template('login.html')

@app.route('/owner_register')
def owner_register():
    owners=Owner.get_all()
    return render_template('super_admin.html',owners=owners)

@app.route('/register_owner', methods=['post'])
def owner_reg():
    if Owner.validate(request.form):
        pw_hash=bcrypt.generate_password_hash(request.form['password'])
        data={**request.form,'password':pw_hash}
        owner_id=Owner.create(data)
        session['owner_id']=owner_id
        session["first_name"]=data['first_name']
        return redirect("/owner_register")
    return redirect("/owner_register")

@app.route('/logout', methods=['post'])
def logout():
    session.clear()
    return redirect("/")