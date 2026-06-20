from DAOs.eventoDAO import EventoDAO

class Evento:
    def __init__(self,data):
        self.data = data
        self.errors = []

    def validate():
        pass

    def save(self):
        dao = EventoDAO()
        return dao.save(self)
    
    def read_one(self,codigo):
        dao = EventoDAO()
        return dao.read_one(codigo)

    def get_by_data(self,data):
        dao = EventoDAO()
        return dao.get_by_data(data)

    def read_all(self):
        dao = EventoDAO()
        return dao.read_all()

    def edit(self):
        dao = EventoDAO()
        return dao.edit(self)

    def delete(self,codigo):
        dao = EventoDAO()
        return dao.delete(codigo)