from flask import redirect, url_for

def init_app(app):
    @app.route('/')
    def root():
        return redirect(url_for('api.home')) 