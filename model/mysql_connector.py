import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

class MySQLConnector:
    def __init__(self):
        try:
            self.con = mysql.connector.connect(
                host="localhost",
                port=3307,
                database=os.getenv("DATABASE"),
                user="root",
                password=os.getenv("ROOT_PASSWORD")
            )
            print("Connection successful")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def __enter__(self):
        self.cursor = self.con.cursor()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.cursor.close()
        self.con.close()
        print("Conexao fechou")

    def __table_exists(self, table_name):
        self.cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
        result = self.cursor.fetchone()
        return result is not None

    def _create_tables(self):
        table = {}
        if not self.__table_exists("Proposicao"): table["Proposicao"] = (
                "CREATE TABLE IF NOT EXISTS Proposicao ("
                "  id INT AUTO_INCREMENT PRIMARY KEY,"
                "  author VARCHAR(1500),"
                "  presentationDate TIMESTAMP,"
                "  ementa TEXT,"
                "  regime VARCHAR(500),"
                "  situation VARCHAR(500),"
                "  propositionType VARCHAR(500),"
                "  number VARCHAR(500),"
                "  year INT,"
                "  city VARCHAR(500) DEFAULT 'Belo Horizonte',"
                "  state VARCHAR(500) DEFAULT 'Minas Gerais'"
                ") ENGINE=InnoDB"
            )

        if not self.__table_exists("Tramitacoes"): table["Tramitacoes"] = (
                "CREATE TABLE IF NOT EXISTS Tramitacoes ("
                "  id INT AUTO_INCREMENT PRIMARY KEY,"
                "  createAt TIMESTAMP,"
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


# if __name__ == "__main__":
#     with MySQLConnector() as connector:
#         connector._create_tables()