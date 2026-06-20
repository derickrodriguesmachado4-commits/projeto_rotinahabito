from flask import Flask
from controllers.agenda_controller import agenda

def add_routes(app:Flask):
    app.add_url_rule("/agenda/<data>","agenda",agenda,methods=["GET"])