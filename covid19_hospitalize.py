from covid19_data_reader import DataReader
import matplotlib.pyplot as plt
from covid19_logistic import CovidLogistic
from covid19_gompertz import CovidGompertz
from datetime import datetime
import pandas as pd
import covid19_test_data as test


regione = "Lombardia"
#regione = None
data = DataReader(regione)
if regione == None:
        regione = "Italia"
all_data = data.get_data()

plt.figure(3)
ax = plt.gca()
all_data.plot(kind='line',x='data_normalized',y='nuovi_attualmente_positivi',ax=ax)

#all_data.plot(kind='line',x='data_normalized',y='totale_casi',ax=ax)
# all_data.plot(kind='line',x='data_normalized',y='totale_ospedalizzati',ax=ax)
# all_data.plot(kind='line',x='data_normalized',y='terapia_intensiva',ax=ax)
# all_data.plot(kind='line',x='data_normalized',y='isolamento_domiciliare',ax=ax)
# all_data.plot(kind='line',x='data_normalized',y='tamponi',ax=ax)
#all_data.plot(kind='line',x='data_normalized',y='dimessi_guariti',ax=ax)


ax.text(.5,.9,regione,horizontalalignment='center',transform=ax.transAxes)
plt.show()