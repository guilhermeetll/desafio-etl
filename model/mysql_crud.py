import pandas as pd
from .mysql_connector import MySQLConnector


class MySQLCRUD(MySQLConnector):
    """
    Classe responsável por realizar operações CRUD (Create, Read, Update, Delete) no banco de dados MySQL.

    Herda:
        MySQLConnector: Classe base que estabelece a conexão com o banco de dados.

    Métodos:
        __init__: Inicializa a classe e a conexão com o banco de dados.
        _create: Insere um novo registro na tabela especificada.
        _read: Lê registros da tabela especificada com base nos critérios fornecidos.
        _update: Atualiza um registro existente na tabela especificada.
        _delete: Deleta registros da tabela especificada.
        __prepare_str: Prepara strings para serem inseridas no banco de dados.
    """

    def __init__(self):
        """
        Inicializa a classe MySQLCRUD e estabelece a conexão com o banco de dados.
        """
        super().__init__()

    def _create(self, table, *args, **kwargs):
        """
        Insere um novo registro na tabela especificada.

        Args:
            table (str): Nome da tabela onde o registro será inserido.
            *args: Argumentos posicionais adicionais (não usados).
            **kwargs: Dicionário com os dados a serem inseridos. As chaves são os nomes das colunas e os valores são os valores a serem inseridos.

        Returns:
            None
        """
        if kwargs == {}: return None
        
        list_keys = list(kwargs.keys())
        command = f'INSERT INTO {table} ('
        command_aux = ''
        for i in list_keys:
            command += f'{i}) ' if i == list_keys[-1] else f'{i}, '
            if type(kwargs[i]) == str:
                aux = self.__prepare_str(kwargs[i])
            elif type(kwargs[i]) == pd.Timestamp:
                aux = kwargs[i].strftime('%Y-%m-%d %H:%M:%S')
                aux = f"'{aux}'"
            else:
                aux = kwargs[i]

            command_aux += f'{aux}) ' if i == list_keys[-1] else f'{aux}, '
    
        command += f'VALUES ({command_aux}'
        self.cursor.execute(command)
        self.con.commit()

    def _read(self, table, *args, **kwargs):
        """
        Lê registros da tabela especificada com base nos critérios fornecidos.

        Args:
            table (str): Nome da tabela de onde os registros serão lidos.
            *args: Argumentos posicionais adicionais (não usados).
            **kwargs: Dicionário com os critérios de seleção. As chaves são os nomes das colunas e os valores são os valores a serem comparados.

        Returns:
            list: Lista de tuplas contendo os registros que atendem aos critérios.
        """
        if kwargs == {}: return None

        list_keys = list(kwargs.keys())
        command = f'SELECT * FROM {table} WHERE '

        for i in list_keys:
            if type(kwargs[i]) == str:
                aux = self.__prepare_str(kwargs[i])
            elif type(kwargs[i]) == pd.Timestamp:
                aux = kwargs[i].strftime('%Y-%m-%d %H:%M:%S')
                aux = f"'{aux}'"
            else:
                aux = kwargs[i]

            command += f'{i} = {aux} AND ' if i != list_keys[-1] else f'{i} = {aux}'

        self.cursor.execute(command)
        result = self.cursor.fetchall()
        return result
    
    def _update(self, table, id, **kwargs):
        """
        Atualiza um registro existente na tabela especificada.

        Args:
            table (str): Nome da tabela onde o registro será atualizado.
            id (int): ID do registro a ser atualizado.
            **kwargs: Dicionário com os novos valores. As chaves são os nomes das colunas e os valores são os novos valores a serem atribuídos.

        Returns:
            None
        """
        list_keys = list(kwargs.keys())
        command = f'UPDATE {table} SET '

        for i in list_keys:
            if type(kwargs[i]) == str:
                aux = self.__prepare_str(kwargs[i])
            elif type(kwargs[i]) == pd.Timestamp:
                aux = kwargs[i].strftime('%Y-%m-%d %H:%M:%S')
                aux = f"'{aux}'"
            else:
                aux = kwargs[i]
            command += f'{i} = {aux}, ' if i != list_keys[-1] else f'{i} = {aux}'

        command += f' WHERE id = {id}'

        self.cursor.execute(command)
        self.con.commit()
    
    def _delete(self, table, *args, **kwargs):
        pass

    def __prepare_str(self, string):
        """
        Prepara strings para serem inseridas no banco de dados.

        Args:
            string (str): String a ser preparada.

        Returns:
            str: String preparada para inserção no banco de dados.
        """
        string = string.replace('"', "'")
        string = string.replace('\n', ' ')
        string = f'"{string}"'
        string = ' '.join(string.split())
        return string