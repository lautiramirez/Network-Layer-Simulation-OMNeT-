import matplotlib.pyplot as plt
import numpy as np
import pandas
import io
import requests

# Cargo base
data = pandas.read_csv('caso2_arrivaltime_5.csv')
print(data)
print(data.columns)

## Cargo valores
time_node_0_lnk0 = data['vectime'].loc[[35]].tolist()
buffer_node_0_lnk0 = data['vecvalue'].loc[[35]].tolist()

time_node_0_lnk1 = data['vectime'].loc[[24]].tolist()
buffer_node_0_lnk1 = data['vecvalue'].loc[[24]].tolist()

time_node_1_lnk0 = data['vectime'].loc[[33]].tolist()
buffer_node_1_lnk0 = data['vecvalue'].loc[[33]].tolist()

time_node_1_lnk1 = data['vectime'].loc[[27]].tolist()
buffer_node_1_lnk1 = data['vecvalue'].loc[[27]].tolist()

time_node_2_lnk0 = data['vectime'].loc[[34]].tolist()
buffer_node_2_lnk0 = data['vecvalue'].loc[[34]].tolist()

time_node_2_lnk1 = data['vectime'].loc[[28]].tolist()
buffer_node_2_lnk1 = data['vecvalue'].loc[[28]].tolist()

time_node_3_lnk0 = data['vectime'].loc[[32]].tolist()
buffer_node_3_lnk0 = data['vecvalue'].loc[[32]].tolist()

time_node_3_lnk1 = data['vectime'].loc[[30]].tolist()
buffer_node_3_lnk1 = data['vecvalue'].loc[[30]].tolist()

time_node_4_lnk0 = data['vectime'].loc[[31]].tolist()
buffer_node_4_lnk0 = data['vecvalue'].loc[[31]].tolist()

time_node_4_lnk1 = data['vectime'].loc[[29]].tolist()
buffer_node_4_lnk1 = data['vecvalue'].loc[[29]].tolist()

time_node_6_lnk0 = data['vectime'].loc[[22]].tolist()
buffer_node_6_lnk0 = data['vecvalue'].loc[[22]].tolist()

time_node_6_lnk1 = data['vectime'].loc[[23]].tolist()
buffer_node_6_lnk1 = data['vecvalue'].loc[[23]].tolist()

time_node_7_lnk0 = data['vectime'].loc[[36]].tolist()
buffer_node_7_lnk0 = data['vecvalue'].loc[[36]].tolist()

time_node_7_lnk1 = data['vectime'].loc[[21]].tolist()
buffer_node_7_lnk1 = data['vecvalue'].loc[[21]].tolist()

time_saltos = data['vectime'].loc[[25]].tolist()
buffer_saltos = data['vecvalue'].loc[[25]].tolist()

time_node_5_app = data['vectime'].loc[[26]].tolist()
buffer_node_5_app = data['vecvalue'].loc[[26]].tolist()

# # Los valores que sacamos estan como un solostring separados por comas por lo que tengo que convertirlos a listas para poder graficarlos
time_node_0_lnk0 = list(map(float, time_node_0_lnk0[0].split()))
time_node_0_lnk1 = list(map(float, time_node_0_lnk1[0].split()))
time_node_1_lnk0 = list(map(float, time_node_1_lnk0[0].split()))
time_node_1_lnk1 = list(map(float, time_node_1_lnk1[0].split()))
time_node_2_lnk0 = list(map(float, time_node_2_lnk0[0].split()))
time_node_2_lnk1 = list(map(float, time_node_2_lnk1[0].split()))
time_node_3_lnk0 = list(map(float, time_node_3_lnk0[0].split()))
time_node_3_lnk1 = list(map(float, time_node_3_lnk1[0].split()))
time_node_4_lnk0 = list(map(float, time_node_4_lnk0[0].split()))
time_node_4_lnk1 = list(map(float, time_node_4_lnk1[0].split()))
time_node_6_lnk0 = list(map(float, time_node_6_lnk0[0].split()))
time_node_6_lnk1 = list(map(float, time_node_6_lnk1[0].split()))
time_node_7_lnk0 = list(map(float, time_node_7_lnk0[0].split()))
time_node_7_lnk1 = list(map(float, time_node_7_lnk1[0].split()))
time_saltos = list(map(float, time_saltos[0].split()))
time_node_5_app = list(map(float, time_node_5_app[0].split()))

