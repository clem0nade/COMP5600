from flask import Flask

def init_app():
    app = Flask(__name__, static_url_path="")

    with app.app_context():
        # Import routes
        from . import routes

        # Import Dash
        from .dashboard.app import init_dashboard
        app = init_dashboard(app)

        return app