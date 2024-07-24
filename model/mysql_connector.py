import mysql.connector
import os
import time
from dotenv import load_dotenv

load_dotenv()

class MySQLConnector:
    def __init__(self):
        while True:
            try:
                self.__create_con()
                break
            except mysql.connector.Error as err:
                time.sleep(1)

    def __enter__(self):
        self.cursor = self.con.cursor()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.cursor.close()
        self.con.close()

    def __table_exists(self, table_name):
        self.cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
        result = self.cursor.fetchone()
        return result is not None
    
    def __create_con(self):
        self.con = mysql.connector.connect(
            host="db",
            port=3306,
            database=os.getenv("DATABASE"),
            user="root",
            password=os.getenv("ROOT_PASSWORD")
        )

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