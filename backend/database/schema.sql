CREATE TABLE IF NOT EXISTS Evento (
    codigo TEXT PRIMARY KEY,
    titulo TEXT,
    date   DATE
);

CREATE TABLE IF NOT EXISTS Tarefa (
    codigo     TEXT PRIMARY KEY,
    titulo     TEXT NOT NULL,
    conteudo   TEXT NOT NULL,
    datetime   TEXT NOT NULL,
    status     TINYINT(1) NOT NULL DEFAULT (0)
);

CREATE TABLE IF NOT EXISTS MensagemMotivacional (
    codigo TEXT PRIMARY KEY,
    conteudo TEXT
)