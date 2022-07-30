# Network-Layer-Simulation-OMNeT-
Simulaciones en OMNeT++ sobre la capa de red.

# Laboratorio 4: Capa de red

## Metodología de anillo

Se nos entregó como *kickstarter* un modelo de red en anillo que posee 8 nodos, cada uno con dos interfaces de comunicación *full-duplex* (se puede transmitir información en ambos sentidos al mismo tiempo) con dos posibles vecinos, como se presenta en la siguiente figura.

![f1](lab4-kickstarter/simulaciones/modelo.png)

Internamente, cada nodo cuenta con dos capas de enlace (lnk[0] y lnk[1], una con cada vecino), una capa de red (net) y una capa de aplicación (app). La capa de aplicación y la capa de enlace implementan generadores de tráfico y buffers.

El objetivo de este laboratorio es trabajar el problema de enrutamiento de tráfico en módulos de múltiples entradas y salidas por medio de simulaciones. La capa de red no reviste de mucha inteligencia, cada paquete que está recibe es evaluado para determinar si el nodo local es el destino final del mismo. En caso que lo sea, el paquete es enviado a la capa de aplicación local. En caso que el paquete esté destinado a otro nodo se elige una interfaz para re-transmitirlo. La capa de red siempre elige la interfaz número 0 (toLnK[0]) que es la que envía el tráfico en sentido horario a lo largo del anillo hasta llegar a destino.

## Parte 1

En esta primera parte realizamos un análisis del modelo descrito anteriormente. Implementamos una métrica adicional que nos cuenta la cantidad de saltos por paquete, es decir, que se contabiliza la cantidad de nodos por los que pasó un paquete antes de llegar a destino. Los casos que analizaremos son:

- Caso 1: las fuentes de tráfico configuradas son node[0] y node[2] que transmiten datos a node[5].
- Caso 2: todos los nodos (0,1,2,3,4,6,7,8) generan tráfico hacia el node[5].

### Caso 1

Como se mencionó anteriormente, en este caso el nodo 0 y 2 son los que transmiten hacia el nodo 5. En los siguientes gráfico se presentan los nodos que conforman el modelo. Se puede observar que el buffer del nodo 0 y 2 como son generadores presentan un comportamiento diferente en relación a los otros nodos esto es debido a que reciben datos de su capa de aplicación además de los que ellos mismos generan.

El nodo 0 exhibe un crecimiento constante que es un indicador de congestión, el nodo 2 no tiene un comportamiento muy marcado sino que oscila durante toda la simulación. Ya que los paquetes son enviados en sentido horario con destino a nodo 5, es decir, que los paquetes que genera el nodo 2 pasan por los nodos 1 y 0 antes de llegar a destino, elevan la carga del nodo 0 y es por esto que presenta una mayor congestión (nodo 3 y 4 no se presentan porque no reciben paquetes de los nodos generadores).

![fig_1](lab4-kickstarter/simulaciones/parte1/caso1/Figure_1.png)

Aquí podemos ver que los nodos 6 y 7 presentan un comportamiento constante, siempre con uno paquete en el buffer. Por otro lado, el delay al nodo destino, crece de forma constante llegando a un máximo de 105.56 y un promedio de demora de 51.56 segundos.

![fig_2](lab4-kickstarter/simulaciones/parte1/caso1/Figure_2.png)

Por último exponemos el gráfico de los saltos que realizaron los paquetes desde que salieron de los nodos generadores hasta llegar a destino. Se realizaron en total 196 saltos que varían entre 3 y 5, con un promedio de 3.92 por paquete. Entonces podemos decir que el rendimiento en cuanto a los saltos y el delay no es muy bueno ya que estos resultados presentan una correlación positiva a la congestión que se produce en los nodos 0 y 2.

![fig_3](lab4-kickstarter/simulaciones/parte1/caso1/Figure_3.png)

### Caso 2

