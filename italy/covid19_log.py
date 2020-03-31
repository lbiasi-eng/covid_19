from italy.covid19_data_reader import DataReader
import matplotlib.pyplot as plt

regione = None
file = globals.file_region
if regione is None:
        regione = "Italia"
        file = globals.file_italy
data = DataReader(file, regione)
all_data = data.get_data()

#new_confirmed = np.log10(all_data['totale_attualmente_positivi'])
#total_cases = np.log10(all_data['totale_casi'])

#new_confirmed = all_data['totale_attualmente_positivi']
new_confirmed = all_data['totale_positivi']
total_cases = all_data['totale_casi']



plt.figure(1)
ax = plt.gca()
ax.plot(total_cases, new_confirmed)
#ax.xlabel('total cases')
#ax.ylabel('new confirmed')
ax.text(.5,.9,regione,horizontalalignment='center',transform=ax.transAxes)
plt.xscale("log")
plt.yscale("log")
plt.grid()

plt.figure(2)
ax = plt.gca()
ax.plot(total_cases, new_confirmed)
#ax.xlabel('total cases')
#ax.ylabel('new confirmed')
ax.text(.5,.9,regione,horizontalalignment='center',transform=ax.transAxes)
plt.grid()

plt.show()