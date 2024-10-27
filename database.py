from langchain_community.utilities.sql_database import SQLDatabase


def get_database():
    db = SQLDatabase.from_uri('sqlite:///database/estoque.db')
    return db
