import pandas as pd
from .mysql_connector import MySQLConnector


class MySQLCRUD(MySQLConnector):

    def __init__(self):
        super().__init__()

    def _create(self, table, *args, **kwargs):
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
        string = string.replace('"', "'")
        string = string.replace('\n', ' ')
        string = f'"{string}"'
        string = ' '.join(string.split())
        return string