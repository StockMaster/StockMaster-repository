from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash



class Ticket:
        def __init__(self, data):
            self.id = data["id"]
            self.employee_id = data["employee_id"]
            self.recipes_id = data["recipes_id"]
            self.recipe_quantity = data["recipe_quantity"]
            self.created_at = data["created_at"]
            self.updated_at = data["updated_at"]


        @classmethod
        def create_ticket(cls, data):
            ticket_query = """
                INSERT INTO tickets (employee_id, recipe_quantity,recipes_id ) 
                VALUES (%(employee_id)s, %(recipe_quantity)s, %(recipes_id)s);
            """
            return connectToMySQL(DATABASE).query_db(ticket_query, data)

        @classmethod
        def add_recipe_to_ticket(cls, data):
        
            query = """
                INSERT INTO tickets_has_recipes (ticket_id, recipe_id, quantity_per_ticket) 
                VALUES (%(ticket_id)s, %(recipe_id)s, %(quantity_per_ticket)s);
            """
            connectToMySQL(DATABASE).query_db(query,data)
