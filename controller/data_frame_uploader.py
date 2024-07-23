from model.mysql_crud import MySQLCRUD
import pandas as pd


class DataFrameUploader:
    def __init__(self, df: pd.DataFrame):
        self.df = df.drop(columns=['presentationDate'])

    def upload_to_db(self, table_name: str):
        for _, row in self.df.iterrows():
            data = row.to_dict()
            with MySQLCRUD() as crud:
                crud._create(table_name, **data)