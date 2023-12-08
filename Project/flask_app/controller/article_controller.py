from flask_app import app
from flask import render_template, redirect, request, flash, session,url_for
from flask_app.model.article_model import Articles

@app.route("/add_articles")
def add():
    return render_template("add_article.html")


@app.route("/create",methods=['post'])
def create():
    # print("qqqqqqq",Articles.validate(request.form))
    if Articles.validate(request.form):
        data={
        **request.form,"stock_value":int(request.form["article_price"])*int(request.form["quantity_in_stock"])
        }
        # print(data)
        Articles.create(data)
        return redirect("all_articles")
    return redirect("add_articles")

@app.route("/all_articles")
def all():
    articles = Articles.get_all()
    # print(articles)
    return render_template("all_articles.html",articles=articles)



@app.route("/articles/<int:article_id>/edit", methods=['GET'])
def load_edit_form(article_id):
    data = {"id": article_id}
    print("((((((((((((((ffffffffffffffffff))))))))))))))",article_id)
    one = Articles.get_one(data)
    print(one,")))))))))))))))))))))))))))))))")
    session.clear('edit_article_data')
    
    session['edit_article_data'] = {
        'id': one.id,
        'article_name': one.article_name,
        'supplier': one.supplier,
        'article_price': one.article_price,
        'quantity_in_stock': one.quantity_in_stock
    }
    print(session['edit_article_data']['id'],'&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
    return None

# Route to process the form submission for updating an article
# @app.route("/articles/update", methods=['POST'])
# def update_article():
#     article_id = request.form.get('article_id')  # Assuming you have an input field with the name 'article_id'
    
#     # Fetch article data based on article_id
#     # Example: article = get_article_by_id(article_id)

#     # Update the article data based on the form submission
#     article_data = {
#         'updated_article_name': request.form.get('updated_article_name'),
#         'updated_supplier': request.form.get('updated_supplier'),
#         'updated_price': request.form.get('updated_price'),
#         'updated_qty_in_stock': request.form.get('updated_qty_in_stock')
#         # Add other fields as needed
#     }

#     # Update the article in the database
#     # Example: update_article(article_id, article_data)

#     flash("Article updated successfully", "success")
#     return redirect(url_for('all'))