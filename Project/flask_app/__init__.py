# __init__.py
from flask import Flask

DATABASE="python_project"


app = Flask(__name__)
app.secret_key = "shhhhhh"
