import os
from flask import Flask
from race_condition import settings


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=settings.SECRET_KEY,
        DATABASE=os.path.join(app.instance_path, "race_condition.sqlite"),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route("/hello")
    def hello():
        return "Hello, World!"

    from race_condition import db

    db.init_app(app)

    from race_condition import auth
    from race_condition import problems
    from race_condition import admin

    app.register_blueprint(problems.bp)
    app.register_blueprint(auth.bp)
    app.register_blueprint(admin.bp)

    return app
