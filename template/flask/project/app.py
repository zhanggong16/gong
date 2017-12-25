pre_code = """from flask import Flask
from werkzeug.utils import import_string

blueprints = [
    '{package_name}.error.views:bp',
    '{package_name}.index.views:bp'
]


def create_app(config=None):
    app = Flask(__name__)
    
    #define blueprint
    for blueprint_name in blueprints:
        blueprint = import_string(blueprint_name)
        app.register_blueprint(blueprint)
    
    return app
"""
