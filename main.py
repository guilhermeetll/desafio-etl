from controller.run_initial import RunInitial
from controller.get_info_api import GetInfoAPI
from controller.infos_clean import InfosClean
from controller.data_frame_uploader import DataFrameUploader


if __name__ == '__main__':

    """
    Função principal que executa o processo de inicialização, coleta de dados da API,
    limpeza dos dados e upload para o banco de dados.
    """
    try:
        print('Waiting for the db to finish rising to start executing the code ...')
        initial_create = RunInitial()  # Inicializa o banco de dados
        print('Database initialization completed.')

        print('Start ///////////////////')
        
        # Coleta dados da API
        infos_api = GetInfoAPI()
        print('Fetching data from API...')
        infos_api._get_data()
        infos_api._extract_results()
        print('Data fetched from API successfully.')

        # Limpeza e preparação dos dados
        infos_clean = InfosClean(infos_api.results)

        # Upload dos dados para o banco de dados
        uploader_proposicao = DataFrameUploader(infos_clean.df_proposicao_initial)
        uploader_proposicao.upload_to_db('Proposicao')
        print('Data for "Proposicao" uploaded successfully.')

        uploader_tramitacao = DataFrameUploader(infos_clean.df_tramitacao_initial)
        uploader_tramitacao.upload_to_db('Tramitacao')
        print('Data for "Tramitacao" uploaded successfully.')

        print('Creation and upload of all data was successful //////////////')

    except Exception as e:
        print("An error occurred:")
        print(e)