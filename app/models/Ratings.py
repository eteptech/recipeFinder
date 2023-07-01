from app.extensions import db

class Ratings (db.Model):
    
    __tablename__ = "Rating"
    
    id = db.Column(db.Integer, primary_key = True) 
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    score = db.Column(db.Integer)
    comment = db.Column(db.String(150))
    
    def __repr__(self):
        return f"<Rating {self.title}>"