from flask import Flask, jsonify
import configurations as con
from app.extensions import db


def create_app(config_class=con.Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    #Initialize Flask extensions here
    db.init_app(app)

    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    
    @app.route('/create/')
    def save():
        
        return "User table create", 200

    return app