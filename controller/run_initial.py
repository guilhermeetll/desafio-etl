from model.mysql_crud import MySQLCRUD

class RunInitial:
    """
    Classe responsável por executar operações iniciais no banco de dados.
    """

    def __init__(self) -> None:
        """
        Inicializa a classe RunInitial e cria as tabelas no banco de dados.

        Este método estabelece uma conexão com o banco de dados utilizando a classe MySQLCRUD e chama o método
        _create_tables para criar as tabelas necessárias.

        Raises:
            mysql.connector.Error: Se ocorrer um erro ao executar operações no banco de dados.
        """
        with MySQLCRUD() as connector:
            connector._create_tables()
