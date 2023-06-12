Generación detallada del producto
#################################
Basándonos en la experiencia de expertos y diversas fuentes consultadas, se ha determinado que el diseño de cualquier vehículo debe realizarse de las ruedas hacia arriba. Esto se debe a que los componentes ubicados en la parte inferior del vehículo definen características y requisitos para los componentes superiores.

El diseño del vehículo teleoperado se inicia centrándose en las ruedas, ya que desempeñan un papel fundamental al soportar la carga, proporcionar tracción y determinar la capacidad de movimiento en el terreno. 

A medida que avanzamos en el proceso de diseño, se analizaron y definieron cuatro subsistemas principales: estructural, transmisión, potencia eléctrica y control y comunicaciones. Esto debido a que a pesar que el vehículo cuenta con cuatro ruedas, el sistema de tracción se va a comportar como un vehículo diferencial, es decir, que las ruedas del lado izquierdo y derecho se moverán de forma independiente.

Selección de las ruedas
=======================
En el proceso de selección de las ruedas para nuestro vehículo teleoperado, consideramos diferentes aspectos para encontrar la mejor opción. Nuestro enfoque principal fue la aplicación específica del vehículo y la disponibilidad de las ruedas en el mercado.

Inicialmente, consideramos utilizar ruedas de cuatrimoto con un diámetro de rin de 6 pulgadas. Específicamente, evaluamos las ruedas *Hakuba* que presentaban un labrado de aproximadamente 1 cm, lo cual las hacía adecuadas para enfrentar los desafíos del terreno en el que operaría el vehículo.

.. image:: https://github.com/cychitivav/pai/assets/30636259/8834b1d5-cad8-4a6d-b478-7cf1816791f1
   :alt: Ruedas costosas
   :align: center

Sin embargo, al evaluar los costos asociados y los requisitos de diseño adicionales, decidimos descartar esta opción. El costo de estas ruedas de cuatrimoto ascendía a 1 millón de pesos, sin contar el gasto adicional de diseñar un acople para unirlas al motor del vehículo.

Posteriormente, nos dirigimos al mercado de ruedas y rodachinas en el sector de Ricaurte para buscar alternativas más económicas. Allí encontramos unas ruedas de 10 pulgadas de diámetro que incluían el rin y el acople necesario, a un costo de 50 mil pesos. Estas ruedas estaban diseñadas específicamente para plataformas de carga de hasta 200 libras, lo cual las convertía en una opción ideal para nuestro vehículo teleoperado de muestreo de suelos. Además, si el labrado no fuese suficiente para enfrentar el terreno, podríamos cambiar la llanta por una de mayor agarre, sin necesidad de cambiar el rin o el acople, esto claro, con consentimiento del cliente.

.. image:: https://github.com/cychitivav/pai/raw/assets/30636259/0b9b328a-1edc-4039-8cae-359e0e02b8e1.jpg
   :alt: Ruedas económicas
   :align: center

La selección de las ruedas de 10 pulgadas nos brindó una solución más rentable, ya que cumplía con nuestros requisitos de tracción y estabilidad a un precio mucho más accesible. Además, el hecho de que estas ruedas ya incluyeran el acople necesario simplificó el proceso de integración en el vehículo, ahorrando tiempo y esfuerzo en el diseño y fabricación de un acople adicional.

Una vez las ruedas son seleccionadas, se procede a realizar el diseño de los subsistemas que conforman el vehículo:

.. toctree::
    details/mechanical/structural
    details/mechanical/transmission
    details/electrical/power
    details/control/control
