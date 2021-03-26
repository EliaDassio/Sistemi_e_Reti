import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import csv

month_n = []
temp_m = []
d_with_jaket = []
d_of_school = []
d_of_vg = []

data_file = open("./data.csv")
data_reader = csv.reader(data_file, delimiter = ',')

for row in data_reader:
    month_n.append(float(row[0]))
    temp_m.append(float(row[1]))
    d_with_jaket.append(float(row[2]))
    d_of_school.append(float(row[3]))
    d_of_vg.append(float(row[4]))

fig, (ax1,ax2,ax3,ax4) = plt.subplots(4,1)
fig.suptitle('Medie delle Temperature di cuneo e numero di giorni: in cui metto la giacca, di scuola e in cui gioco ai videogiochi in relazione ad ogni mese')

ax1.plot(month_n, temp_m, '0-g')
ax1.set_xlabel('Mese')
ax1.set_ylabel('temperature')

ax2.plot(month_n, d_with_jaket, '0-b')
ax2.set_xlabel('Mese')
ax2.set_ylabel('giorni in cui metto la giacca')

ax3.plot(month_n, d_of_school, '0-k')
ax3.set_xlabel('Mese')
ax3.set_ylabel('Giorni di scuola')

ax4.plot(month_n, d_of_vg, '0-g')
ax4.set_xlabel('Mese')
ax4.set_ylabel('Giorni in cui gioco hai videogiochi')

plt.show()