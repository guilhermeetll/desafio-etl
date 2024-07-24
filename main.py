import time
from controller.run_initial import RunInitial
from controller.get_info_api import GetInfoAPI
from controller.infos_clean import InfosClean
from controller.data_frame_uploader import DataFrameUploader


if __name__ == '__main__':

    try: 
        initial_create = RunInitial()
    except AttributeError:
        print('Waiting for the db to finish rising to start executing the code ...')
        time.sleep(20)
        initial_create = RunInitial()
    except:
        raise ConnectionError('Error create db.')
    
    print('Start ///////////////////')
    infos_api = GetInfoAPI()
    print('Get infos api...')
    infos_api._get_data()
    infos_api._extract_results()
    print('Get infos api successfully.')

    
    infos_clean = InfosClean(infos_api.results)
    
    uploader = DataFrameUploader(infos_clean.df_proposicao_initial)
    uploader.upload_to_db('Proposicao')

    uploader = DataFrameUploader(infos_clean.df_tramitacao_initial)
    uploader.upload_to_db('Tramitacao')

    print('Creation and upload of all data was successful //////////////')