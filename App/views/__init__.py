from App.views.blue_view import blue


def init_blue(app):
    app.register_blueprint(blue)
