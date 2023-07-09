from flask import render_template, request
from app.main import bp
from app.models import Recipe
from app.extensions import db

@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/submit', methods=['GET'])
def submit():
    return render_template('recipe.html')

@bp.route('/submit_recipe', methods=['POST'])
def submit_recipe():
    title = request.form.get('name')
    description = request.form.get('ingredients')
    instructions = request.form.get('instructions')
    

    return f'Recipe added successfully{title}'
    
    