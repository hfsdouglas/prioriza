from routes.auth.auth import auth

def register_routes(app):
    app.register_blueprint(auth)