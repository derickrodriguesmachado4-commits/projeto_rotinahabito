from flask import render_template
from models.tarefa import Tarefa
from datetime import datetime
import calendar

def agenda(data):

    data_obj = datetime.strptime(data, "%Y-%m-%d")
    tarefas_do_mes = Tarefa({}).get_by_mes(f"{data_obj.month:02d}")

    ano = data_obj.year
    mes = data_obj.month

    calendario = calendar.monthcalendar(ano,mes)
    return render_template("agenda.html", context={"data":data_obj, "tarefas":tarefas_do_mes, "calendario":calendario})