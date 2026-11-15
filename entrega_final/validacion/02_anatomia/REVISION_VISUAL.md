# Fase 2: anatomía y preparación

**Revisión posterior en fase 5:** las pruebas antiguas de pierna usaban el signo inverso al pliegue anatómico. No se consideran validación anatómica de la rodilla. Se generaron e inspeccionaron codos_rodilla_anatomicos.png, flexion_pelvis_anatomica.png y rodillas_flexion_anatomica.png con el sentido correcto. Esa revisión reveló pesos irregulares del faldón, corregidos en el checkpoint actual de fase 5. Este archivo de fase 2 se conserva como estado histórico recuperable, no como entrega final del rig.

Se revisaron las imágenes reales de mano/muñeca, hombros elevados, codos/rodilla/cadera y flexión de pelvis. Después del ajuste se inspeccionaron codos_rodilla_corregidos.png, flexion_pelvis_corregida.png y rodillas_flexion_detalle.png.

La silueta de brazos, antebrazos y manos permite conservar la anatomía de origen. En la elevación probada los hombros y las axilas permanecen unidos al uniforme. La flexión de codos no abre la manga. Se conservaron los dedos y el esqueleto existente. No se añadió un cuerpo interno oculto bajo el uniforme: el personaje ya emplea cabeza, manos y prendas independientes.

Se detectó una transición irregular de pesos alrededor de las rodillas. Se regularizó la mezcla muslo/pantorrilla dentro de una banda alrededor de cada articulación, con una transición gradual hacia los pesos anteriores. Se conservaron los bucles, las UV y las posiciones de los vértices; no se decimaron articulaciones. El detalle final permite ver la compresión de la rodilla sin una abertura en la prenda. El acabado de los pliegues del pantalón todavía necesita la fase 3.

La pose diagnóstica de pelvis inicial estaba suspendida. Se corrigió la traslación en coordenadas del hueso y se apoyó la pose sobre el suelo antes del nuevo render. Es una prueba estática de flexión, no una animación de agacharse ni un sistema IK.

Auditoría final: geometría, topología y UV idénticas a la fase 1; pesos modificados solo en el pantalón, normalizados y con máximo cuatro influencias. 52 huesos y 44 mallas. El archivo 02_Anatomia.blend está guardado con el rig en reposo y sin la traslación de la pose.

Pendiente dentro del objetivo completo: tela y pliegues (fase 3), revisión específica del cuero y las botas (fase 4), pruebas ampliadas del rig y caminata intermedia (fases 7 y 9). No se considera que estas pruebas iniciales validen una animación completa.
