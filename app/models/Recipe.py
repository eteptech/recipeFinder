from app.extensions import db
from datetime import datetime


class Recipe(db.Model):
    
    __tablename__ = "recipe"
        
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=True)
    rating = db.relationship('Rating', backref='recipe', lazy=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    img = db.Column(db.String(200))
    description = db.Column(db.String(250), unique=True, nullable=True)
    instructions = db.Column(db.String(250), unique=True, nullable=True)
    cookTime = db.Column(db.Integer, unique=True, nullable=True)
    prepTime = db.Column(db.Integer, unique=True, nullable=True) 
    createAt = db.Column(db.DateTime, default=datetime.utcnow)
    updated = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f"<User {self.title}>"