Subsistema de potencia eléctrica
================================

Selección de motores
--------------------
.. toctree::
    motor

Selección de controladores de motor
-----------------------------------
Para la implementación de los motores DC seleccionados es necesario incluir un controlador de motor o Driver con el fin de modificar la señal de control adaptándola para que esta esté en la capacidad de inducir movimiento en el motor. 

Para dicha selección se tuvieron en cuenta cinco parámetros principales enumerados a continuación : 
* **Tensión o Voltaje de operación [V]:** Se seleccionan drivers cuyo voltaje de alimentación sea superior al voltaje del motor. Por generalidad, se opta por tensiones de alimentación esté entre 1,5 y 2 veces el voltaje del motor.
* **Corriente Promedio [A]:**  Parámetro relacionado con la corriente consumida por el controlador. Como criterio de selección para este parámetro ,se definió que su valor mínimo  debe ser la corriente asociada al torque máximo que puede entregar el motor (stall current).
* **Tensión de la señal de control [V]:** Valor de voltaje para la señal de salida del driver. 
* **Frecuencia de PWM [kHz]:** Frecuencia de los pulsos de la señal de control. 
* **Reversibilidad:** Se evalúa la capacidad del controlador de invertir el sentido de giro para el motor seleccionado.

Matriz de decisión para la selección de driver
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+------------------+----------------------+--------------------+--------------------------------+-------------------+----------------+
|                  | Tensión de operación | Corriente promedio | Tensión de la señal de control | Frecuencia de PWM | Reversibilidad |
+==================+======================+====================+================================+===================+================+
| RioRand Upgraded |                      |                    |                                |                   |                |
| DC Motor Pump    | 6-90 V               |  8-15 A            | 0-5 V                          | 15 kHz            | No             |
| Speed Controller |                      |                    |                                |                   |                |
| 6-90 V 15A       |                      |                    |                                |                   |                |
+------------------+----------------------+--------------------+--------------------------------+-------------------+----------------+
| RioRand 8-50V DC |                      |                    |                                |                   |                |
| Motor Speed      | 8-50 V               | 20-30 V            | 0-5 V                          | 12 kHz            | No             |
| Controller       |                      |                    |                                |                   |                |
| for Power Wheel  |                      |                    |                                |                   |                |
| PWM Switch       |                      |                    |                                |                   |                |
+------------------+----------------------+--------------------+--------------------------------+-------------------+----------------+
| RioRand 6V 12V   |                      |                    |                                |                   |                |
| 24V 28V 3A 80W   | 6-28 V               | 3A                 | 0-5 V                          | 10 kHz            | Si             |
| DC Motor Speed   |                      |                    |                                |                   |                |
| Controller       |                      |                    |                                |                   |                |
+------------------+----------------------+--------------------+--------------------------------+-------------------+----------------+
| Pololu Dual      |                      |                    |                                |                   |                |
| MAX14870 Motor   | 4,5 - 36 V           | 1,7 A              | 0-5V                           | 50 kHz            | Si             |
| Driver Shield    |                      |                    |                                |                   |                |
| for Arduino      |                      |                    |                                |                   |                |
+------------------+----------------------+--------------------+--------------------------------+-------------------+----------------+


Selección de batería
--------------------
Para la selección de la batería se establecieron los siguientes parámetros a tener en cuenta:

* **Voltaje de la batería [V]:** parámetro dependiente del tipo de motor seleccionado.
* **Capacidad de almacenamiento [mAh]:** 
* **Corriente entregada [mA]:** Parámetro relacionado con la capacidad de descarga [C] de la batería. 
* **Costo estimado [$]:** una estimación inicial de  300 mil pesos
* **Tamaño [mxmxm]:** Dependiente del tamaño de chasis 
* **Peso:** Búsqueda de reducción de peso
* **Densidad energética [Wh/kg]:**
* **Disponibilidad:** Facilidad de encontrar la batería en el comercio local.

Se realizó una búsqueda de los tipos de baterías existentes haciendo énfasis en encontrar las baterías que se utilizan en aplicaciones adyacentes, es decir baterías para vehículos eléctricos  como por ejemplo baterías usadas en bicicletas eléctricas.  Se obtuvieron como resultado  los siguientes tipos Plomo, Gel, Li-Ion, LiFePo4, LiPo, Ni-Mh, Ni-Cd. Sobre los cuales se descartaron las de Ni-Mh, Ni-Cd y gel debido a no cumplir la restricción de disponibilidad y no haber elementos asequibles en el mercado local.
Sobre las restantes se realizó una evaluación calificando su idoneidad en una una escala de 1 a 5 respecto a los parámetros de selección restante. 


+------------------+---------------------+------------------------+--------------------------+---------------------+
|                  | Plomo               | Li-Ion                 | LiFePo4                  | LiPo                |
+==================+=====================+========================+==========================+=====================+
| Voltaje          | 3                   | 5                      | 5                        | 4                   |
| de la batería    |                     |                        |                          |                     |
+------------------+---------------------+------------------------+--------------------------+---------------------+
| Debe tener un    | Batería a 12 voltios| El paquete modular     | Versión de batería a 12, | Versión a 21.5 o    |
| voltaje de hasta | Necesidad de comprar| permite establecer     | 24 y 48 V                | 25.7 V              |
| 24 V.            | 2 baterías para     | el voltaje por número  |                          |                     |
|                  | cumplir requisito.  | de baterías en serie   |                          |                     |
+------------------+---------------------+------------------------+--------------------------+---------------------+
| Capacidad de     | 5                   | 4                      | 4                        | 3                   |
| almacenamiento   |                     |                        |                          |                     |
+------------------+---------------------+------------------------+--------------------------+---------------------+
| Define la        | 7.5 Ah              | 7.8 Ah batería 6S3P    |                          |                     |
| autonomía del    |                     |                        |                          |                     |
| robot            |                     |                        |                          |                     |
+------------------+---------------------+------------------------+--------------------------+---------------------+
| Corriente        | 2                   | 4                      | 3                        | 3                   |
| entregada        |                     |                        |                          |                     |
+------------------+---------------------+------------------------+--------------------------+---------------------+
| Costo            | 3                   | 4                      | 3                        | 3                   |
+------------------+---------------------+------------------------+--------------------------+---------------------+
| Tamaño           | 2                   | 4                      | 2                        | 4                   |
+------------------+---------------------+------------------------+--------------------------+---------------------+
| Peso             | 2                   | 4                      | 2                        | 3                   |
+------------------+---------------------+------------------------+--------------------------+---------------------+
| Densidad         | 3                   | 3                      | 3                        | 5                   |
| energética       |                     |                        |                          |                     |
+------------------+---------------------+------------------------+--------------------------+---------------------+
| **Acumulado**    | **12**              | **28**                 | **23**                   | **26**              |
+------------------+---------------------+------------------------+--------------------------+---------------------+

Donde a partir de la evaluación se decidió escoger una batería ion litio de configuración 6S3P 
