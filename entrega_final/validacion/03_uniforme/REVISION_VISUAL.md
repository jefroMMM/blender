# Fase 3: uniforme y tela

**Revisión posterior en fase 5:** la antigua pose de rodilla se definió en sentido inverso al anatómico. Se repitió la prueba en pliegues_flexion_anatomica.png y se detectó un defecto de pesos en la cintura/faldón al flexionar. La corrección está en 05_desgaste/05_Desgaste.blend y se comprobó mediante agachado_revision.png y faldon_flexion.png. El checkpoint de fase 3 permanece sin modificar para recuperación; sus poses antiguas no validan la flexión anatómica final.

Punto de control: 03_Uniforme.blend. Conserva la chaqueta y los pantalones de origen.

## Cambios revisados

- Silueta: pequeñas variaciones en mangas, flancos/cintura, rodillas y entrada de las botas, de hasta unos 2,5 mm. Se mantuvieron las mallas y los bucles existentes.
- Superficie: arrugas de compresión en codos y axilas, cintura y rodillas, tensión diagonal de entrepierna y pliegues en tobillos. La microtextura y los pliegues finos están horneados en el atlas normal de 2048 px; no se añadieron subdivisiones.
- Tela: roughness alta y variación sutil de color, con relieve fino. Se conservaron las diferencias de cuero y metal del atlas compartido en correas, hebillas y equipo.
- Bolsillos: se relajaron sus centros manteniendo la sujeción del perímetro, fuelles, solapas y costuras independientes del cuerpo. Los cuatro continúan como accesorios separados.
- Cuello: la parte superior de la tapeta original se iba hacia la espalda, dejando piel visible a través de un hueco. Se corrigió su trayectoria, se suavizó su superficie y se amplió la zona superior para que cubriera la abertura. No se reemplazó el uniforme.
- Puño/manga: el detalle mostró cortes triangulares en la venda derecha por cruce de superficies. Se reajustó contra la manga con una separación pequeña; la prueba de colores planos y el render final ya muestran una banda continua.

## Inspección real

Se inspeccionaron torso.png, pantalon.png, cuello.png, espalda.png, manga_puno.png y pliegues_en_flexion.png. El torso y el cuello se regeneraron tras la corrección final de la tapeta; manga y flexión se regeneraron después del último ajuste de la venda. El pantalón y la espalda no cambiaron de geometría ni material durante esos ajustes finales.

La primera versión de los pliegues de las piernas se descartó porque formaba anillos regulares. La versión revisada tiene inclinación, ancho y extensión distintos entre arrugas. La vista de flexión permite comprobar que los pliegues acompañan a la prenda y que codo y rodilla permanecen cerrados en la postura probada. Esto no sustituye las pruebas ampliadas de rig y caminata de fases 7 y 9.

La imagen venda_diagnostico_geometria.png emplea colores planos (venda naranja, camisa verde), sin texturas ni sombras, para confirmar que los cortes detectados eran cruces geométricos y comprobar su corrección.

## Auditoría técnica

- 12.870 vértices y 24.621 triángulos, sin incrementos.
- 44 mallas, cinco materiales y 14 imágenes utilizadas, todas empaquetadas.
- 52 huesos; pesos normalizados y máximo cuatro influencias.
- UV, topología y pesos conservados respecto a la fase 2.
- Ocho mallas con cambios de coordenadas: camisa, pantalón, tapeta, cuatro bolsillos y venda derecha. Las otras 36 mallas mantienen su geometría.
- Rig guardado en reposo; los renders de flexión no se guardaron como pose del archivo de entrega.

Los puntos de control de geometría y autoría se sincronizaron con las últimas correcciones de tapeta y venda. La fuente anterior sigue recuperable en 02_anatomia y en los respaldos de Blender.

Pendientes dentro del objetivo completo: botas (fase 4), desgaste localizado e identidad (fase 5), biblioteca y anclajes (fase 6), rig (fase 7), optimización y materiales finales (fase 8), revisión global (fase 9). El exceso respecto al presupuesto de 20.000 triángulos no está resuelto todavía.
