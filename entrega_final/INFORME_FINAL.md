# Vigías del Umbral — soldado modular

**Estado: entrega final verificada.** Se inspeccionaron directamente las 16 imágenes finales: nueve vistas estáticas y siete posturas FK. Las auditorías de nativo, biblioteca y transferencia GLB están aprobadas. `revision_visual.json` identifica los archivos observados mediante sus hashes.

Personaje de una facción militar ficticia, inspirado en uniformes y tecnología de la Segunda Guerra Mundial, con desgaste moderado de supervivencia. Se refinó el personaje existente conservando su identidad, ropa y accesorios; los puntos de control anteriores siguen recuperables en el proyecto local.

## Archivos

- `Vigias_del_Umbral.blend`: personaje, rig FK, biblioteca interna, escenas de catálogo y cámaras de entrega. Texturas empaquetadas.
- `Vigias_del_Umbral.glb`: personaje y rig para intercambio, con las texturas embebidas.
- `Biblioteca_Umbral.blend`: biblioteca independiente sin cuerpo ni armadura; 29 piezas y tres conjuntos.
- `blender_assets.cats.txt` y `catalogo.json`: categorías, anclajes y piezas.
- `humanoide.json` y `esqueleto.json`: mapa de retargeting y jerarquía.
- `poses_referencia.py`: funciones de poses FK, también incluidas como texto dentro del Blender. No se ejecutan automáticamente.
- `auditoria_nativo.json`, `auditoria_glb.json`, `camaras.json` y `poses_verificadas.json`: comprobaciones de entrega.

## Cifras del personaje montado

| Medida | Resultado |
|---|---:|
| Vértices del nativo | 12.964 |
| Triángulos del nativo | 24.674 |
| Mallas del personaje | 46 |
| Objetos con rig y anclajes | 72 |
| Materiales compartidos | 5 |
| Imágenes empaquetadas | 14 |
| Huesos | 52 |
| Influencias máximas por vértice | 4, normalizadas |
| Maestros reutilizables | 29 |
| Conjuntos completos | 3 |
| Anclajes | 25 |
| Accesorios rígidos / deformables | 19 / 10 |

Estas cifras excluyen estudio, cámaras y copias de catálogo. Los maestros y piezas montadas comparten los datos de malla; no son geometría adicional del personaje exportado.

## Materiales y presupuesto

Cinco materiales PBR para piel, ojos, uniforme, equipo y cantimplora. El cuero, metal y las telas se distinguen mediante color, rugosidad y detalle normal. Las reparaciones comparten atlas de uniforme. Color en sRGB; normales/ORM en Non-Color. ORM: R=1 (sin AO horneada), G=roughness y B=metallic.

Se conservan nueve imágenes 2048² y cinco 1024²: 164 MiB en RGBA8 sin compresión, aproximadamente 219 MiB con mipmaps completos. El motor de destino decide compresión y consumo real.

La malla queda **4.674 triángulos (23,37 %) por encima** del extremo orientativo de 20.000. Es una desviación deliberada: se priorizan rostro, dedos, bucles de deformación, botas completas y accesorios que pueden desmontarse y reutilizarse. Rostro/ojos/manos suman 7.883 triángulos; botas, 2.539; cantimplora completa, 1.708; ropa y resto del equipo, 12.544.

Se redujeron 1.118 triángulos en superficies rígidas de cantimplora. Las diferencias muestreadas entre superficies fueron inferiores a 0,6 mm. Se descartaron reducciones de otras piezas que alteraban detalles o silueta; no se aplicó decimación a articulaciones. No se recorta el cráneo bajo un casco desmontable ni los reversos útiles de piezas reutilizables. El cuerpo interno oculto innecesario ya estaba retirado. La entrega conserva un único nivel de detalle; no incluye LOD de multitudes.

## Rig y transferencia

Rig FK `RIG | Caminante`, con colecciones Cuerpo, Brazos, Piernas y Dedos. Raíz no deformante más 51 huesos deformantes, con nombres consistentes. Permite mover cabeza/cuello, torso, brazos, dedos y piernas y construir poses de caminata, carrera y agachado. Sin IK, controles faciales ni ciclos terminados; no se solicitaron animaciones complejas.

Muslo +X hacia delante; rodilla -X para flexionar; codo +X para flexionar. Giro de torso y cabeza sobre Y local. Los reguladores metálicos siguen anclajes rígidos de columna; casco sigue cabeza, mochila torso y cantimplora/bolsas cintura. Botas y prendas conservan pesos por armadura. No hay simulación física de accesorios.

