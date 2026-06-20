from DAOs.tarefaDAO import TarefaDAO

class Tarefa:
    def __init__(self,data):
        self.data = data
        self.errors = []

    def validate(self):
        titulo = self.data["titulo"]
        conteudo = self.data["conteudo"]

        if titulo.strip() == "":
            self.errors.append("Título não pode ser vazio")
        if conteudo.strip() == "":
            self.errors.append("Conteudo não pode ser vazio")


    def save(self):
        dao = TarefaDAO()
        return dao.save(self)
    
    def read_one(self,codigo):
        dao = TarefaDAO()
        return dao.read_one(codigo)

    def get_by_data(self,data):
        dao = TarefaDAO()
        return dao.get_by_data(data)
    
    def get_by_mes(self,mes):
        dao = TarefaDAO()
        return dao.get_by_mes(mes)

    def read_all(self):
        dao = TarefaDAO()
        return dao.read_all()

    def edit(self):
        dao = TarefaDAO()
        return dao.edit(self)
    
    def alterar_status(self,codigo):
        dao = TarefaDAO()
        return dao.alterar_status(codigo)

    def delete(self,codigo):
        dao = TarefaDAO()
        return dao.delete(codigo)