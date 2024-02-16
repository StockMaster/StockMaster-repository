from flask_app import app
from flask import render_template,session,redirect,request,flash
from flask_app.model.owner_model import Owner
from flask_app.model.ticket_model import Ticket
from flask_app.model.pointing_model import Pointing
from flask_app.model.purchase_model import Purchase
from flask_app.model.article_model import Articles


from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/log')
def home_page():
    return render_template('login.html')

@app.route('/owner_register')
def owner_register():
    owners=Owner.get_all()
    turnovers=[]
    for i in owners:
        data={'owner_id':i.id}
        turnover=Ticket.sales_monthly(data)
        turnovers.append(turnover)
    return render_template('super_admin.html',owners=owners,turnovers=turnovers)
@app.route('/dashboard')
def dashboarding():
    if 'datacollect' in session:
        data=session['datacollect']
        all_sales=Ticket.sales_2_dates(data)
        top_products=Ticket.top_products_2_dates(data)
        pointingsPerEmployee=Pointing.pointings_2_dates_per_employee(data)
        totalPointings=Pointing.pointings_2_dates_total(data)
        totalPurchases=Purchase.purchases_2_dates(data)
        stock_value=Articles.stock_2_dates(data)
        print("💵💵💵",all_sales,'🥇🥈🥉',top_products,'⏰⏱️⌛',pointingsPerEmployee,'⏱️💵⏱️',totalPointings,totalPurchases)
        return render_template('dashboard.html',all_sales=all_sales,top_products=top_products,pointingsPerEmployee=pointingsPerEmployee,totalPointings=totalPointings,totalPurchases=totalPurchases,stock_value=stock_value)
    return render_template('dashboard.html')
    

@app.route('/dateview', methods=['post'])
def viewdashboard():
    data={**request.form,'owner_id':session['user_id']}
    session['datacollect']=data
    return redirect("/dashboard")

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
    return redirect("/log")