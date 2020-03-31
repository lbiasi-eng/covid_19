from italy.covid19_data_reader import DataReader
import matplotlib.pyplot as plt

regione = "Lombardia"
#regione = None
file = globals.file_region
if regione is None:
        regione = "Italia"
        file = globals.file_italy
data = DataReader(file, regione)
all_data = data.get_data()

plt.figure(3)
ax = plt.gca()
all_data.plot(kind='line',x='data_normalized',y='totale_positivi',ax=ax)

#all_data.plot(kind='line',x='data_normalized',y='totale_casi',ax=ax)
# all_data.plot(kind='line',x='data_normalized',y='totale_ospedalizzati',ax=ax)
# all_data.plot(kind='line',x='data_normalized',y='terapia_intensiva',ax=ax)
# all_data.plot(kind='line',x='data_normalized',y='isolamento_domiciliare',ax=ax)
# all_data.plot(kind='line',x='data_normalized',y='tamponi',ax=ax)
#all_data.plot(kind='line',x='data_normalized',y='dimessi_guariti',ax=ax)


ax.text(.5,.9,regione,horizontalalignment='center',transform=ax.transAxes)
plt.show()