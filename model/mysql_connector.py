import mysql.connector
import os
import time
from dotenv import load_dotenv

load_dotenv()

class MySQLConnector:
    """
    Classe responsável por estabelecer a conexão com o banco de dados MySQL.

    Métodos:
        __init__: Inicializa a classe e tenta conectar ao banco de dados.
        __create_con: Tenta criar a conexão com o banco de dados.
        __enter__: Inicializa o cursor para operações no banco de dados.
        __exit__: Fecha o cursor e a conexão com o banco de dados.
    """

    def __init__(self):
        """
        Inicializa a classe e tenta conectar ao banco de dados.
        Continua tentando até que a conexão seja bem-sucedida.
        """
        while True:
            try:
                self.__create_con()
                break # Sai do loop se a conexão for bem-sucedida
            except mysql.connector.Error as err:
                time.sleep(1) # Espera 1 segundo antes de tentar novamente

    def __enter__(self):
        """
        Inicializa o cursor para operações no banco de dados.
        Retorna a instância da classe.
        """
        self.cursor = self.con.cursor()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Fecha o cursor e a conexão com o banco de dados.
        """
        self.cursor.close()
        self.con.close()

    def __table_exists(self, table_name):
        self.cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
        result = self.cursor.fetchone()
        return result is not None
    
    def __create_con(self):
        """
        Tenta criar a conexão com o banco de dados.
        Define a conexão como um atributo da classe.
        """
        self.con = mysql.connector.connect(
            host="db",
            port=3306,
            database=os.getenv("DATABASE"),
            user="root",
            password=os.getenv("ROOT_PASSWORD")
        )

    def _create_tables(self):
        """
        Cria tabela de Proposicao caso não exista
        Cria tabela de Tramitacao caso não exista
        """
        table = {}
        if not self.__table_exists("Proposicao"): table["Proposicao"] = (
                "CREATE TABLE IF NOT EXISTS Proposicao ("
                "  id INT AUTO_INCREMENT PRIMARY KEY,"
                "  author VARCHAR(1500),"
                "  presentationDate TIMESTAMP,"
                "  ementa TEXT,"
                "  regime VARCHAR(500),"
                "  situation VARCHAR(500),"
                "  propositionType VARCHAR(250),"
                "  number VARCHAR(250),"
                "  year INT,"
                "  city VARCHAR(250) DEFAULT 'Belo Horizonte',"
                "  state VARCHAR(250) DEFAULT 'Minas Gerais'"
                ") ENGINE=InnoDB"
            )

        if not self.__table_exists("Tramitacao"): table["Tramitacao"] = (
                "CREATE TABLE IF NOT EXISTS Tramitacao ("
                "  id INT AUTO_INCREMENT PRIMARY KEY,"
                "  createdAt TIMESTAMP,"
                "  description TEXT,"
                "  local VARCHAR(500),"
                "  propositionId INT,"
                "  FOREIGN KEY (propositionId) REFERENCES Proposicao(id)"
                ") ENGINE=InnoDB"
            )

        for table_name, table_creation_query in table.items():
            try:
                print(f"Creating table {table_name}...")
                self.cursor.execute(table_creation_query)
                print(f"Table {table_name} created successfully.")
            except mysql.connector.Error as err:
                print(err.msg)