buffer_node_0_lnk0 = list(map(float, buffer_node_0_lnk0[0].split()))
buffer_node_0_lnk1 = list(map(float, buffer_node_0_lnk1[0].split()))
buffer_node_1_lnk0 = list(map(float, buffer_node_1_lnk0[0].split()))
buffer_node_1_lnk1 = list(map(float, buffer_node_1_lnk1[0].split()))
buffer_node_2_lnk0 = list(map(float, buffer_node_2_lnk0[0].split()))
buffer_node_2_lnk1 = list(map(float, buffer_node_2_lnk1[0].split()))
buffer_node_3_lnk0 = list(map(float, buffer_node_3_lnk0[0].split()))
buffer_node_3_lnk1 = list(map(float, buffer_node_3_lnk1[0].split()))
buffer_node_4_lnk0 = list(map(float, buffer_node_4_lnk0[0].split()))
buffer_node_4_lnk1 = list(map(float, buffer_node_4_lnk1[0].split()))
buffer_node_6_lnk0 = list(map(float, buffer_node_6_lnk0[0].split()))
buffer_node_6_lnk1 = list(map(float, buffer_node_6_lnk1[0].split()))
buffer_node_7_lnk0 = list(map(float, buffer_node_7_lnk0[0].split()))
buffer_node_7_lnk1 = list(map(float, buffer_node_7_lnk1[0].split()))
buffer_saltos = list(map(float, buffer_saltos[0].split()))
buffer_node_5_app = list(map(float, buffer_node_5_app[0].split()))


# # Graficando

# # Node0
# max_node0_lnk0 = max(buffer_node_0_lnk0)
# xpos_node0_lnk0 = buffer_node_0_lnk0.index(max_node0_lnk0)
# xmax_node0_lnk0 = time_node_0_lnk0[xpos_node0_lnk0]

# max_node0_lnk1 = max(buffer_node_0_lnk1)
# xpos_node0_lnk1 = buffer_node_0_lnk1.index(max_node0_lnk1)
# xmax_node0_lnk1 = time_node_0_lnk1[xpos_node0_lnk1]

# # Node1
# max_node1_lnk0 = max(buffer_node_1_lnk0)
# xpos_node1_lnk0 = buffer_node_1_lnk0.index(max_node1_lnk0)
# xmax_node1_lnk0 = time_node_1_lnk0[xpos_node1_lnk0]

# max_node1_lnk1 = max(buffer_node_1_lnk1)
# xpos_node1_lnk1 = buffer_node_1_lnk1.index(max_node1_lnk1)
# xmax_node1_lnk1 = time_node_1_lnk1[xpos_node1_lnk1]

# # Node2
# max_node2_lnk0 = max(buffer_node_2_lnk0)
# xpos_lnk0 = buffer_node_2_lnk0.index(max_node2_lnk0)
# xmax_lnk0 = time_node_2_lnk0[xpos_lnk0]

# max_node2_lnk1 = max(buffer_node_2_lnk1)
# xpos_lnk1 = buffer_node_2_lnk1.index(max_node2_lnk1)
# xmax_lnk1 = time_node_2_lnk1[xpos_lnk1]

#####
ax1 = plt.subplot(212)
plt.suptitle("Caso 2: InterArrivalTime = 5", fontsize=20)
ax1.plot(time_node_0_lnk0, buffer_node_0_lnk0, linewidth=1.0,
         linestyle="-", color='gray', label='node[0].lnk0')
ax1.plot(time_node_0_lnk1, buffer_node_0_lnk1, linewidth=1.0,
         linestyle="-", color='black', label='node[0].lnk1')
# ax1.plot(xmax_node0_lnk0, max_node0_lnk0, 'o', color='red',
#          label=f"Max:{round(xmax_node0_lnk0, 2), round(max_node0_lnk0, 2)}")
# ax1.plot(xmax_node0_lnk1, max_node0_lnk1, 'o', color='red',
#          label=f"Max:{round(xmax_node0_lnk1, 2), round(max_node0_lnk1, 2)}")
ax1.set_title('Node[0]')
ax1.legend()
ax1.grid()

ax2 = plt.subplot(221)
ax2.plot(time_node_1_lnk0, buffer_node_1_lnk0, linewidth=1.0,
         linestyle="-", color='blue', label='node[1].lnk0')
ax2.plot(time_node_1_lnk1, buffer_node_1_lnk1, linewidth=1.0,
         linestyle="-", color='black', label='node[1].lnk1')
ax2.set_title('Node[1]')
ax2.legend()
ax2.grid()

ax3 = plt.subplot(222)
ax3.plot(time_node_2_lnk0, buffer_node_2_lnk0, linewidth=1.0,
         linestyle="-", color='green', label='node[2].lnk0')
