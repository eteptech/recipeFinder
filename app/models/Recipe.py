from app.extensions import db
from datetime import datetime


class Recipe(db.Model):
    
    __tablename__ = "recipe"
        
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    rating = db.relationship('Rating', backref='recipe', lazy=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    img = db.Column(db.String(200))
    description = db.Column(db.String(250), unique=True, nullable=False)
    instructions = db.Column(db.String(250), unique=True, nullable=False)
    cookTime = db.Column(db.Integer, unique=True, nullable=False)
    prepTime = db.Column(db.Integer, unique=True, nullable=False) 
    createAt = db.Column(db.DateTime, default=datetime.utcnow)
    updated = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f"<User {self.title}>"