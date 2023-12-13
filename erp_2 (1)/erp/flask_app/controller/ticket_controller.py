from flask_app import app
from flask import render_template,session,redirect,request
from flask_app.model.employee_model import Employee
from flask_app.model.recipes_model import Recipe
from flask_app.model.ticket_model import Ticket

@app.route('/cash_register')
def cash_register():
    data={'id':session['user_id']}
    employees=Employee.get_by_id(data)
    print(employees,")))))))))))))")
    datax={'owner_id':employees.owner_id}
    recipes = Recipe.get_all(datax)
    # owner= data={'employee.owner_id':session['user_id']}:
    return render_template('cash_register.html',recipes=recipes)


@app.route("/cashier/aa" ,methods=["post"])
def cashier():
    recipe_id = request.form["id"]
    recipe_name = request.form["recipe_name"]
    recipe_quantity = request.form["quantity"]
    recipe_price = request.form["recipe_price"]
    print(recipe_id,recipe_name,recipe_quantity)
    if "recipes" not in session:
        print("****************************")
        session["recipes"]=[]
    list=session["recipes"]
    dict={
            "recipes_id":recipe_id,
            "recipe_name":recipe_name,
            "recipe_quantity":recipe_quantity,
            "recipe_price":recipe_price
        }
    found=False
    for i in list:
        if i["recipes_id"]==recipe_id:
            i["recipe_quantity"]=int(i["recipe_quantity"])+int(request.form["quantity"])
            found=True
    if found==False:
        list.append(dict)
    print("--------------------++==",list)
    session["recipes"]=list
        # session["recipe"]=recipe_id
        # session["recipe_name"]=recipe_name
        # session["recipe_quantity"]=recipe_quantity
        # session["recipe_price"]=recipe_price
    # else:
    #     session["recipe_quantity"]=
    #     print("&&&&&&&&&&&&&&&&&&&&&&&")
    # print(session,"-((((((((((((((()))))))))))))))")
    # if 'item' in session:
    #     session.
    #     session['item'].append(request.form)
    #     print('SESSION1',session['recipe_ids'])
    #     return redirect("/cash_register")
    # session['recipe_ids']=request.form
    # print('SESSION2', session['recipe_ids'])
    

    return redirect("/cash_register")
    

@app.route("/cancel", methods=["post"])
def cancel():
    if "recipes" in session:
        session.pop("recipes")
    last=Ticket.get_last_ticket()
    print(last,"zzzzzzzz")
    return redirect("/cash_register")


@app.route("/ticket", methods=["post"])
def ticket():
    for item in session["recipes"]:
        one_item = {
        **item,
        "employee_id": session["user_id"],

        }
        Ticket.create_ticket(one_item)
        if "recipes" in session:
            session.pop("recipes")
    
    return redirect("/cash_register")



# for item in session:
#     one_item = {
#         **item,
#         "user_id": session["user_id"],

#     }


