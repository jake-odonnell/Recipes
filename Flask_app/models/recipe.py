from Flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Recipe:
    def __init__(self, data:dict):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.made_at = data['made_at']
        self.under = data['under']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.creator = data['first_name']
        self.user_id = data['users.id']

    @classmethod
    def get_all_recipes(cls):
        query = 'SELECT * FROM recipes LEFT JOIN users ON users.id = recipes.user_id'
        results = connectToMySQL('recipes').query_db(query)
        recipes = []
        for recipe in results:
            recipes.append(cls(recipe))
        return recipes

    @classmethod
    def get_recipe_from_id(cls, id):
        query = 'SELECT * FROM recipes LEFT JOIN users ON users.id = recipes.user_id WHERE recipes.id = %(id)s;'
        data = {'id': id}
        result = connectToMySQL('recipes').query_db(query, data)
        return cls(result[0])

    @staticmethod
    def add_recipe(data:dict):
        query = "INSERT INTO recipes (name, description, instructions, made_at, user_id, under) VALUES(%(name)s, %(description)s, %(instructions)s, %(made_at)s, %(user_id)s, %(under)s);"
        connectToMySQL('recipes').query_db(query, data)
        return

    @staticmethod
    def val_recipe(data:dict):
        is_val = True
        print(data)
        if len(data['name']) < 3:
            flash('Must include recipe name with at least 3 characters')
            is_val = False
        if len(data['description']) < 3:
            flash('Must include description with at least 3 characters')
            is_val = False
        if len(data['instructions']) < 3:
            flash('Must include instructions with at least 3 characters')
            is_val = False
        if data['made_at'] == '':
            flash('Must include a date cooked')
            is_val = False
        if data.get('under') == None:
            flash('Must provide the time')
            is_val = False
        return is_val

    @staticmethod
    def edit_recipe(data:dict):
        query = """UPDATE recipes
        SET name = %(name)s, description = %(description)s, instruction = %(instructions)s, made_at = %(made_at)s, under = %(under)s
        WHERE id = user_id"""
        connectToMySQL('recipes').query_db(query, data)
        return


    @staticmethod
    def delete_recipe(data):
        query = 'DELETE FROM recipes WHERE id = %(id)s;'
        connectToMySQL('recipes').query_db(query, data)
        return