ax3.plot(time_node_2_lnk1, buffer_node_2_lnk1, linewidth=1.0,
         linestyle="-", color='black', label='node[2].lnk1')
# ax3.plot(xmax_lnk0, max_node2_lnk0, 'o', color='red',
#          label=f"Max:{round(xmax_lnk0, 2), round(max_node2_lnk0, 2)}")
# ax3.plot(xmax_lnk1, max_node2_lnk1, 'o', color='red',
#          label=f"Max:{round(xmax_lnk1, 2), round(max_node2_lnk1, 2)}")
ax3.set_title('Node[2]')
ax3.legend()
ax3.grid()

ax1.set_xlabel('Tiempo de simulacion en segundos', fontsize=20)
ax1.set_ylabel('Cantidad de paquetes en el buffer')
ax2.set_ylabel('Cantidad de paquetes en el buffer')

plt.show()

###
ax1 = plt.subplot(212)
plt.suptitle("Caso 2: InterArrivalTime = 5", fontsize=20)
ax1.plot(time_node_3_lnk0, buffer_node_3_lnk0, linewidth=1.0,
         linestyle="-", color='gray', label='node[3].lnk0')
ax1.plot(time_node_3_lnk1, buffer_node_3_lnk1, linewidth=1.0,
         linestyle="-", color='black', label='node[3].lnk1')
ax1.set_title('Node[3]')
ax1.legend()
ax1.grid()

ax2 = plt.subplot(221)
ax2.plot(time_node_4_lnk0, buffer_node_4_lnk0, linewidth=1.0,
         linestyle="-", color='blue', label='node[4].lnk0')
ax2.plot(time_node_4_lnk1, buffer_node_4_lnk1, linewidth=1.0,
         linestyle="-", color='black', label='node[4].lnk1')
ax2.set_title('Node[4]')
ax2.legend()
ax2.grid()

ax3 = plt.subplot(222)
ax3.plot(time_node_6_lnk0, buffer_node_6_lnk0, linewidth=1.0,
         linestyle="-", color='green', label='node[6].lnk0')
ax3.plot(time_node_6_lnk1, buffer_node_6_lnk1, linewidth=1.0,
         linestyle="-", color='black', label='node[6].lnk1')
ax3.set_title('Node[6]')
ax3.legend()
ax3.grid()

ax1.set_xlabel('Tiempo de simulacion en segundos', fontsize=20)
ax1.set_ylabel('Cantidad de paquetes en el buffer')
ax2.set_ylabel('Cantidad de paquetes en el buffer')

plt.show()

#####
# Delay
delay_avg = np.average(buffer_node_5_app)
max_delay = max(buffer_node_5_app)
xpos = buffer_node_5_app.index(max_delay)
xmax = time_node_5_app[xpos]
ax1 = plt.subplot(212)

# Saltos
total = len(buffer_saltos)
saltos_averg = np.average(buffer_saltos)

plt.suptitle("Caso 2: InterArrivalTime = 5", fontsize=20)
ax1.plot(time_node_5_app, buffer_node_5_app,
         linewidth=1.0, linestyle="-", color='gray')
ax1.plot(xmax, max_delay, 'o', color='red',
         label=f"Max:{round(xmax, 2), round(max_delay, 2)}")
ax1.hlines(delay_avg, 0, 200, linestyles='--', color='red',
           label=f"Promedio: {round(float(delay_avg), 2)}s")
ax1.set_title('Delay Node[5]')
ax1.legend()
plt.grid()

ax2 = plt.subplot(221)
ax2.plot(time_saltos, buffer_saltos, linewidth=1.0, linestyle="-",
         color='blue', label=f"Saltos ({total})")
ax2.hlines(saltos_averg, 0, 200, linestyles='--', color='red',
           label=f"Promedio: {round(float(saltos_averg), 2)}s")
ax2.set_ylabel('Saltos')
ax2.set_title('Saltos node[5]')
ax2.legend()
plt.grid()

ax3 = plt.subplot(222)
ax3.plot(time_node_7_lnk0, buffer_node_7_lnk0,
         linewidth=1.0, linestyle="-", color='green', label='node[7].lnk0')
ax3.plot(time_node_7_lnk1, buffer_node_7_lnk1,
         linewidth=1.0, linestyle="-", color='black', label='node[7].lnk1')
ax3.set_title('Node[7]')
ax3.legend()
ax3.set_ylabel('Cantidad de paquetes en el buffer')

ax1.set_xlabel('Tiempo de simulacion en segundos', fontsize=15)
ax1.set_ylabel('Delay en segundos')
plt.grid()
plt.show()

