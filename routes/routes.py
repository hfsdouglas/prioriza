from routes.auth.login import auth

def register_routes(app):
    app.register_blueprint(auth)