Ahora con el objetivo de encontrar la estabilidad de la red corrimos simulaciones para valores de **interArrivalTime** que van desde 0.5 a 8, los casos que más nos llamaron la atención los presentamos a continuación.

#### InterArrivalTime 2

En los siguiente gráficos se presentan todos los nodos de la red, a simple vista podemos decir que tienen una tendrencia creciente, excepto por el nodo 4. Entonces, este *interArrivalTime* detectamos congestión, por ende la red no se encuentra en equilibrio.

![fig_1](lab4-kickstarter/simulaciones/parte1/caso2/Figure_1_arrivaltime_2.png)

![fig_2](lab4-kickstarter/simulaciones/parte1/caso2/Figure_2_arrivaltime_2.png)

Para reforzar lo mencionado en el párrafo anterior, vemos  que el delay al nodo destino es creciente, llegando a un máximo de 170.23 segundos durante toda la simulación con un promedio de 56.9 segundos. Por otra parte los saltos realizados por los paquetes también revelan la ineficiencia que posee este intervalo de generación, debido a que se producen 199 saltos, pero con un promedio de 2.9 cada uno.

![fig_3](lab4-kickstarter/simulaciones/parte1/caso2/Figure_3_arrivaltime_2.png)

#### InterArrivalTime 5

Con un *interArrivalTime* de 5, vemos un comportamiento muy distinto al caso anterior. Los nodos presentados oscilan entre valores relativamente bajos, esto es bueno debido a que nos da indicios de que nuestra red no se congestiona demasiado. El nodo 6 presenta un comportamiento creciente, con más de 30 paquetes en su buffer, cabe resaltar que es aproximadamente la mitad de paquetes que se tenían en el caso anterior, por ende nuestra red está tendiendo al equilibrio

![fig_1](lab4-kickstarter/simulaciones/parte1/caso2/Figure_1_arrivaltime_5.png)

![fig_2](lab4-kickstarter/simulaciones/parte1/caso2/Figure_2_arrivaltime_5.png)

Se observa un delay promedio 29.9 segundos que es mucho más chico, el número de saltos que se producen cae levemente con un promedio de 4.07 por paquete, es decir, que con este *interArrivalTime* los paquetes en promedio realizan más saltos que el caso anterior pero tiene un delay en promedio menor. El nodo 7 presenta una tendencia alcista pero con una cantidad menor de paquetes, mismo comportamiento que el nodo 6. Entonces podemos decir que todavía no encontramos un equilibrio total en el modelo.

![fig_3](lab4-kickstarter/simulaciones/parte1/caso2/Figure_3_arrivaltime_5.png)

#### InterArrivalTime 7

En este último caso vemos que todos los nodos presentan una tendencia oscilatoria entre valores relativamente bajos, como ninguno de ellos presenta una tendencia creciente podemos afirmar que con un *interArrivalTime* de 7 la red está estable.

![fig_1](lab4-kickstarter/simulaciones/parte1/caso2/Figure_1_arrivaltime_7.png)

![fig_2](lab4-kickstarter/simulaciones/parte1/caso2/Figure_2_arrivaltime_7.png)

Para reforzar lo que mencionamos anteriormente, vemos en los siguientes gráficos que el delay promedio es de 9.72 segundos muy por debajo en relación a los casos anteriores y el promedio de saltos en segundos es de 4.18 que es parecido al caso anterior pero aquí el número de saltos es menor. Esto nos dice que aunque los paquetes tardan en promedio lo mismo en llegar pasan por menos nodos intermedios en relación al caso anterior. Entonces podemos concluir que con intervalo de generación de 7, la red presenta estabilidad.

![fig_3](lab4-kickstarter/simulaciones/parte1/caso2/Figure_3_arrivaltime_7.png)

## Parte 2

Para esta sección se pondrá a prueba el algoritmo de enrutamiento que diseñamos para poder mejorar la eficiencia de la red, usaremos los casos 1 y 2 que analizamos en la parte 1. A continuación describimos cómo funciona el algoritmo.

