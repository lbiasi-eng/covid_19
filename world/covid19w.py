import world.covid19w_data_reader as ds
import matplotlib.pyplot as plt
import globals

file = globals.file_world
data_italy = ds.DataReader(file, "Italy").get_data()
data_us = ds.DataReader(file, "US").get_data()
data_china = ds.DataReader(file, "China").get_data()


plt.figure(3)
ax = plt.gca()

data_italy.plot(kind='line',x='data_normalized',y='Confirmed',label='Italy', ax=ax)
data_us.plot(kind='line',x='data_normalized',y='Confirmed',label='US',ax=ax)
data_china.plot(kind='line',x='data_normalized',y='Confirmed',label='China',ax=ax)
plt.ylabel('Total cases')
plt.xlabel('days')
plt.show()


