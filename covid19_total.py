from covid19_data_reader import DataReader
import matplotlib.pyplot as plt
from covid19_logistic import CovidLogistic
from covid19_gompertz import CovidGompertz
from datetime import datetime
import pandas as pd
import covid19_test_data as test


#regione = "Lombardia"
regione = None
data = DataReader(regione)
if regione == None:
        regione = "Italia"
pos = data.get_positives()
deaths = data.get_deaths()
total = data.get_total()

#Logistic regression
model = CovidLogistic()
xdata, popt = model.fit(total['data'], total['totale_casi'])

xdata_new = pd.concat( [xdata.copy(deep=True), test.get_xdata_test()])

#logistic
y = model.logistic_model(xdata_new, *popt)

plt.figure(1)
ax = plt.gca()
plt.plot(xdata_new, y, 'y-', label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))
plt.plot(xdata,total['totale_casi'], 'bo')
plt.text(.5,.9,regione,horizontalalignment='center',transform=ax.transAxes)
plt.text(.9,.9,"sat: %d" % y.max(),horizontalalignment='center',transform=ax.transAxes)
plt.xlabel('days since 01-01-2020')
plt.ylabel('Number of total cases')


plt.figure(3)
ax = plt.gca()
pos.plot(kind='line',x='data_normalized',y='totale_attualmente_positivi',ax=ax)
deaths.plot(kind='line',x='data_normalized',y='deceduti', color='red', ax=ax)
ax.text(.5,.9,regione,horizontalalignment='center',transform=ax.transAxes)
ax.text(.5,.8,"pos: %d" %pos['totale_attualmente_positivi'].iloc[-1],horizontalalignment='center',transform=ax.transAxes)
ax.text(.5,.7,"deaths: %d" % deaths['deceduti'].iloc[-1] ,horizontalalignment='center',transform=ax.transAxes)
plt.show()