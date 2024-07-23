from model.mysql_crud import MySQLCRUD

class RunInitial:

    def __init__(self) -> None:
        with MySQLCRUD() as connector:
            connector._create_tables()
