from flask import Flask
from controllers.tarefa_controller import inicio,show_form_create,show_form_edit,criar,editar,trocar_status

def add_routes(app: Flask):
    app.add_url_rule("/tarefa/inicio/<data>","tarefa_inicio",inicio,methods=["GET"])
    app.add_url_rule("/tarefa/form_criar/<data>","form_criar_tarefa",show_form_create,methods=["GET"])
    app.add_url_rule("/tarefa/form_editar/<data>","form_editar_tarefa",show_form_edit,methods=["GET"])
    app.add_url_rule("/tarefa/criar/<data>","criar_tarefa",criar,methods=["POST"])
    app.add_url_rule("/tarefa/editar/<data>","editar_tarefa",editar,methods=["POST"])
    app.add_url_rule("/tarefa/trocar_status","trocar_status",trocar_status,methods=["POST"])