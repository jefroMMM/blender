# Fase 4: botas militares

**Revalidación posterior en fase 5:** se detectó que la pose de pierna antigua usaba el sentido inverso al pliegue anatómico de rodilla. Se regeneró e inspeccionó flexion_anatomica.png sobre este mismo archivo, con el sentido correcto, sin modificar el nativo. La nueva imagen valida la unión de suela y cuero en la postura probada; flexion.png se conserva como diagnóstico de la pose anterior y no se usa como prueba anatómica.

Punto de control aprobado para la siguiente fase: 04_Botas.blend. La fase 3 permanece recuperable e intacta.

## Construcción y correcciones

Se conservaron las proporciones corregidas de v2, la caña, la mayor parte de la pala, lengüetas, cordones, ojales y tiradores de ambas botas. Se sustituyó el componente de suela que sobresalía como una plataforma recta por un contorno muestreado sobre la horma existente: 40 puntos y cinco niveles para el borde inferior, pared y encuentro superior. Se añadieron un arco inferior discreto y un apoyo de talón definido a partir de los tacos existentes. Se retiró el taco del centro que anulaba el arco.

La primera prueba de elevar la base cerrada del cuero generó puntas y sombras triangulares en el talón. Se descartó esa solución. En el resultado final se recortó únicamente la zona inferior a 4 cm y se construyó una franja continua hasta la suela, sin cambiar la caña ni la forma superior de la puntera. La parte inferior abierta de esa franja queda oculta dentro de la suela; no es una abertura visible en el calzado.

La costura de la puntera se volvió a colocar sobre la pala. Los pliegues leves de empeine/tobillo, grano de cuero y roughness se hornearon en el atlas de equipo. El perfil permite distinguir cuero y caucho, con una unión continua y sin el saliente rectangular anterior del talón.

Las botas siguen siendo dos objetos modulares independientes, con transformaciones, origen y grupos de huesos conservados. La biblioteca de maestros todavía debe sincronizarse en la fase 6.

## Revisión de imágenes

Se inspeccionaron tres_cuartos.png, perfil.png, talones.png, flexion.png, conjunto.png y equipo_espalda.png del resultado final. El perfil final se reencuadró para incluir toda la suela y sus tacos; el perfil de referencia inicial cortaba parte del borde inferior.

La prueba de flexión combina muslo, rodilla, tobillo y punta del pie izquierdo. En la postura probada la suela permanece con el calzado, el cuero del tobillo no se separa y el pantalón sigue entrando en la caña. Es una prueba estática; los ensayos amplios de correr/agacharse y caminata intermedia siguen pendientes de fases 7 y 9.

Se revisaron también los conjuntos frontal y posterior porque el nuevo atlas incluye otros seis objetos de equipo. La redistribución de UV no cambió la geometría del casco, mochila, manta, cuerda, placa o venda. Las texturas se transfirieron desde sus UV fuente antes de asignar el nuevo atlas.

## Auditoría técnica y presupuesto

- 13.149 vértices, 25.060 triángulos, 44 mallas, cinco materiales, 14 imágenes utilizadas y empaquetadas, 52 huesos.
- Geometría y pesos de las otras 42 mallas idénticos a la fase 3.
- UV reorganizadas solo en los ocho objetos del atlas de equipo; las otras familias de texturas se conservan.
- Todas las mallas permiten calcular tangentes, sin caras de área nula ni aristas con más de dos caras.
- Pesos normalizados y máximo cuatro influencias. Rig guardado en reposo antes de renderizar las pruebas.
- Las botas añadieron 439 triángulos en total respecto a la fase 3 para mejorar el contorno, el bisel y la unión con el cuero. Esa subida es deliberada y evita sacrificar la silueta por una reducción pequeña. La desviación global del presupuesto de 12.000–20.000 triángulos sigue pendiente de la fase 8; esta auditoría no la da por resuelta.

No se han declarado finalizados el desgaste postapocalíptico, la biblioteca, el rig de entrega ni las pruebas finales del personaje.
