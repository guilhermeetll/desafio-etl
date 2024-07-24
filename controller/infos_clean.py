import pandas as pd


class InfosClean:

    def __init__(self, infos_api_results) -> None:
        self.df_proposicao_initial = self._create_first_df_proposicao(infos_api_results)
        self.df_tramitacao_initial = self._create_first_df_tramitacao(infos_api_results)


    def _create_first_df_proposicao(self, api_results):
        list_keys_proposicao = ['numero', 'ano', 'autor', 'ementa', 'situacao', 'dataPublicacao', 'regime', 'siglaTipoProjeto', 'city', 'state']

        data_for_dataframe = []

        for i in api_results:
            dict_for_dataframe = {k: i.get(k, '') for k in list_keys_proposicao}
            dict_for_dataframe['city'] = 'Belo Horizonte'
            dict_for_dataframe['state'] = 'Minas Gerais'
            data_for_dataframe.append(dict_for_dataframe)

        df_proposicao = pd.DataFrame(data_for_dataframe, columns=list_keys_proposicao)

        df_proposicao.rename(columns={'numero': 'number', 'ano': 'year', 'autor': 'author', 'situacao': 'situation',
                                      'dataPublicacao': 'presentationDate', 'siglaTipoProjeto': 'propositionType'}, inplace=True)

        dtype_mapping = {
            'number': 'str',
            'year': 'int',
            'author': 'str',
            'situation': 'str',
            'presentationDate': 'datetime64[ns]',  # 'datetime64[ns]' é usado para datas
            'propositionType': 'str',
            'ementa': 'str',
            'regime': 'str',
            'situation': 'str'
        }

        df_proposicao = df_proposicao.astype(dtype_mapping)

        df_proposicao['presentationDate'] = pd.to_datetime(df_proposicao['presentationDate'], errors='coerce')

        return df_proposicao
    

    def _create_first_df_tramitacao(self, api_results):

        list_keys_tramitacao = ['data', 'local', 'historico', 'propositionId', 'passo']

        data_for_dataframe = []

        for j, i in enumerate(api_results):

            for item in i['listaHistoricoTramitacoes']:
                item['propositionId'] = j + 1
                data_for_dataframe.append(item)

        df_tramitacao = pd.DataFrame(data_for_dataframe, columns=list_keys_tramitacao)

        df_tramitacao.rename(columns={'data': 'createdAt', 'local': 'local', 'historico': 'description'}, inplace=True)

        dtype_mapping = {
            'createdAt': 'datetime64[ns]',
            'local': 'str', 
            'description': 'str',
            'propositionId': 'int'
        }

        df_tramitacao = df_tramitacao.astype(dtype_mapping)

        df_tramitacao['createdAt'] = pd.to_datetime(df_tramitacao['createdAt'], errors='coerce')

        df_tramitacao.drop(columns=['passo'], inplace=True)

        print

        return df_tramitacao