### Diseño

Para mejorar el algoritmo base decidimos que los nodos generadores mandan los paquetes de forma aleatoria, y el nodo que lo recibe lo envía por el otro extremo, es decir, que si se recibe un paquete por lnk[0] se envia por lnk[1] y viceversa. Como la topología de la red es circular, la mitad de los nodos se dirigen al nodo destino por un lado y los demás nodos por otro. Cabe resaltar que el algoritmo solo funciona suponiendo la circularidad de la red, en caso que está cambie no se asegura el funcionamiento.

Por otra parte, el algoritmo es ineficiente en el caso que los paquetes se generan cerca del nodo destino y cómo se envían de forma aleatoria tomen el camino opuesto teniendo que dar toda la vuelta para llegar al nodo final.
### Caso 1

En los siguientes gráficos podemos ver cómo funcionan los nodos con el nuevo algoritmo con un *interArrivalTime* de 1, vemos que los nodos 0, 1 y 2 presentan estabilidad en las ambas direcciones (lnk0 y lnk1). El nodo 1 siempre oscila entre 0 y 1, en el nodo 2 se nota estabilidad en la dirección lnk0 y un fuerte aumento en lnk1 pero con una posterior caída y los paquetes en el buffer son relativamente pocos. A su vez, el nodo 0 en lnk1 es constante, pero el lnk0 presenta cierta irregularidad en algunos tramos de la simulación.

![fig_1](lab4-kickstarter/simulaciones/parte2/caso1/Figure_1.png)

En el caso de los nodos 4, 6 y 3 oscilan durante toda la simulación entre 0 y 1.

![fig_2](lab4-kickstarter/simulaciones/parte2/caso1/Figure_2.png)

Por último, el node 7 también oscila. Lo importante a resaltar es lo que sucede con el nodo destino, se puede observar que tiene un delay promedio de 7.9 segundos por paquete, presenta 368 saltos durante los 200 segundos de la simulación con un tiempo promedio de 3.9 segundos.

Vemos que el número de saltos aumentó de manera considerable en relación al caso 1 de la parte 1, pero el valor en promedio no cambió, además el comportamiento de los nodos en este caso es mucho más estable por lo que nuestra implementación funciona correctamente.

![fig_3](lab4-kickstarter/simulaciones/parte2/caso1/Figure_3.png)
### Caso 2
#### InterArrivalTime 2

Para el caso 2, con un *interArrivalTime* de 2 todos los nodos presentan una tendencia creciente una de sus direcciones, mientras que el la otra dirección la tendencia es constante.

![fig_1](lab4-kickstarter/simulaciones/parte2/caso2/Figure_1_arrivaltime_2.png)

![fig_2](lab4-kickstarter/simulaciones/parte2/caso2/Figure_2_arrivaltime_2.png)

Para el caso de los saltos por paquete hasta llegar a destino oscilan entre 1 y 7. Durante la simulación se realizan 390 saltos, con un promedio de 3.75 segundos, en relación la parte 1 este mismo caso presentaba menos saltos y un promedio más bajo. Lo que nuestro algoritmo mejora de forma considerable es el delay en promedio se reduce a 42.56.

![fig_3](lab4-kickstarter/simulaciones/parte2/caso2/Figure_3_arrivaltime_2.png)
#### InterArrivalTime 5

Ahora con este nuevo *interArrivalTime*, en las siguiente figuras podemos ver que los nodos 0, 1, 2, 3, 4, 6, 7 presentan un comportamiento oscilatorio en ambas direcciones, esto da indicios de que la red se está estabilizando.

![fig_1](lab4-kickstarter/simulaciones/parte2/caso2/Figure_1_arrivaltime_5.png)

![fig_2](lab4-kickstarter/simulaciones/parte2/caso2/Figure_2_arrivaltime_5.png)

