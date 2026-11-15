# Fase 6: biblioteca modular y anclajes

Archivo actual para continuar: `06_Modular.blend`. Incluye al personaje, biblioteca interna y dos escenas de presentación. Biblioteca reutilizable independiente: `Biblioteca_Umbral.blend`.

## Refinamiento de los accesorios

Se revisaron los accesorios existentes antes de preparar maestros. Cantimplora, bolsillos, botas y casco conservan las correcciones previas. La mochila recibió un ajuste leve de volumen y caída, de hasta 3,47 mm, y pliegues finos de lona horneados. La manta dejó de tener una sección completamente regular mediante variaciones inferiores a 0,48 mm y relieve superficial, conservando las zonas de sujeción y el extremo enrollado. No se añadieron accesorios de carga ni polígonos al personaje.

Se inspeccionó equipo_refinado.png antes de organizar la biblioteca. El atlas de equipo se horneó de nuevo sobre la misma distribución UV; se mantuvieron cinco materiales y 14 mapas usados en el personaje.

## Estructura entregada

Dentro del proyecto, `MODULAR_LIBRARY` contiene 29 piezas maestras en `Helmets`, `Backpacks`, `Belts`, `Pouches`, `Canteens`, `Boots`, `Utility_Props` y `Repairs`. Los dos remiendos y las botas/cantimplora revisadas corresponden al estado actual, no a la biblioteca antigua de v2.

Los tres recursos de colección son casco con barboquejo, cantimplora con funda y mochila equipada con cierres, bolsillo, cuerda y manta. Las piezas tienen nombres consistentes, malla independiente del cuerpo y datos compartidos con su copia montada. Los conjuntos y las escenas de catálogo reutilizan esas mallas; no son duplicados independientes de geometría.

Los maestros tienen transformación identidad, unidades métricas, frente local -Y y vertical local +Z. Sus orígenes representan el punto de montaje descrito en cada recurso y en catalogo.json. Casco y cantimplora comparten marco entre sus componentes para recomponerlos directamente. La mochila equipada guarda las transformaciones relativas de sus seis partes.

Se crearon 25 anclajes en `ATTACHMENTS`. Diecisiete accesorios rígidos siguen un anclaje de hueso sin una segunda deformación por armadura. Doce accesorios —botas, piezas cosidas y correas deformables— mantienen pesos de armadura y usan su anclaje como referencia de ajuste. Ningún accesorio se fusionó con el cuerpo.

## Inspección visual y correcciones del catálogo

Se inspeccionaron biblioteca_piezas.png y biblioteca_conjuntos.png. La primera lámina recortaba filas y extremos: se corrigió la escala de cámara para el formato vertical. La primera vista previa de mochila leía matrices de mundo no evaluadas en una colección oculta y superponía sus piezas; se corrigió para usar las transformaciones de base guardadas y se añadió una prueba numérica de colocación de todos los componentes. El catálogo final muestra las 29 piezas completas y los tres conjuntos ensamblados.

También se inspeccionaron personaje.png y espalda.png del nativo reorganizado. No aparecieron desplazamientos de equipo ni cambios de silueta por el cambio de orígenes o parentescos.

## Evidencia técnica de reutilización

- 29 maestros, 29 datos de malla compartidos con el personaje, tres conjuntos y 25 anclajes.
- Comparación antes/después en reposo, torsión de torso/cabeza, giro de pelvis y flexión de extremidades: error máximo 0,000000369 m. La organización no altera las poses de origen.
- Se movió el anclaje real de cantimplora: botella y funda se desplazaron juntas; cinturón y maestros permanecieron inmóviles. Se restauró la transformación antes de terminar la comprobación.
- La biblioteca se cargó en una escena vacía: 29 piezas maestras, tres conjuntos, 29 mallas únicas y cero objetos de armadura. Ningún objeto de la biblioteca tiene padre, modificador o restricción dependiente del personaje. Las texturas están empaquetadas.
- Cantimplora completa y mochila equipada se cargaron por separado. Se verificó su número de piezas y sus límites espaciales, además de la posición de cada componente respecto a su equivalente montado.
- Los grupos de pesos se conservan como información opcional en los maestros compartidos; no enlazan a un esqueleto. La biblioteca puede ajustarse y vincularse a otro personaje.

El personaje mantiene 13.523 vértices, 25.792 triángulos, 46 mallas, cinco materiales, 14 imágenes empaquetadas y 52 huesos. La biblioteca oculta y las copias de presentación no forman parte de esas cifras del personaje ni de la selección de exportación.

La fase 7 debe ampliar las pruebas de rig y de intersecciones. La optimización, el presupuesto de triángulos y la inspección final siguen pendientes de fases 8 y 9. Esta reorganización no equivale a una animación terminada.
