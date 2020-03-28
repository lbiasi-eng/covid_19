from covid19_data_reader import DataReader
import matplotlib.pyplot as plt
from covid19_logistic import CovidLogistic
from covid19_gompertz import CovidGompertz
import pandas as pd
import covid19_test_data as test

#regione = "Puglia"
regione = None
data = DataReader(regione)
if regione == None:
        regione = "Italia"
pos = data.get_positives()
deaths = data.get_deaths()

#Logistic regression
model = CovidLogistic()
xdata, popt = model.fit(pos['data'], pos['totale_attualmente_positivi'])

xdata_new = pd.concat( [xdata.copy(deep=True), test.get_xdata_test()])

y = model.logistic_model(xdata_new, *popt)

#Gompertz
model2 = CovidGompertz()
xdata, popt2 = model2.fit(pos['data'], pos['totale_attualmente_positivi'])

y_gompertz = model2.gompertz_model(xdata_new, *popt2)


plt.figure(1)
ax = plt.gca()
ax.plot(xdata_new, y, 'y-', label='Logistic')
ax.plot(xdata_new, y_gompertz, 'r-', label='Gompertz')
ax.plot(xdata,pos['totale_attualmente_positivi'], 'bo')
plt.text(.5,.9,regione,horizontalalignment='center',transform=ax.transAxes)
plt.text(.9,.5,"logistic sat: %d" % y.max(),horizontalalignment='center',transform=ax.transAxes)
plt.text(.9,.9,"gompertz sat: %d" % y_gompertz.max(),horizontalalignment='center',transform=ax.transAxes)

plt.xlabel('days since 01-01-2020')
plt.ylabel('Number of current positives')


plt.figure(3)
ax = plt.gca()
pos.plot(kind='line',x='data_normalized',y='totale_attualmente_positivi',ax=ax)
deaths.plot(kind='line',x='data_normalized',y='deceduti', color='red', ax=ax)
ax.text(.5,.9,regione,horizontalalignment='center',transform=ax.transAxes)
ax.text(.5,.8,"pos: %d" %pos['totale_attualmente_positivi'].iloc[-1],horizontalalignment='center',transform=ax.transAxes)
ax.text(.5,.7,"deaths: %d" % deaths['deceduti'].iloc[-1] ,horizontalalignment='center',transform=ax.transAxes)
plt.show()