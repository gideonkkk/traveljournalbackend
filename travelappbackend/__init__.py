from flask import Flask
from travelappbackend.config import config

def create_app():
    app = Flask(__name__)
    app.config.from_object(config['development'])  # Make sure the config dictionary is correctly set up

    # Import and register blueprints
    from travelappbackend.routes.auth import auth_bp
    from travelappbackend.routes.posts import posts_bp
    from travelappbackend.routes.users import users_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(posts_bp)
    app.register_blueprint(users_bp)

    return app
