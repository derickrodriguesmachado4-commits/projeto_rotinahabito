from database.sqlite_db import executar,consultar

class EventoDAO:

    def save(self,evento):
        sql = "INSERT INTO Evento VALUES (?,?,?);"
        values = (evento.data["codigo"],evento.data["titulo"],evento.data["date"])
        result = executar(sql,values)
        return result
    
    def read_one(self,codigo):
        from models.evento import Evento
        sql = "SELECT codigo,titulo,date FROM Evento WHERE codigo = ?;"
        values = (codigo,)
        result_db = consultar(sql,values)

        result = []
        #CONVERTER DE OBJETO PARA MODELO
        for linha in result_db:
            data_evento = {
                "codigo":linha[0],
                "titulo":linha[1],
                "date":linha[2]
            }
            result.append(Evento(data_evento))
        return result
    
    def get_by_data(self,data):
        from models.evento import Evento
        sql = "SELECT codigo,titulo FROM Evento where date = ?;"
        values = (data,)
        result_db = consultar(sql,values)

        result = []
        #CONVERTER DE OBJETO PARA MODELO
        for linha in result_db:
            data_evento = {
                "codigo":linha[0],
                "titulo":linha[1],
                "date":linha[2]
            }
            result.append(Evento(data_evento))
        return result
    

    
    def read_all(self):
        from models.evento import Evento
        sql = "SELECT codigo,titulo,date FROM Evento;"
        result_db = consultar(sql)

        result = []
        #CONVERTER DE OBJETO PARA MODELO
        for linha in result_db:
            data_evento = {
                "codigo":linha[0],
                "titulo":linha[1],
                "date":linha[2]
            }
            result.append(Evento(data_evento))

        return result
    
    def edit(self,evento):
        sql = "UPDATE Evento SET titulo = ?, date = ? WHERE codigo = ?;"
        values = (evento.data["titulo"],evento.data["date"],evento.data["codigo"])
        result = executar(sql,values)

        #CONVERTER DE OBJETO PARA MODELO

        return result
    
    def delete(self,codigo):
        sql = "DELETE FROM Evento WHERE codigo = ?;"
        values = (codigo,)
        result = executar(sql,values)
        return result