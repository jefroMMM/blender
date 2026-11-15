# Inspección de entrega final

Se abrieron directamente las 16 imágenes de esta entrega. `revision_visual.json` registra sus hashes para distinguirlas de las imágenes anteriores y de las primeras versiones de encuadre. El nativo está en reposo; las poses se aplicaron en memoria para renderizar.

## Vistas estáticas

- `renders/frontal.png`, `posterior.png`, `lateral.png` y `tres_cuartos.png`: cuerpo completo, sin corte de casco, manos ni pies. Conservan silueta, proporción de las botas y equipo de cintura/espalda. Se corrigió la línea del suelo del estudio en las primeras tres y se inspeccionaron los reemplazos.
- `renders/rostro.png`, `rostro_lateral.png` y `rostro_tres_cuartos.png`: expresión seria, barba corta, sombra de ojos y variación discreta de piel; proporciones de nariz, boca y orejas conservadas. La edad aparente es una lectura artística. Se volvió a renderizar y revisar el tres cuartos para quitar una línea del fondo cerca del hombro.
- `renders/uniforme_equipo.png` y `equipo_posterior.png`: prendas y costuras, bolsillos, correas, mochila/manta y cantimplora. Acabado mate de tela, respuesta diferente de cuero y herrajes, remiendos y variación de uso. Estas son vistas de detalle y recortan el resto del cuerpo intencionadamente.

## Pruebas de deformación

- `poses/brazos_arriba.png`: mangas y axilas continuas, tirantes y reguladores estables; brazos y dedos completos en imagen.
- `poses/codos.png`: flexión de ambas mangas sin abertura grave; compresión interior y pliegue exterior visibles, remiendo acompañando manga.
- `poses/torso.png`: camisa/tapeta se torsionan con el torso; reguladores mantienen su forma rígida, equipo de cintura permanece sujeto.
- `poses/cabeza_cuello.png`: cabeza y casco giran juntos; cuello y camisa mantienen una transición sin gran rotura visible.
- `poses/caminar.png`: flexión anatómica de rodillas/tobillos, prendas y equipo acompañan el movimiento. Pose de referencia, sin resolver un ciclo de apoyos.
- `poses/correr.png`: mayor flexión de codos, cadera y rodilla; no se aprecia una rotura grande de prendas o remiendos. El faldón sigue la pierna sin la punta larga de las pruebas antiguas.
- `poses/agachado.png`: cintura, faldón y bolsillos comprimidos de forma continua, rodillas flexionadas y botas acompañando las piernas; accesorios estables.

No se observaron roturas ni intersecciones graves en estas vistas y posturas. La compresión fuerte mantiene pliegues marcados, especialmente en codos y cintura. Una animación terminada debe comprobar sus extremos y contactos propios; estas imágenes no se presentan como ciclos acabados.

Las cifras, arquitectura modular y límites del rig se documentan en INFORME_FINAL.md. El presupuesto de 24.674 triángulos supera el extremo orientativo de 20.000 y se justifica expresamente; no se oculta como una optimización a 20k.

Fase 9 completada tras inspección real de las imágenes, auditoría de nativo/biblioteca y prueba de reimportación GLB.
