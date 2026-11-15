# Fase 8 — materiales y optimización

Proyecto: `08_Materiales.blend`. Biblioteca reutilizable: `Biblioteca_Umbral.blend`. Ambos contienen imágenes empaquetadas. `08_Antes.blend` conserva el rig de fase 7; `08_Geometria.blend` separa la reducción de geometría de los cambios de material.

Se mantienen cinco materiales compartidos: piel, ojos, uniforme, equipo y cantimplora. Los mapas de color usan sRGB; normales y ORM usan Non-Color. ORM contiene R=1 (sin oclusión horneada), G=roughness y B=metallic. No se presenta R como una oclusión calculada.

Los atlas existentes incorporan fibra muy sutil en tela y grano en cuero, con variación de rugosidad. El cuero tiene reflejo más amplio que el metal; se ajusta la respuesta del herraje expuesto sin convertir lona o pintura de casco en metal uniforme. La piel y los ojos conservan su material específico. Los remiendos usan zonas del atlas de uniforme y no añaden materiales.

Texturas: nueve imágenes de 2048² y cinco de 1024²; 14 en total. En RGBA8 sin compresión representan 164 MiB, aproximadamente 219 MiB con una cadena completa de mipmaps. La memoria real depende del formato y compresión del motor. Los PNG empaquetados no representan ese consumo de GPU. Este proyecto conserva calidad de autoría; la plataforma de destino deberá escoger compresión y resolución.

## Presupuesto de geometría

12.964 vértices y 24.674 triángulos en las 46 mallas del personaje. Hay 72 objetos contando armadura y 25 anclajes. Los maestros y vistas de catálogo comparten datos y no se suman al personaje montado.

Se eliminaron 1.118 triángulos de las dos piezas rígidas de cantimplora, manteniendo sus mallas independientes. La reducción conserva los enlaces de maestros, conjuntos y vistas previas. Las comprobaciones muestreadas de distancia entre las superficies anteriores y posteriores, en ambas direcciones, dieron como máximos 0,5845 mm para botella/tapón y 0,5109 mm para funda/soporte. Son medidas muestreadas sobre vértices y centros de triángulo, no una garantía matemática de distancia máxima sobre toda la superficie.

Se probaron reducciones locales de otras piezas rígidas y se descartaron cuando excedían las tolerancias fijadas, afectaban piezas pequeñas o desplazaban la silueta. `optimizacion.json` conserva los intentos. Las 44 mallas restantes conservan geometría, UV y pesos, incluidos rostro, manos, articulaciones, prendas y botas. No hay subdivisiones ni modificadores de geometría pendientes.

### Desviación justificada

La entrega queda 4.674 triángulos (23,37 %) por encima del extremo orientativo de 20.000. Se conserva deliberadamente esta versión porque el objetivo prioriza silueta, deformación y reutilización sobre una decimación indiscriminada.

- Rostro/cuello, ojos y manos con dedos: 7.883 triángulos.
- Botas completas con suelas, cordones y ojales: 2.539.
- Botella y soporte reutilizables: 1.708.
- Uniforme y resto del equipo: 12.544.

No se recorta la cabeza cubierta por el casco ni los reversos necesarios del equipo: casco y accesorios deben poder desmontarse y reutilizarse. El cuerpo oculto innecesario ya se retiró en la preparación anatómica. No se han reducido los bucles de articulaciones. Para multitudes o dispositivos de menor capacidad convendría producir un LOD adicional adaptado a la distancia y motor concretos; esta entrega no contiene ese LOD.

`auditoria_final.json` verifica geometría deformable preservada, pesos normalizados, UV, tangentes, mapas empaquetados y carga de biblioteca sin dependencia de armadura. La inspección visual se documenta por separado al terminar los renders de esta fase.
