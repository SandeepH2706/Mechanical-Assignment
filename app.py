from flask import Flask
from models import db
from routes import routes_bp
from config import Config

def app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    with app.app_context():
        db.create_all()
    
    app.register_blueprint(routes_bp)
    return app

if __name__ == '__main__':
    app = app()
    app.run(debug=True)


