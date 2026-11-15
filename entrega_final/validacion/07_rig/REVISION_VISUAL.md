# Fase 7 — rig humanoide

Se inspeccionaron los renders de `final/`: brazos levantados, codos, giro de torso, cabeza/cuello, caminata, carrera y agachado. También se revisaron los detalles de cuello, hombros por detrás y codo en carrera. Son posturas de comprobación, no ciclos de animación.

Las mangas conservan continuidad al elevar los brazos. La zona oscura de la axila se contrastó con una vista de colores planos: corresponde a pliegue y sombra. La flexión fuerte comprime la tela en la cara interior del codo; se suavizaron los pesos de esa zona y se transfirieron al remiendo cosido. Permanece un pliegue marcado, sin rotura visible en el detalle final.

Los reguladores metálicos se deformaban con el reparto anterior de pesos. Se fijaron como piezas rígidas a anclajes de `spine`, conservando su posición en reposo, y se regularizaron los pesos del tirante a esa altura. En las tres posturas medidas el cambio absoluto máximo de longitud de arista es menor que 0,00000009 m, compatible con error numérico.

Se revisaron la cintura, el faldón y los accesorios al caminar, correr y agacharse. No se aprecian intersecciones graves en estas posturas. Esto no cubre todas las poses posibles: una animación definitiva deberá revisar sus extremos y contactos concretos.

`auditoria_final.json` confirma 13.523 vértices, 25.792 triángulos, 46 mallas del personaje, cinco materiales, 14 imágenes empaquetadas y 52 huesos. Las 46 mallas conservan sus coordenadas locales, caras y UV respecto de fase 6. Cambiaron pesos de seis objetos. Esqueleto en reposo, nombres y jerarquía conservados; mapa de 51 huesos deformantes válido, más raíz no deformante. Máximo cuatro influencias normalizadas por vértice.

La biblioteca independiente vuelve a cargar sin armadura: 29 maestros y tres conjuntos. Hay 25 anclajes; 19 accesorios rígidos y diez deformables. Los maestros comparten datos de malla con las piezas montadas.

Fase 7 completada. Pendientes de las fases 8 y 9: evaluación de materiales/presupuesto y comprobación final de entrega.
