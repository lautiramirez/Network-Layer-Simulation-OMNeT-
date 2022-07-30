import matplotlib.pyplot as plt
import numpy as np
import pandas
import io
import requests

# Cargo base
data = pandas.read_csv('caso2_arrivaltime_7.csv')
print(data)
print(data.columns)

# Cargo valores
time_node_0 = data['vectime'].loc[[25]].tolist()
buffer_node_0 = data['vecvalue'].loc[[25]].tolist()

time_node_1 = data['vectime'].loc[[29]].tolist()
buffer_node_1 = data['vecvalue'].loc[[29]].tolist()

time_node_2 = data['vectime'].loc[[28]].tolist()
buffer_node_2 = data['vecvalue'].loc[[28]].tolist()

time_node_3 = data['vectime'].loc[[27]].tolist()
buffer_node_3 = data['vecvalue'].loc[[27]].tolist()

time_node_4 = data['vectime'].loc[[26]].tolist()
buffer_node_4 = data['vecvalue'].loc[[26]].tolist()

time_node_6 = data['vectime'].loc[[22]].tolist()
buffer_node_6 = data['vecvalue'].loc[[22]].tolist()

time_node_7 = data['vectime'].loc[[21]].tolist()
buffer_node_7 = data['vecvalue'].loc[[21]].tolist()

time_saltos = data['vectime'].loc[[23]].tolist()
buffer_saltos = data['vecvalue'].loc[[23]].tolist()

time_node_5_app = data['vectime'].loc[[24]].tolist()
buffer_node_5_app = data['vecvalue'].loc[[24]].tolist()

# Los valores que sacamos estan como un solostring separados por comas por lo que tengo que convertirlos a listas para poder graficarlos
time_node_0 = list(map(float, time_node_0[0].split()))
time_node_1 = list(map(float, time_node_1[0].split()))
time_node_2 = list(map(float, time_node_2[0].split()))
time_node_3 = list(map(float, time_node_3[0].split()))
time_node_4 = list(map(float, time_node_4[0].split()))
time_node_6 = list(map(float, time_node_6[0].split()))
time_node_7 = list(map(float, time_node_7[0].split()))
time_saltos = list(map(float, time_saltos[0].split()))
time_node_5_app = list(map(float, time_node_5_app[0].split()))

buffer_node_0 = list(map(float, buffer_node_0[0].split()))
buffer_node_1 = list(map(float, buffer_node_1[0].split()))
buffer_node_2 = list(map(float, buffer_node_2[0].split()))
buffer_node_3 = list(map(float, buffer_node_3[0].split()))
buffer_node_4 = list(map(float, buffer_node_4[0].split()))
buffer_node_7 = list(map(float, buffer_node_7[0].split()))
buffer_node_6 = list(map(float, buffer_node_6[0].split()))
buffer_saltos = list(map(float, buffer_saltos[0].split()))
buffer_node_5_app = list(map(float, buffer_node_5_app[0].split()))

# Graficando
# Dibuja el sistema de coordenadas (subgrafo) de la fila 0 y la columna 1, ir significa círculo verde, punto verde

ax1 = plt.subplot(212)
plt.suptitle("Caso 2: InterArrivalTime = 7", fontsize=20)
ax1.plot(time_node_0, buffer_node_0, linewidth=1.0, linestyle="-", color='gray')
ax1.set_title('Node[0]')
ax1.grid()

ax2 = plt.subplot(221)
ax2.plot(time_node_1, buffer_node_1, linewidth=1.0, linestyle="-", color='blue')
ax2.set_title('Node[1]')
ax2.grid()

ax3 = plt.subplot(222)
ax3.plot(time_node_2, buffer_node_2, linewidth=1.0, linestyle="-", color='green')
ax3.set_title('Node[2]')
ax3.grid()

ax1.set_xlabel('Tiempo de simulacion en segundos', fontsize=15)
ax1.set_ylabel('Cantidad de paquetes en el buffer')
ax2.set_ylabel('Cantidad de paquetes en el buffer')
plt.show()

##
ax1 = plt.subplot(212)
plt.suptitle("Caso 2: InterArrivalTime = 7", fontsize=20)
ax1.plot(time_node_3, buffer_node_3, linewidth=1.0, linestyle="-", color='gray')
ax1.set_title('Node[3]')
plt.grid()

ax2 = plt.subplot(221)
ax2.plot(time_node_4, buffer_node_4, linewidth=1.0, linestyle="-", color='blue')
ax2.set_title('Node[4]')
ax2.grid()

ax3 = plt.subplot(222)
ax3.plot(time_node_6, buffer_node_6, linewidth=1.0, linestyle="-", color='green')
ax3.set_title('Node[6]')
ax3.grid()

ax1.set_xlabel('Tiempo de simulacion en segundos', fontsize=15)
ax1.set_ylabel('Cantidad de paquetes en el buffer')
ax2.set_ylabel('Cantidad de paquetes en el buffer')
plt.show()

### Algunos calculos
#Delay
delay_avg = np.average(buffer_node_5_app)
max_delay = max(buffer_node_5_app)
xpos = buffer_node_5_app.index(max_delay)
xmax = time_node_5_app[xpos]

#Saltos
total = len(buffer_saltos)
saltos_averg = np.average(buffer_saltos)

ax1 = plt.subplot(212)
plt.suptitle("Caso 2: InterArrivalTime = 7", fontsize=20)
ax1.plot(time_node_7, buffer_node_7, linewidth=1.0,
         linestyle="-", color='gray')
ax1.set_title('Node[7]')
plt.grid()

ax2 = plt.subplot(221)
ax2.plot(time_node_5_app, buffer_node_5_app, linewidth=1.0,
         linestyle="-", color='blue')
ax2.plot(xmax, max_delay, 'o', color='red',
         label=f"Max:{round(xmax, 2), round(max_delay, 2)}")
ax2.hlines(delay_avg, 0, 200, linestyles='--', color='red',
           label=f"Promedio: {round(float(delay_avg), 2)}s")
ax2.set_title('Delay Node[5]')
ax2.set_ylabel('Delay en segundos')
ax2.legend()
plt.grid()

ax3 = plt.subplot(222)
ax3.plot(time_saltos, buffer_saltos, linewidth=1.0,
         linestyle="-", color='green')
ax3.plot(time_saltos, buffer_saltos, linewidth=1.0, linestyle="-",
         color='blue', label=f"Saltos ({total})")
ax3.hlines(saltos_averg, 0, 200, linestyles='--', color='red',
           label=f"Promedio: {round(float(saltos_averg), 2)}s")
ax3.set_title('Saltos Node[5]')
ax3.set_ylabel('Saltos')
ax3.legend()
ax3.grid()

ax1.set_xlabel('Tiempo de simulacion en segundos', fontsize=15)
ax1.set_ylabel('Cantidad de paquetes en el buffer')
plt.show()
