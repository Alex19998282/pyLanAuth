"""
Webserver routing

    /
    /login  Route to the main page
"""
# Python stl imports

# External module imports
from flask import Flask, render_template

# Internal module imports
from lanauth.api import load_api


class App(Flask):
    """
    Web application
    """

    def configure_views(self):
        """Configures core views"""

        @self.route('/')
        @self.route('/login')
        def login():
            """Route to login (index) page"""
            return render_template('login.html')


def app_factory(app_name, config, blueprints=None):
    """Build the webappi
    
    :param str app_name:        Name of the Flask application
    :param config:              Site configuration
    :param list blueprints:     List of blueprint tuples to load formatted as:
                                (blueprint class, "end point")
    """
    app = App(app_name)
    app.config.update(config)
    app.configure_views()
    if blueprints is not None:
        for blueprint, prefix in blueprints:
            app.register_blueprint(blueprint, url_prefix=prefix)

    load_api(app)
    return app

