Subsistema de control y comunicaciones
######################################
Selección de unidad de control
==============================
Para la unidad de control encargada de la recepción y procesamiento de datos así como las señales de mando y la transmisión de señales de pwm para el control de los drivers. (Ver anexo 400-15) Donde se tuvieron en cuenta los parámetros de Tensión de Operación, Alimentación, Consumo, Puertos Digitales	Puertos Análogos y Comunicaciones con las que contaba cada tarjeta.

.. toctree::
    electronics

Diseño de conexiones
====================
El subsistema de control y comunicación comprende a diversos elementos electrónicos de control y transmisión. A continuación se listan los componentes vinculados: 
* Raspberry Pi 4
* 2 Drivers Pololu Dual MAX14870 Motor Driver Shield for Arduino
* Regulador de Tensión de 5V a 3A
* Circuito Integrado ATtiny85-20P
* Fusibles y elementos de protección.
* Elementos de conexión : Borneras, interruptores, pines de interconexión.

El diseño electrónico generado se alimenta con la batería de 24V .El subsistema de control se divide en tres secciones independientes.

Alimentación de la tarjeta Raspberry Pi 4.
------------------------------------------
Esta sección está destinada a alimentar la tarjeta Raspberry a partir de la alimentación inicial.  Ya que la tarjeta se alimenta con una tensión de 5V  a una corriente de 3A se requiere incluir un regulador de tensión y demás elementos de protección(fusibles de 3A) para no poner en riesgo la integridad de la tarjeta.

.. image:: https://user-images.githubusercontent.com/30636259/245347253-6d77602c-404b-48e6-b7fa-f45b970e5c6a.png
    :align: center
    :alt: circuito A

Sección Circuito integrado ATtiny 85-20P
----------------------------------------
.. image:: https://user-images.githubusercontent.com/30636259/245347441-7f4cc2b5-2192-4a9f-803d-8a32887fbde6.png
    :align: center
    :alt: circuito B    

Circuito de control de motores 
------------------------------
Esta sección del montaje eléctrico cuenta con un consumo máximo de 8 amperios, a raíz del consumo de corriente individual de cada uno de los motores.
El circuito parte de una línea de alimentación de 24V y un elemento de activación (interruptor de Parada de Emergencia) el cual interrumpe el funcionamiento del vehículo sin necesidad de apagar el sistema de control en su totalidad, apagando únicamente los motores.
Esta línea alimenta los drivers los cuales controlan 2 motores cada uno. A partir de la tarjeta de control Raspberry se controlan los valores de PWM y Dirección. Ver planos

.. image:: https://user-images.githubusercontent.com/30636259/245347523-3307fc72-d026-4c00-8b0c-2900fd8ef5ca.png
    :align: center
    :alt: circuito C

Fabricación de PCB
==================
El diseño electrónico propuesto para el subsistema de control implica un gran número de conexiones, sin embargo no se amerita la fabricación de una Placa de Circuito Impreso de doble cara.
Uno de los factores de  diseño y fabricación de esta placa es la presencia de altas corrientes en ella. Para la capa de cobre trasera (B.Cu) se manejó un grosor estándar de 0.035mm. En función de este espesor y la cantidad de corriente que transita por las pistas se definió el ancho de las mismas generando tres clases : 


+---------------+----------------+----------------------------+-----------------------+
| Tipo de Pista | Ancho de Pista | Factor de Diseño           | Aplicaciones          |
+===============+================+============================+=======================+
| Pista A       | 0.4 mm         | Baja corriente. Caminos que| Conexiones entre el   |
|               |                | no requieren ningún tipo de| circuito integrado,   |
|               |                | limitación en corriente. Se| la tarjeta Raspberry y|
|               |                | escoge este espesor por    | los controladores.    |
|               |                | viabilidad de las          |                       |
|               |                | conexiones a raíz de un    |                       |
|               |                | proceso de iteración en el |                       |
|               |                | diseño.                    |                       |
+---------------+----------------+----------------------------+-----------------------+
| Pista B       | 1.27 mm        | Pistas con una corriente   | Conexiones de potencia| 
|               |                | admisible de 3 A.          | para la tarjeta       |
|               |                |                            | Raspberry.            |
+---------------+----------------+----------------------------+-----------------------+
| Pista C       | 2.54 mm        | Pistas con una corriente   | Alimentacion de       |
|               |                | admisible de 8 A           | Controladores y       |
|               |                |                            | motores.              |
+---------------+----------------+----------------------------+-----------------------+

A continuación se presenta una imagen del diseño final para la Placa de Circuito Impreso vinculada al sistema de control.

.. image:: https://github.com/cychitivav/pai/assets/30636259/ca4c9cfb-6492-4cda-bf3a-0dccf43555e1
    :align: center
    :alt: PCB
    :width: 50%