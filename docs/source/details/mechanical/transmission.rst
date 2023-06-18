Subsistema de transmisión
=========================
Selección de rodamientos
------------------------
Para llevar a cabo esta evaluación, se recopilaron los datos técnicos proporcionados por SKF y se compararon con los requisitos de carga especificados. Además, se consideraron aspectos como la capacidad de carga, las dimensiones del rodamiento, la calidad y confiabilidad del fabricante, así como la lubricación.

Resultados:
^^^^^^^^^^^

* **Capacidad de carga:** Según la información suministrada por SKF, el rodamiento 63003 tiene una capacidad de carga radial estática de 3,25 kN y una capacidad de carga radial dinámica de 6,56 kN. Dado que la carga radial en la aplicación es de 500 N, se determinó que el rodamiento seleccionado puede soportar de manera segura esta carga con un margen significativo.
* **Dimensiones:** El rodamiento 63003 SKF tiene un diámetro interior de 17 mm, un diámetro exterior de 35 mm y un ancho de 14 mm. Estas dimensiones son adecuadas para la aplicación en consideración, lo que permite un ajuste adecuado y un funcionamiento eficiente.
* **Calidad y confiabilidad:** SKF es reconocido como un fabricante líder en la industria de rodamientos, conocido por producir productos de alta calidad y confiables. Esto respalda la fiabilidad del rodamiento 63003 SKF y su capacidad para resistir condiciones exigentes en la aplicación.
* **Lubricación:** El rodamiento 63003 SKF se suministra prelubricado de fábrica con grasa de alta calidad. Esto reduce la fricción y el desgaste, y contribuye a una vida útil prolongada del rodamiento. Sin embargo, se recomienda mantener una adecuada lubricación durante la operación para garantizar un rendimiento óptimo a largo plazo.

En conclusión, con base en los resultados del análisis, se concluye que el rodamiento 63003 SKF es una elección adecuada para soportar cargas radiales de 500 N en la aplicación estudiada. Su capacidad de carga, dimensiones apropiadas, calidad y confiabilidad, respaldadas por la reputación del fabricante, lo convierten en una opción recomendada.

Diseño del eje y elementos auxiliares
-------------------------------------
El dimensionamiento del eje involucra varias iteraciones de diseño, donde se analizaron las distintas implicaciones que conllevaba cada geometría del eje. Inicialmente se optó por la geometría dispuesta en la figura del eje, donde se cuenta con 3 secciones de diámetros diferentes. La sección externa tendría un diámetro de 34.1 milímetros con el fin de encajar en la flor que acopla la llanta., mientras una sección central de mayor diámetro permitiría durante el progreso del diseño impedir el deslizamiento axial de este eje. El diámetro más interno corresponde a las dimensiones de los rodamientos seleccionados. Dentro de esta sección se maquinaría un agujero con chavetero que permitiría la transmisión de torque del motor a este eje. La dimensión de esta abertura estaría predefinida por las dimensiones del eje de salida del motor ya escogido. Por otro lado durante la primera iteración se establecieron las fuerzas que actuaban sobre el eje, que eran producidas por el resto de elementos en contacto con este(Rodamientos, acople llanta, eje del motor), las cuales también se encuentran en la siguiente figura.

.. image:: https://user-images.githubusercontent.com/30636259/245341525-94a3283a-873a-4037-b517-5d8eeef556d2.png
    :width: 50 %
    :alt: eje1
    :align: center

Al considerar todas estas interacciones se llegó a un sistema estáticamente indeterminado que sería difícil de complementar con una ecuación de deformación, debido a las diferentes y complejas geometrías preliminares. Si se asume que el motor es totalmente soportado por la estructura externa, entonces este no ejercería una fuerza radial sobre el eje, solamente ejercería el torque, por lo que se para las siguientes iteraciones se despreciaría esta fuerza (E1). Durante el estudio de distribución de fuerzas sobre el eje se consideraron varios valores para s y L, y se observó que L afecta enormemente el momento flector que siente el eje, por lo que se opta por mantener esta distancia lo mínima posible. También se elige mantener la distancia entre los rodamientos de apoyo en aproximadamente 30 milímetros, con el fin de minimizar el momento a la vez que se deja espacio para el mecanismo basculante que va sobre la estructura auxiliar. 

Posteriormente se observó que el cambio de diámetro de 34 mm a 17 mm causaba un importante concentrador de esfuerzos, lo que hizo reconsiderar todo el diseño del eje. Es de esta manera que se decidió utilizar un diámetro único de 17 mm para todo el eje y de esta manera evitar los concentradores de esfuerzos por cambios abruptos de sección, para acoplar la flor de la llanta al eje se opta por usar una camisa auxiliar que permita encajar el eje y la flor de la llanta a su vez que mantiene la transición centrada. Debido a la sección única, se decidió utilizar anillos seeger para evitar el deslizamiento axial del eje. Estos anillos se situarían en unas ranuras que van en el espacio entre los dos rodamientos de apoyo. Además para transmitir el torque a la llanta se opta por usar un pasador que atraviesa la flor, la camisa y el eje como tal, por lo que se hace necesario maquinar en el eje un agujero transversal donde vaya alojado este pasador de transmisión. Es así que se llega al nuevo y definitivo diseño del eje, que se puede observar en la siguiente figura. 

.. image:: https://user-images.githubusercontent.com/30636259/245341539-2d777165-f171-49b9-9464-2d0bd261edb0.png
    :width: 50 %
    :alt: eje1
    :align: center

Para verificar el correcto diseño de este eje se lleva a cabo un detallado análisis que permite establecer el factor de seguridad a fatiga del eje junto a los componentes auxiliares de este (Camisa y pasador). Dicho análisis puede verse en el anexo “Diseño de elementos de transmisión de potencia”. En dicho análisis se observó que se puede optimizar el factor de seguridad en función del diámetro del pasador. De este análisis se obtuvo un factor de seguridad mínimo y óptimo de aproximadamente 1.8, que corresponde a la fatiga por flexión del pasador. Ya con dicho factor se dan por establecidas todas las dimensiones del eje, camisa y pasador. 
