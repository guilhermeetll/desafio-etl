import pandas as pd


class InfosClean:

    def __init__(self, infos_api_results) -> None:
        self.df_proposicao_initial = self._create_first_df_proposicao(infos_api_results)
        self.df_tramitacao_initial = self._create_first_df_tramitacao(infos_api_results)


    def _create_first_df_proposicao(self, api_results):
        list_keys_proposicao = ['numero', 'ano', 'autor', 'ementa', 'situacao', 'dataPublicacao', 'regime', 'city', 'state']

        data_for_dataframe = []

        for i in api_results:
            dict_for_dataframe = {k: i.get(k, '') for k in list_keys_proposicao}
            dict_for_dataframe['city'] = 'Belo Horizonte'
            dict_for_dataframe['state'] = 'Minas Gerais'
            data_for_dataframe.append(dict_for_dataframe)

        df_proposicao = pd.DataFrame(data_for_dataframe, columns=list_keys_proposicao)

        df_proposicao.rename(columns={'numero': 'number', 'ano': 'year', 'autor': 'author', 'situacao': 'situation',
                                      'dataPublicacao': 'presentationDate'}, inplace=True)

        dtype_mapping = {
            'number': 'str',
            'year': 'int',
            'author': 'str',
            'situation': 'str',
            'presentationDate': 'datetime64[ns]',  # 'datetime64[ns]' é usado para datas
            'ementa': 'str',
            'regime': 'str',
            'situation': 'str'
        }

        df_proposicao = df_proposicao.astype(dtype_mapping)

        df_proposicao['author'] = df_proposicao['author'].apply(self.remove_extra_spaces)

        return df_proposicao
    

    def _create_first_df_tramitacao(self, api_results):
        pass

    def remove_extra_spaces(self, text):
        if isinstance(text, str):  # Verifica se a entrada é uma string
            return ' '.join(text.split())
        return text
