import pandas as pd
from os import listdir
from os.path import isfile, join


#data structure:
#data,stato,ricoverati_con_sintomi,terapia_intensiva,totale_ospedalizzati,isolamento_domiciliare,
# totale_attualmente_positivi,nuovi_attualmente_positivi,dimessi_guariti,deceduti,totale_casi,tamponi
class DataReader:

    def __init__(self, regione):
        if regione is None:
            file = "C:\\Users\\LuigiBiasi\\Documents\\CODIV_19_data\\COVID-19\\dati-andamento-nazionale\\dpc-covid19-ita-andamento-nazionale.csv"
            all_data = pd.read_csv(file)
            all_data['data_normalized'] = pd.to_datetime(all_data['data']).dt.normalize()
            self.data = all_data
        else:
            file = "C:\\Users\\LuigiBiasi\\Documents\\CODIV_19_data\\COVID-19\\dati-regioni\\dpc-covid19-ita-regioni.csv"
            self.regione = regione
            all_data = pd.read_csv(file)
            all_data['data_normalized'] = pd.to_datetime(all_data['data']).dt.normalize()
            self.data = all_data[all_data['denominazione_regione'] == regione]

    def get_positives(self):
        return self.data[['data_normalized','data', 'totale_attualmente_positivi']]

    def get_deaths(self):
        return self.data[['data_normalized','data', 'deceduti']]

    def get_recovered(self):
        return self.data[['data_normalized','data','dimessi_guariti']]

    def get_total(self):
        return self.data[['data_normalized', 'data', 'totale_casi']]

    def get_data(self):
        return self.data
