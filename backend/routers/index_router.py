from flask import Flask
from controllers.index_controller import index

def add_routes(app: Flask):
    app.add_url_rule("/","index", index, methods=["GET"])