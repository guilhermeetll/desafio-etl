from controller.run_initial import RunInitial
from controller.get_info_api import GetInfoAPI
from controller.infos_clean import InfosClean


if __name__ == '__main__':

    initial_create = RunInitial()

    infos_api = GetInfoAPI()
    print('Get infos api...')
    infos_api._get_data()
    infos_api._extract_results()
    print('Get infos api successfully.')

    
    infos_clean = InfosClean(infos_api.results)
    
