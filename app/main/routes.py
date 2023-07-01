from flask import render_template, request
from app.main import bp

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/api/recipes')
def recipes():
    name =  "Chicken"
    instruction = "Cook before eaten"
    return f"{name}, {instruction}"    

@bp.route('/api/recipes/save')
def save_recipe():
    
    
    name = request.form.get("name")
    instructions = request.form.get("instructions")
    
    return f"{name},  {instructions} Submitted to form!"
    
    