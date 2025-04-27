import os
from flask import Flask
from models import db
from routes import routes_bp
from config import Config
from werkzeug.middleware.proxy_fix import ProxyFix

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Production configuration for proxy headers
    if os.environ.get('FLASK_ENV') == 'production':
        app.wsgi_app = ProxyFix(
            app.wsgi_app,
            x_for=1,
            x_proto=1,
            x_host=1,
            x_prefix=1
        )
    
    # Database initialization
    db.init_app(app)
    
    # Database table creation
    with app.app_context():
        db.create_all()
    
    # Blueprint registration
    app.register_blueprint(routes_bp)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=os.environ.get('FLASK_ENV') == 'development')



# from flask import Flask
# from models import db
# from routes import routes_bp
# from config import Config

# app = Flask(__name__)
# app.config.from_object(Config)
# db.init_app(app)

# with app.app_context():
#     db.create_all()

# app.register_blueprint(routes_bp)


# from flask import Flask
# from models import db
# from routes import routes_bp
# from config import Config

# def create_app():
#     app = Flask(__name__)
#     app.config.from_object(Config)
#     db.init_app(app)
#     app.register_blueprint(routes_bp)
#     return app

# if __name__ == '__main__':
#     app = create_app()
#     app.run(debug=True)


# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "Hello, World!"

# if __name__ == '__main__':
#     app.run(debug=True)
