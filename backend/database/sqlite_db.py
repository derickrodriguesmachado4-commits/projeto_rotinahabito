import sqlite3
from flask import g

# Arquivo do banco
DATABASE = "operacoes.db"

# Arquivo com o schema SQL
SCHEMA = "database/schema.sql"


def get_db():
    """
    Retorna uma conexão SQLite.
    Cria uma nova conexão caso ainda não exista.
    """

    db = getattr(g, "_database", None)

    if db is None:
        db = g._database = sqlite3.connect(DATABASE)

        # Habilita Foreign Keys
        db.execute("PRAGMA foreign_keys = ON")

        # Permite acessar colunas por nome
        db.row_factory = sqlite3.Row

    return db


def close_db(e=None):
    """
    Fecha a conexão ao final da requisição.
    """

    db = getattr(g, "_database", None)

    if db is not None:
        db.close()


def executar(query, params=()):
    """
    Executa INSERT, UPDATE e DELETE.
    Retorna a quantidade de linhas afetadas.
    """

    try:
        db = get_db()

        cursor = db.execute(query, params)

        db.commit()

        return cursor.rowcount

    except sqlite3.Error as e:

        db.rollback()

        print(f"Erro ao executar comando SQL: {e}")

        return 0


def consultar(query, params=()):
    """
    Executa SELECT.
    Retorna todos os registros encontrados.
    """

    try:
        db = get_db()

        cursor = db.execute(query, params)

        return cursor.fetchall()

    except sqlite3.Error as e:

        print(f"Erro ao consultar banco: {e}")

        return []


def executar_script_sql(arquivo_sql):
    """
    Executa um arquivo .sql completo.
    """

    try:

        with open(arquivo_sql, "r", encoding="utf-8") as f:
            script = f.read()

        db = get_db()

        db.executescript(script)

        db.commit()

        print("Banco inicializado com sucesso.")

    except sqlite3.Error as e:

        db.rollback()

        print(f"Erro ao executar script SQL: {e}")


def init_db(app):
    """
    Inicializa o banco de dados e registra o fechamento da conexão.
    """

    app.teardown_appcontext(close_db)

    with app.app_context():

        executar_script_sql(SCHEMA)