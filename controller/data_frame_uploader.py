from model.mysql_crud import MySQLCRUD
import pandas as pd


class DataFrameUploader:
    """
    Classe responsável por carregar dados de um DataFrame para um banco de dados MySQL.

    Esta classe utiliza a classe `MySQLCRUD` para inserir os dados de um DataFrame em uma tabela do banco de dados.

    Atributos:
        df (pd.DataFrame): O DataFrame que contém os dados a serem carregados no banco de dados.

    Métodos:
        __init__(df): Inicializa a classe com o DataFrame a ser carregado.
        upload_to_db(table_name): Carrega os dados do DataFrame para a tabela especificada no banco de dados.
    """
    
    def __init__(self, df: pd.DataFrame):
        """
        Inicializa a classe DataFrameUploader com o DataFrame fornecido.

        Parâmetros:
            df (pd.DataFrame): O DataFrame que contém os dados a serem carregados.
        """
        self.df = df


    def upload_to_db(self, table_name: str):
        """
        Carrega os dados do DataFrame para a tabela especificada no banco de dados.

        Para cada linha no DataFrame, o método converte a linha em um dicionário e usa a classe `MySQLCRUD`
        para inserir os dados na tabela fornecida.

        Parâmetros:
            table_name (str): O nome da tabela no banco de dados onde os dados serão inseridos.

        Levanta:
            mysql.connector.Error: Se ocorrer um erro ao executar a operação de inserção no banco de dados.
        """
        for _, row in self.df.iterrows():
            data = row.to_dict()
            with MySQLCRUD() as crud:
                crud._create(table_name, **data)