El GLB contiene 46 mallas, cinco materiales, 14 imágenes y 52 huesos. Se volvió a importar y se transfirieron las siete posturas mediante los movimientos de los huesos en espacio mundial. Diferencia máxima muestreada de superficie: 0,000010764 m (aproximadamente 0,011 mm); en reposo, 0,000000612 m. El exportador omite un triángulo diminuto de la funda: GLB 24.673 frente a 24.674 del nativo. Las pruebas de superficie incluyen esa diferencia. El widget Icosphere que Blender crea al importar para representar huesos no forma parte del GLB ni se cuenta como malla del personaje. La prueba verifica geometría y transferencia del rig, no idéntica iluminación entre motores.

## Abrir y renderizar

Abrir `Vigias_del_Umbral.blend`. La cámara activa es `FINAL | tres_cuartos`, con encuadre de cuerpo completo y sin borde de render. F12 genera la imagen; F11 muestra u oculta la ventana de resultado. En la imagen, Home ajusta el render a la ventana.

Para ver la espalda, seleccionar `FINAL | posterior` en el Outliner y, con el cursor sobre la vista 3D, pulsar Ctrl+0 del teclado numérico para activarla; después F12. También hay cámaras frontal, lateral, rostro y detalles. Las cámaras de cuerpo completo usan una pequeña elevación para evitar que el horizonte del suelo atraviese al personaje.

El rig está oculto en la vista para facilitar la inspección. Mostrarlo desde el Outliner y entrar en Pose Mode para animar. El archivo está guardado en reposo.

Para reutilizar equipo, añadir la biblioteca en las preferencias de Asset Libraries o usar File > Append. Los maestros tienen origen de montaje, transformaciones de objeto identidad, mallas independientes y materiales compartidos. Los grupos de pesos se conservan como referencia opcional; la biblioteca no necesita la armadura original.

Para exportar todo el personaje, incluir **la colección `CENIZA | Modular` completa**, con mallas, rig y anclajes; excluir `MODULAR_LIBRARY` y escenas de catálogo. Al automatizar la selección, primero mostrar los objetos, actualizar la vista y después seleccionarlos, comprobando los 72 objetos: cambiar visibilidad mientras se itera una colección puede invalidar su lista interna en Blender.

## Inspección visual y alcance de las pruebas

Se abrieron e inspeccionaron las cuatro vistas de cuerpo completo (`frontal`, `posterior`, `lateral`, `tres_cuartos`), tres del rostro y dos de uniforme/equipo. Cabeza, manos y pies quedan completos en las vistas generales. Las vistas de detalle recortan intencionadamente el resto del personaje. Se corrigió el horizonte del suelo que aparecía tras la figura en las primeras cámaras frontal/posterior/lateral y en el primer rostro tres cuartos; se revisaron sus imágenes de reemplazo.

Se inspeccionaron `brazos_arriba`, `codos`, `torso`, `cabeza_cuello`, `caminar`, `correr` y `agachado`. Las mangas conservan continuidad en axilas y codos; la flexión fuerte produce compresión y un pliegue marcado en el codo. El faldón y los bolsillos siguen las caderas sin las puntas largas observadas en las pruebas anteriores. Las rodillas flexionan en el sentido anatómico y los remiendos acompañan la prenda. El cuello gira dentro del uniforme sin una abertura grande visible. Casco, mochila, cantimplora y bolsas permanecen vinculados a sus anclajes.

Las imágenes mantienen desgaste moderado, marca ficticia y diferencias entre tela, cuero, metal y piel. No se observaron roturas ni intersecciones graves en las vistas y posturas inspeccionadas. Las poses son referencias estáticas de flexión, no ciclos terminados ni una comprobación de todos los movimientos posibles.

## Problemas pendientes y límites

No quedan defectos graves detectados sin corregir en estas pruebas. Se conserva conscientemente la desviación de geometría indicada: 24.674 triángulos y un único LOD. El rig es FK básico; las animaciones definitivas necesitarán ajustar contactos de pies/manos y revisar sus extremos concretos. No se incluyen IK, animación facial ni ciclos terminados, que estaban fuera del alcance solicitado. La iluminación y algunos efectos de piel del nativo pueden variar según el motor que abra el GLB.

## Fuentes

Anatomía base y piel derivadas de assets CC0 de MakeHuman Community y jartur69, adaptadas al personaje. Créditos y texto de licencia en `FUENTES_Y_LICENCIAS.md` y `LICENSE.ASSETS.md`. La facción, marca y equipo adaptado son ficticios.
