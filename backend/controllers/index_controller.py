from datetime import date 
from flask import redirect

def index():
    hoje = date.today().strftime("%Y-%m-%d")
    return redirect(f"tarefa/inicio/{hoje}")