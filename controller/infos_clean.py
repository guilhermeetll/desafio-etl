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

        print(df_proposicao)

        return df_proposicao
    

    def _create_first_df_tramitacao(self, api_results):
        pass
