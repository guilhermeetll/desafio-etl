import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

class MySQLConnector:
    try:
        con = mysql.connector.connect(
            host="localhost",
            port=3307,
            database=os.getenv("DATABASE"),
            user="root",
            password=os.getenv("ROOT_PASSWORD")
        )
        print("Connection successful")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

    def __init__(self) -> None:
        pass

    def __open_connect(self):
        self.cursor = self.con.cursor()

    def __close_cursor(self):
        self.cursor.close()

    def __close_con(self):
        self.con.close()

connector = MySQLConnector()