El delay en promedio es de 4.25 segundos, se observan un total de 193 saltos con un promedio de 3.83 segundos. Esto es muy bueno, recordemos que en la parte 1 obtuvimos resultado parecidos recién con un *InterArrivalTime* igual a 7, por eso lo escogimos como punto de equilibrio.

![fig_3](lab4-kickstarter/simulaciones/parte2/caso2/Figure_3_arrivaltime_5.png)

#### InterArrivalTime 7

Para este último caso, vemos que todos los nodos presentan estabilidad, es decir, evolucionan de forma constante a lo largo de toda la simulación.

![fig_1](lab4-kickstarter/simulaciones/parte2/caso2/Figure_1_arrivaltime_7.png)

![fig_2](lab4-kickstarter/simulaciones/parte2/caso2/Figure_2_arrivaltime_7.png)

Lo importante a destacar es lo que exponemos en la siguiente figura, donde el delay promedio para llegar al destino final es de 9.72 segundos, esto es mucho más alto que el caso anterior. Por otro lado se presentan un total de 184 saltos con un promedio de 4.18 segundos, aquí el número de saltos es menor pero en promedio superan al caso anterior. Entonces podemos decir que con la implementación de nuestro algoritmo el equilibrio en la red se encuentra con un *interArrivalTime* menor.

![fig_3](lab4-kickstarter/simulaciones/parte1/caso2/Figure_3_arrivaltime_7.png)

## Conclusiones

Durante este trabajo pusimos a prueba una red que presentaba una topología del tipo anillo, para ver como se veia afectada la congestión en cada nodo mientras variamos el valor del *interArrivalTime*. Partimos de un modelo donde los paquetes que se generaban se enviaban en sentido horario y por ende en los casos 1 y 2 los nodos se saturaron, esto se evidenciaba principalmente en el delay y saltos que realizaban los paquetes antes de llegar al nodo destino. 

A modo de prueba descubrimos que la red se estabiliza con un *interArrivalTime* de 7, por ende no había saturación en los buffers del modelo. Luego para poder mejorar esto propusimos un modelo muy simple en el cual los nodos que generan los paquetes los envían aleatoriamente y el nodo que los recibe los envía en la dirección opuesta, esto permite que no se generen loop de enrutamiento.

Para el caso 1 al correr la simulación con nuestro algoritmo se observó una mejora notable, ya que ahora hay un mayor aprovechamiento de los buffes, la congestión se reduce drásticamente. Pero se evidenció un mayor número de saltos. Por otro lado, para el caso 2 encontramos un nuevo valor óptimo en el cual la red se estabiliza, pasó de estar en *interArrivalTime* centrado en 7 a uno centrado en 5, esta es una mejora en cuanto al algoritmo base.

Entonces, podemos concluir que con un algoritmo sencillo se evita la congestión en la red. Pero esta implementación tiene un punto deficiente, como lo es la aleatoriedad a la hora de enviar los paquetes, en caso que el generador se encuentre cerca del nodo destino y se decida enviarlo por el otro extremo, esto sería algo que podríamos mejorar. Además el funcionamiento del algoritmo sólo está garantizado en topoligías del tipo anillo.
## Posibles extensiones

Podemos decir que los resultados del trabajo cumplen con lo previsto, pues nuestro algoritmo logra un equilibrio en la red con un *interArrivalTime* más chico que en la parte 1. Nos hubiera gustado implementar alguno de los algoritmos o protocolos que vimos en teórico para poder analizar su comportamiento en la práctica.

## Integrantes del grupo

* Castellaro, Agustín.
* Mansilla, Kevin Gaston.
* Ramirez, Lautaro.

## Referencias

* Tanembaum, A. S. (2012). Redes De Computadores (5ta ed.). Pearson.
* Varga, A. (2019). OMNeT++ - Simulation Manual. OpenSim Ltd. <https://doc.omnetpp.org/omnetpp/manual/>
