from .mysql_connector import MySQLConnector


class MySQLCRUD(MySQLConnector):

    def __init__(self):
        super().__init__()

    def _create(self, table, *args, **kwargs: tuple[str, type]):
        if kwargs == {}: return None

        print(kwargs)

        list_keys = list(kwargs.keys())
        command = f'INSERT INTO {table} ('
        command_aux = ''
        for i in list_keys:
            command += f'{i}) ' if i == list_keys[-1] else f'{i}, '
            aux = kwargs[i]
            command_aux += f'{aux[1](aux[0])}) ' if i == list_keys[-1] else f'{aux[1](aux[0])}, '
    
        command += f'VALUES ({command_aux}'

        print(command)

        self.cursor.execute(command)
        self.con.commit()

    def _read(self, table, *args, **kwargs):
        if kwargs == {}: return None

        print(kwargs)

        list_keys = list(kwargs.keys())
        command = f'SELECT * FROM {table} WHERE '

        for i in list_keys:
            command += f'{i} = {kwargs[i]} AND ' if i != list_keys[-1] else f'{i} = {kwargs[i]}'

        print(command)

        self.cursor.execute(command)
        result = self.cursor.fetchall()
        return result
    
    def _update(self, table, id, **kwargs):

        list_keys = list(kwargs.keys())
        command = f'UPDATE {table} SET '

        for i in list_keys:
            command += f'{i} = {kwargs[i]}, ' if i != list_keys[-1] else f'{i} = {kwargs[i]}'

        command += f' WHERE id = {id}'
        print(command)

        self.cursor.execute(command)
        self.con.commit()
    
    def _delete(self, table, *args, **kwargs):
        pass
    
    
# with MySQLCRUD() as connector:
#     connector._create(table='Proposicao', year = (34, int), ementa = ('"Otimizado"', str))
    #print(connector._read(table='Proposicao', year = 34, ementa = '"Otimizado"'))
    #connector._update(table='Proposicao', id=1, ementa = '"Mudei para outro valor Maravilha"', author = '"Guilherme Tavaglia"')