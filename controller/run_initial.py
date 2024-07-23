from model.mysql_crud import MySQLCRUD


class RunInitial:

    def __init__(self) -> None:
        self.CRUD = MySQLCRUD()
        
    def _start(self):
        self.CRUD._create_tables()