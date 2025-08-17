from flask import Flask
from models import db
from routes import routes_bp
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize DB without creating tables immediately
    db.init_app(app)
    
    # Register Blueprint
    app.register_blueprint(routes_bp)

    # Only create tables when explicitly requested (avoids startup errors)
    @app.cli.command("init-db")
    def init_db():
        with app.app_context():
            db.create_all()
            print("Database tables created!")

    return app

app = create_app()

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5002))
    debug = os.environ.get('FLASK_ENV') != 'production'
    app.run(host='0.0.0.0', port=port, debug=debug)



