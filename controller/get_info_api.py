import requests
import pandas as pd
from traceback import print_exc


class GetInfoAPI:
    """
    Classe responsável por obter e extrair informações de uma API.

    Esta classe faz uma requisição para uma API pública para buscar dados sobre proposições e extrair os resultados relevantes.

    Atributos:
        url (str): URL da API para obter os dados.
        response (dict or None): Resposta da API em formato JSON, ou None se a requisição falhar.
        results (list or None): Lista de resultados extraídos da resposta da API, ou None se a extração falhar.

    Métodos:
        __init__(): Inicializa a URL da API e define os atributos de resposta e resultados como None.
        _get_data(): Faz uma requisição para a API e armazena a resposta no atributo `response`.
        _extract_results(): Extrai a lista de resultados da resposta da API.
    """

    def __init__(self) -> None:
        """
        Inicializa a classe GetInfoAPI configurando a URL da API e inicializando os atributos `response` e `results`.

        Parâmetros:
            Nenhum.
        """
        self.url = 'https://dadosabertos.almg.gov.br/ws/proposicoes/pesquisa/direcionada?tp=1000&formato=json&ano=2023&ord=3'
        self.response = None
        self.results = None

    def _get_data(self):
        """
        Faz uma requisição GET para a API e armazena a resposta em formato JSON no atributo `response`.

        Levanta uma exceção se houver um erro na requisição.

        Parâmetros:
            Nenhum.

        Levanta:
            requests.RequestException: Se houver um erro na requisição HTTP.
        """
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raise an exception for HTTP errors
            self.response = response.json()
        except requests.RequestException as e:
            print("Error fetching data from API:", e)
            print_exc()
            raise

    def _extract_results(self):
        """
        Extrai a lista de resultados da resposta da API e armazena no atributo `results`.

        Levanta uma exceção se a chave 'resultado' ou 'listaItem' não estiver presente na resposta.

        Parâmetros:
            Nenhum.

        Levanta:
            KeyError: Se a chave 'resultado' não estiver presente na resposta.
            ValueError: Se a lista de resultados não existir na resposta.
        """
        try:
            self.results = self.response['resultado']['listaItem']
        except KeyError:
            raise ValueError('Results not exist')
        
        