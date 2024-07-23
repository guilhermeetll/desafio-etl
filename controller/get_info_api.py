import requests
import pandas as pd
from traceback import print_exc


class GetInfoAPI:

    def __init__(self) -> None:
        self.url = 'https://dadosabertos.almg.gov.br/ws/proposicoes/pesquisa/direcionada?tp=1000&formato=json&ano=2023&ord=3'
        self.response = None
        self.results = None

    def _get_data(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raise an exception for HTTP errors
            self.response = response.json()
        except requests.RequestException as e:
            print("Error fetching data from API:", e)
            print_exc()
            raise

    def _extract_results(self):
        try:
            self.results = self.response['resultado']['listaItem']
        except KeyError:
            raise ValueError('Results not exist')
        
        