from flask import Flask
from database.sqlite_db import init_db
from routers import index_router,tarefa_router,agenda_router

app = Flask(__name__)
init_db(app)

#ROTAS
index_router.add_routes(app)
tarefa_router.add_routes(app)
agenda_router.add_routes(app)


if __name__ == "__main__":
    app.run(debug=True)