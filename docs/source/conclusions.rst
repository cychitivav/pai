Conclusiones y trabajo futuro
#############################
Conclusiones
============
* El prototipo desarrollado comprende una primera aproximación a la automatización de muestreo de suelos. Si bien aún se requiere de un operario que manipule el vehículo, el recorrido de este permitirá la captura de datos georreferenciados con una resolución superior a la obtenida por las técnicas tradicionales y menor tiempo requerido en campo.
* Si bien el prototipo puede no funcionar bien en algunos terrenos con pendiente o con tamaño de agregado demasiado grande, en ambientes controlados su desempeño ha sido sobresaliente.
* El diseño conceptual depende de la disponibilidad comercial de algunas piezas, esto facilita su mantenimiento y reparación en caso de ser necesario reemplazar componentes dañados o desgastados.
* El presupuesto ajustado limitó la adquisición de algunos componentes de mayor calidad o precisión que posiblemente habrían resultado en un incremento en el desempeño del prototipo final.

Trabajo futuro
==============

Autonomía del robot
-------------------
El alcance del presente proyecto limitó el prototipo a ser teleoperado, de manera que el sistema de control funciona en lazo abierto y la única realimentación de la localización del vehículo es la observación directa del operario. Se espera a futuro seguir trabajando dentro del semillero SIMA en la implementación de sensores que permitan al robot solucionar el problema de navegación y generar trayectorias de forma independiente.

Suspensión
----------
Si bien el diseño de detalle presenta un sistema de amortiguamiento, este no pudo ser implementado en la construcción del prototipo debido a problemas de disponibilidad de los componentes. Se espera en un futuro adquirir los resortes que cumplan con las especificaciones calculadas e instalarlos en el prototipo.

Captura de datos
----------------
El subsistema de captura de datos georreferenciados no estaba contemplado en el presente proyecto, sin embargo comprende la aplicación real del vehículo desarrollado. El objetivo del semillero es proponer un nuevo proyecto para diseñar y/o adecuar sensores que permitan la medición de variables físicas del suelo e implementar (en lo posible en el mismo controlador) un software que almacene estas mediciones para futuro procesamiento.
