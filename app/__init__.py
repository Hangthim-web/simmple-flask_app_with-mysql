from flask import Flask 
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost/mydb'

    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from app.routes.user import user_bp 
    app.register_blueprint(user_bp)
    
    return app 
