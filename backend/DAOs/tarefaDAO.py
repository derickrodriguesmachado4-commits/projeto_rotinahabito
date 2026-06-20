from database.sqlite_db import executar,consultar

def lista_modelo(lista_objeto):
    from models.tarefa import Tarefa
    result = []
    #CONVERTER DE OBJETO PARA MODELO
    for linha in lista_objeto:
        data_tarefa = {
            "codigo":linha[0],
            "titulo":linha[1],
            "conteudo":linha[2],
            "datetime":linha[3],
            "status":linha[4]
        }
        result.append(Tarefa(data_tarefa))
    return result

class TarefaDAO:
    def save(self,tarefa):
        sql = "INSERT INTO Tarefa (codigo,titulo,conteudo,datetime) VALUES (?,?,?,?);"
        values = (tarefa.data["codigo"],tarefa.data["titulo"],
                  tarefa.data["conteudo"],tarefa.data["datetime"])
        result = executar(sql,values)
        return result
    
    def read_one(self,codigo):
        sql = "SELECT codigo,titulo,conteudo,datetime,status FROM Tarefa WHERE codigo = ?;"
        values = (codigo,)
        result_db = consultar(sql,values)

        result = lista_modelo(result_db)
        return result
    
    def get_by_data(self,data):
        sql = "SELECT codigo,titulo,conteudo,datetime,status FROM Tarefa WHERE DATE(datetime) = ? ORDER BY datetime;"
        result_db = consultar(sql,(data,))

        result = lista_modelo(result_db)
        return result
    
    def get_by_mes(self,mes):
        sql = "SELECT codigo,titulo,conteudo,datetime,status FROM Tarefa WHERE strftime('%m',datetime) = ?;"
        result_db = consultar(sql,(mes,))

        result = lista_modelo(result_db)
        return result
    
    def read_all(self):
        sql = "SELECT codigo,titulo,conteudo,datetime,status FROM Tarefa;"
        result_db = consultar(sql)

        result = lista_modelo(result_db)
        return result

    def edit(self,tarefa):
        sql = "UPDATE Tarefa SET titulo = ?, conteudo = ?, datetime = ? WHERE codigo = ?;"
        values = (tarefa.data["titulo"],tarefa.data["conteudo"],tarefa.data["datetime"],tarefa.data["codigo"])
        result = executar(sql,values)
        return result
    
    def alterar_status(self,codigo):
        sql = "UPDATE Tarefa SET status = NOT status WHERE codigo = ?;"
        values = (codigo,)
        result = executar(sql,values)
        return result
    
    def delete(self,codigo):
        sql = "DELETE FROM Tarefa WHERE codigo = ?;"
        values = (codigo,)
        result = executar(sql,values)
        return result