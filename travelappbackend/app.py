from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from travelappbackend.config import Config
from travelappbackend.routes.auth import auth_bp
from travelappbackend.routes.posts import posts_bp
from travelappbackend.routes.users import users_bp
from dotenv import load_dotenv

load_dotenv()  

db = SQLAlchemy() 
migrate = Migrate()  

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config['development'])  



    db.init_app(app)
    migrate.init_app(app, db)
    
  
    app.register_blueprint(auth_bp)
    app.register_blueprint(posts_bp)
    app.register_blueprint(users_bp)

    return app

if __name__ == "__main__":
    app = create_app() 
    app.run(debug=True)
