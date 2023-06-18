Planteamiento del problema y especificaciones
#############################################
Marco teórico
=============
Muestreo de suelos
------------------
El muestreo de suelos es la actividad de recolección de muestras representativas de suelo mediante distintas técnicas, con el fin de proporcionar información clave sobre sus propiedades físicas, químicas y biológicas. El muestreo busca determinar la variabilidad espacial y temporal de las propiedades del suelo, útiles para evaluar la calidad del suelo y diagnosticar problemas relacionados. Parte fundamental del proceso consiste en el diseño de experimento, selección del tamaño de la muestra y de los métodos de muestreo; para esto se debe determinar el sensor a utilizar (de acuerdo a la variable que se desea medir), así como seleccionar la unidad de muestreo y el recorrido que puede ser aleatorio o sistemático (comúnmente zigzag o cuadrícula).

Robótica móvil en la agricultura
--------------------------------
Un robot móvil es un sistema robótico capaz de desplazarse en distintos entornos y que cuenta con capacidades que le permiten ejecutar tareas complejas en un espacio amplio, ya sea de forma autónoma o controlado por un operador humano. En la agricultura los robots móviles de uso más común son los vehículos aéreos no tripulados UAV (unmanned aerial vehicle) y los vehículos terrestres no tripulados o UGV (unmanned ground vehicle) que se caracterizan por operar estando en contacto con el suelo; generalmente los primeros son utilizados para labores de monitoreo y supervisión, mientras que los segundos son para tareas de aplicación o interacción directa con los cultivos. La finalidad de la utilización de los robots móviles en la agricultura es automatizar algunos procesos agrícolas para que sean llevados a cabo de manera más eficiente y precisa en comparación con los métodos tradicionales, además de reemplazar la intervención humana en labores que pueden ser perjudiciales para su salud (como el caso de la aplicación de químicos).


Planteamiento del problema
==========================
El Semillero de Investigación de Maquinaria Agrícola SIMA está buscando ofrecer el servicio de muestreo y mapeo de propiedades físicas del suelo de manera teleoperada y que sea asequible a pequeños productores agrícolas. Para esto requieren de un mecanismo capaz de recorrer terreno de suelo desnudo, que sea fácil de transportar, y que cuente con una plataforma donde instalar los distintos sensores requeridos. Para la primera etapa, el semillero limitará la implementación de la solución a parcelas pertenecientes a la sabana de Bogotá (terreno plano).

Objetivos
=========
Objetivo general
----------------
Desarrollar un prototipo de vehículo terrestre no tripulado (UGV) capaz de recorrer un terreno plano sin labrar, siguiendo una trayectoria definida de forma teleoperada y que cuente con una interfaz o plataforma para instalar sensores y dispositivos para medición de propiedades físicas del suelo.

Objetivos específicos
---------------------
* Diseñar y simular el UGV para diferentes configuraciones de carga (sensores).
* Diseñar e implementar un sistema de control que permita al vehículo seguir trayectorias (en lazo abierto).
* Validar el prototipo en un lote perteneciente a la Universidad Nacional de Colombia previamente adecuado.
* Elaborar informe de trabajo y manual de uso.


Estudio preliminar de factibilidad
==================================
.. _art:

Estado del arte
---------------
Empresas internacionales de soluciones tecnológicas en la agricultura como Blue River Technology o Ecorobotix, han desarrollado y comercializan dispositivos inteligentes para aplicaciones en cultivos, sin embargo estos vehículos no son autónomos y se requiere de un tractor para moverlos en el terreno de interés. Otras empresas como Robotnik, se dedican a comercializar robots móviles y manipuladores móviles de propósito general, de manera que pueden ser fácilmente adaptables para tareas agrícolas. Los productos encontrados en el mercado se caracterizan por ser vehículos de gran tamaño enfocados a cultivos de gran extensión, además, la representación de las marcas en Colombia es casi nula lo que complica el servicio técnico.

A nivel investigativo, se han encontrado algunos trabajos universitarios similares como el “Prototipo de robot móvil autónomo para caracterizar suelos de cultivo” desarrollado en el Instituto Politécnico Nacional de México, o el “Agrobot CERES” desarrollado por la Universidad Militar Nueva Granada en conjunto con la Universidad Nacional de Colombia. Estos modelos presentan un primer acercamiento al producto que se pretende desarrollar y han sido usados como guía en la etapa de diseño, sin embargo, no son una solución final para el problema abordado en el presente trabajo.


Manufactura
-----------
Como primera medida se consideran los servicios de manufactura que ofrecen los diferentes laboratorios de la Universidad Nacional de Colombia. Posteriormente se realizó una investigación respecto a los procesos de manufactura disponibles comercialmente en la ciudad de Bogotá que sean asequibles en cuanto a costos, y se elaboró una lista de proveedores que permitieran abastecer los componentes necesarios (ver anexo 400-8). En esta etapa se encontró que los procesos a los que se tiene acceso son operaciones de metalmecánica y maquinado convencional, doblado de perfiles, soldadura y fabricación de PCB  de agujero pasante. Para las labores de corte, taladrado, esmerilado y soldadura se cuenta con los equipos necesarios en el Laboratorio de Mecanización del departamento de Ingeniería Agrícola, laboratorio que pertenece al semillero (cliente).


