from Flask_app import app
from flask import render_template, redirect, session, request, flash
from Flask_app.models.user import User
from Flask_app.models.recipe import Recipe

@app.route('/home')
def r_home():
    if session.get('user_id') == None:
        return redirect('/login')
    else:
        user = User.get_user_from_id(session['user_id'])
        recipes = Recipe.get_all_recipes()
        return render_template('home.html', user =user, recipes = recipes)

@app.route('/add_recipe')
def r_add_recipe():
    if session.get('user_id') == None:
        return redirect('/login')
    else:
        return render_template('add_recipe.html', user_id = session['user_id'])

@app.route('/add-recipe', methods = ['POST'])
def f_add_recipe():
    if Recipe.val_recipe(request.form):
        Recipe.add_recipe(request.form)
        return redirect('home')
    else:
        return redirect('/add_recipe')

@app.route('/delete/<id>')
def delete_recipe(id):
    if session.get('user_id') == None:
        return redirect('/login')
    recipe = Recipe.get_recipe_from_id(id)
    if session.get('user_id') == recipe.user_id:
        Recipe.delete_recipe(id)
    return redirect('/home')

@app.route('/view/<id>')
def r_view_recipe(id):
    if session.get('user_id') == None:
        return redirect('/login')
    recipe = Recipe.get_recipe_from_id(id)
    user = User.get_user_from_id(session['user_id'])
    return render_template('view_recipe.html', recipe = recipe, user = user)

@app.route('/edit/<id>')
def r_edit_recipe(id):
    if session.get('user_id') == None:
        return redirect('/login')
    user = User.get_user_from_id(session['user_id'])
    recipe = Recipe.get_recipe_from_id(id)
    if user.first_name != recipe.creator:
        return redirect('/home')
    return render_template('edit_recipe.html', recipe = recipe, user = user)

@app.route('/edit-recipe', methods = ['POST'])
def f_edit_recipe():
    if Recipe.val_recipe(request.form):
        Recipe.edit_recipe(request.form)
        return redirect('/home')
    else: 
        return redirect('/edit/' + request.form['id'])