.. _design:
    
Diseño conceptual
#################
Generación de conceptos a partir de análisis funcional y requerimientos
=======================================================================
Alternativas de solución
------------------------
Al momento de buscar alternativas de solución se realizó el boceto de diferentes configuraciones de ruedas, así como mecanismos de transmisión de potencia y sistemas de amortiguamiento  (ver Anexo 400-9 reporte de boceto)


Definición de subsistemas
=========================
Estructura
----------
La estructura está compuesta por placas paralelas atornilladas a los subsistemas de transmisión. De igual forma, la estructura de soporte de interfaz se atornilla a las placas paralelas. Se usa una chapa superior con una matriz de agujeros como interfaz donde se ubican los futuros posibles sensores a usar.

Transmisión y suspensión
------------------------
El sistema de transmisión consta de un eje acoplado al motor, y un elemento de transmisión de torque hacia el acople de la llanta. Este eje irá soportado sobre dos rodamientos que garantizarán la estabilidad estática de este subsistema. También se contará con un mecanismo basculante donde se podrá incorporar una amortiguador para cada una de los subsistemas de transmisión de potencia. 

Potencia eléctrica
------------------
Este sistema está compuesto por un motor eléctrico, una batería y un controlador. El motor eléctrico es el encargado de generar el torque necesario para el movimiento del vehículo. La batería es la encargada de almacenar la energía eléctrica que será suministrada al motor. El controlador es el encargado de regular la energía que es suministrada al motor, de acuerdo a las instrucciones que recibe del sistema de control y comunicación.

Control y comunicación
----------------------
Finalmente, el sistema de control y comunicación está compuesto por una Raspberry Pi, la cual es la encargada de procesar la información recibida por el módulo de comunicación inalámbrica y enviar las instrucciones al sistema de potencia eléctrica.