Presupuesto
-----------
Como se contempla en el contrato social, el presupuesto del que se dispone es de máximo 5'000.000 COP, que serán retornados en su totalidad por el cliente previa presentación de las facturas de los componentes o procesos de manufactura contratados, siempre con un compromiso por parte de los integrantes del equipo de optimizar los recursos.

Desarrollo y análisis de requerimientos
=======================================
* **Portabilidad y desmontabilidad:** El mecanismo no deberá sobrepasar los 60 Kg de peso total, y debe ser parcialmente desarmable, de manera que su transporte y posterior reensamblaje sea cómodo y rápido.
* **Carga útil:** El producto deberá ser capaz de soportar en su plataforma una carga de hasta 6 Kg correspondiente a algún sensor.
* **Capacidad de recorrido:** La autonomía del vehículo debe permitirle recorrer un lote de al menos un cuarto de fanegada en una carga completa para garantizar la eficiencia del proceso de muestreo.
* **Resolución espacial:** El subsistema de adquisición de datos debe ser capaz de almacenar datos con una resolución espacial mínima de al menos 50 cm para garantizar que la precisión de la variable sensada sea mejor que la obtenida por métodos tradicionales.
* **Limitaciones geográficas:** Este primer prototipo estará limitado a funcionar en parcelas pertenecientes a terrenos de la Universidad Nacional de Colombia sede Bogotá, los cuales se caracterizan por ser terreno plano, de corta extensión y de suelo desnudo.


Desarrollo y análisis de especificaciones de ingeniería
=======================================================

Valores priorizados
-------------------
La tabla presenta los requerimientos de ingeniería que han sido tomados en cuenta para la etapa de diseño, así como las respectivas métricas que se deben cumplir en el prototipo final. La tabla está organizada en orden de prioridad, de manera que un parámetro ubicado en una fila superior tendrá prioridad sobre otro ubicado en una fila inferior.

+----------+-------------------------------------+----------------+-----------+-----------------------------------------------------+
| Código   | Requerimiento                       | Valor y unidad | Objetivo  | Criterio de evaluación                              |
+==========+=====================================+================+===========+=====================================================+
| 2.6.1.1. | Carga útil                          | :math:`5\ kg`  | maximizar | Pesar la carga adicional a acoplar en el vehículo y |
|          |                                     |                |           | ponerlo en funcionamiento con esta.                 |
+----------+-------------------------------------+----------------+-----------+-----------------------------------------------------+
| 2.6.1.2. | Peso                                | 60 Kg          | minimizar | Pesar el robot completamente ensamblado y ponerlo en|
|          |                                     |                |           | funcionamiento.                                     |
+----------+-------------------------------------+----------------+-----------+-----------------------------------------------------+
| 2.6.1.3. | Volumen                             | 1 m^3          | minimizar | Medir los valores máximos de alto, largo y ancho del|
|          |                                     |                |           | del robot completamente ensamblado y calcular su    |
|          |                                     |                |           | volumen.                                            |
+----------+-------------------------------------+----------------+-----------+-----------------------------------------------------+
| 2.6.1.4. | Velocidad de crucero                | 7 Km/h         | maximizar | Definir una trayectoria de distancia conocida,      |
|          |                                     |                |           | cronometrar el tiempo de recorrido y con estos datos|
|          |                                     |                |           | calcular su velocidad media.                        |
+----------+-------------------------------------+----------------+-----------+-----------------------------------------------------+
| 2.6.1.5. | Distancia del suelo a la plataforma | 50 cm          | minimizar | Medir la distancia entre el suelo y la carga        |
|          |                                     |                |           | acoplada en la plataforma/interfaz.                 |
+----------+-------------------------------------+----------------+-----------+-----------------------------------------------------+
| 2.6.1.6. | Duración de un ciclo de carga       | 30 minutos     | maximizar | Cronometrar el tiempo de funcionamiento a velocidad |
|          |                                     |                |           | crucero hasta que se descargue la batería.          |
+----------+-------------------------------------+----------------+-----------+-----------------------------------------------------+
| 2.6.1.7. | Radio de giro                       | 50 cm          | minimizar | Someter al robot a movimiento circular uniforme con |
|          |                                     |                |           | diferentes radios sin que pierda el equilibrio.     |
+----------+-------------------------------------+----------------+-----------+-----------------------------------------------------+
| 2.6.1.8. | Tiempo de ensamble                  | 30 minutos     | minimizar | Cronometrar el tiempo que se tarda un operario en   |
|          |                                     |                |           | ensamblar y poner en funcionamiento el robot.       |
+----------+-------------------------------------+----------------+-----------+-----------------------------------------------------+
| 2.6.1.9. | Distancia de teleoperación          | 10 m           | maximizar | Mover el robot de manera que se aleje del centro de |
|          |                                     |                |           | mando y medir la distancia entre estos cuando se    |
|          |                                     |                |           | pierda la conexión.                                 |
+----------+-------------------------------------+----------------+-----------+-----------------------------------------------------+