from flask import render_template,request,redirect
from datetime import datetime
from models.tarefa import Tarefa
from models.evento import Evento

def show_form_create(data):
    return render_template("tarefa/criar.html",context={"data":data,"mensagem":[],"status":""})

def show_form_edit(codigo):
    tarefa = Tarefa({}).read_one(codigo)
    return render_template("tarefa/editar.html",context={"tarefa":tarefa,"mensagem":[],"status":""})


def separar_tarefas(tarefas):
    tarefas_dict = {
        "tarefas_feitas":[],
        "tarefas_pendentes":[]
    }
    for tarefa in tarefas:
        if tarefa.data["status"]:
            tarefas_dict["tarefas_feitas"].append(tarefa)
        else:
            tarefas_dict["tarefas_pendentes"].append(tarefa)
    return tarefas_dict

def inicio(data):
    eventos = Evento({}).get_by_data(datetime.strptime(data,"%Y-%m-%d").strftime("%Y-%m-%d"))
    tarefas = Tarefa({}).get_by_data(datetime.strptime(data,"%Y-%m-%d").strftime("%Y-%m-%d"))
    tarefas_dict = separar_tarefas(tarefas)

    return render_template("tarefa/inicio.html", context={
        "data": datetime.strptime(data,"%Y-%m-%d"),
        "tarefas_pendentes":tarefas_dict["tarefas_pendentes"],
        "tarefas_feitas":tarefas_dict["tarefas_feitas"],
        "eventos":eventos
        })

def criar(data):
    from uuid import uuid4
    data_tarefa = request.form.to_dict()
    data_tarefa["codigo"] = str(uuid4())
    tarefa = Tarefa(data=data_tarefa)
    tarefa.validate()

    if len(tarefa.errors) == 0:
        tarefa.save()
        return render_template("tarefa/criar.html",context={"data":datetime.strptime(data,'%Y-%m-%d'),"mensagem":["Tarefa criada com sucesso"],"status":"SUCESSO"})
    return render_template("tarefa/criar.html", context={"data":datetime.strptime(data,'%Y-%m-%d'),"mensagem":[tarefa.errors],"status":"ERRO"})

def editar():
    data_tarefa = request.form.to_dict()
    tarefa = Tarefa(data=data_tarefa)
    tarefa.validate()

    if len(tarefa.errors) == 0:
        tarefa.edit()
        return render_template("tarefa/editar.html",context={"data":tarefa.data["datetime"],"tarefa": tarefa,"mensagem":["Tarefa editado com sucesso"],"status":"SUCESSO"})
    return render_template("tarefa/editar.html", context={"data":tarefa.data["datetime"],"tarefa": tarefa,"mensagem":[tarefa.errors],"status":"ERRO"})
    
def deletar():
    data = request.form["data"]
    data_formatada = datetime.strptime(data,"%Y-%m-%dT%H:%M:%S").strftime("%Y-%m-%d")
    codigo = request.form["codigo"]
    Tarefa({}).delete(codigo)
    return redirect(f"/tarefa/inicio/{data_formatada}")

def trocar_status():
    data = request.form["data"]
    print(data)
    data_formatada = datetime.strptime(data,"%Y-%m-%dT%H:%M").strftime("%Y-%m-%d")
    codigo = request.form["codigo"]
    Tarefa({}).alterar_status(codigo)
    return redirect(f"/tarefa/inicio/{data_formatada}")