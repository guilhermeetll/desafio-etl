from controller.run_initial import RunInitial
from controller.get_info_api import GetInfoAPI
from controller.infos_clean import InfosClean
from controller.data_frame_uploader import DataFrameUploader


if __name__ == '__main__':

    initial_create = RunInitial()

    infos_api = GetInfoAPI()
    print('Get infos api...')
    infos_api._get_data()
    infos_api._extract_results()
    print('Get infos api successfully.')

    
    infos_clean = InfosClean(infos_api.results)
    uploader = DataFrameUploader(infos_clean.df_proposicao_initial)
    uploader.upload_to_db('Proposicao')
    
