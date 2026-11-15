# Fase 5: identidad y desgaste

Punto de control actual: 05_Desgaste.blend. Los originales de fase 4 y el respaldo anterior a corregir cintura siguen recuperables.

## Identidad y uso

La facción es completamente ficticia: **Vigías del Umbral**. La marca original combina un arco abierto y tres trazos verticales de distinta altura. Está pintada en ocre apagado en el frente del casco y presenta pérdidas de pintura; no se añadieron símbolos de unidades históricas.

El casco conserva su reparación de chapa remachada. Se añadieron deformaciones pequeñas de hasta 1,38 mm en la calota, pintura oliva mate y desgaste concentrado en borde y arañazos específicos del frente. La primera marca era demasiado limpia y el arañazo demasiado continuo: se redujeron y fragmentaron antes del horneado final.

Las máscaras de suciedad siguen zonas de contacto: codos, puños, rodillas, bajos de pantalón, fondo de bolsas, zona de hebillas, parte baja de mochila y funda de cantimplora. Hay decoloración discreta en hombros y bordes de bolsillos, cuero desgastado de cinturón y polvo en la parte baja de las botas. Las hebillas tienen pátina localizada; la distribución no es una capa de suciedad uniforme sobre todo el personaje. Los tirantes recibieron deformaciones inferiores a 0,8 mm.

Se añadieron dos remiendos de sarga recuperada, en codo derecho y rodilla izquierda, con color ligeramente distinto y pespunte perimetral. Son objetos independientes, con origen de montaje en la costura superior, y deberán incorporarse a los maestros de la fase 6. No se añadieron nuevos objetos de carga.

## Correcciones e inspección

El primer remiendo de rodilla, construido como una cuadrícula proyectada, era atravesado por los pliegues del pantalón. Se descartó. Los remiendos finales se obtienen recortando una copia de la superficie real de cada prenda, conservan sus pliegues y pesos interpolados y añaden una separación pequeña y espesor de tela. Se inspeccionaron en rodilla.png, codo.png, rodilla_flexion.png y codo_flexion.png: en las posturas revisadas ya no aparecen los cortes triangulares del primer intento.

Durante la prueba se descubrió que el signo de la flexión de rodilla de los ensayos anteriores era inverso al anatómico. Se corrigió: el muslo gira hacia delante y la pantorrilla hacia atrás. Se comprobó la orientación con las posiciones reales de los tres segmentos del esqueleto. Las imágenes antiguas de sobreextensión no se usan como prueba de animación válida.

Se repitieron las pruebas sobre los checkpoints anteriores sin modificar sus archivos nativos:

- Fase 2: codos_rodilla_anatomicos.png, flexion_pelvis_anatomica.png y rodillas_flexion_anatomica.png.
- Fase 3: pliegues_flexion_anatomica.png.
- Fase 4: flexion_anatomica.png.

Estas imágenes se inspeccionaron y mostraron otro defecto: el faldón anterior se arrugaba en triángulos al agacharse. En el checkpoint actual se regularizó el reparto pelvis/muslo en la camisa y se transfirieron esos pesos por proximidad a triángulos e interpolación baricéntrica a tapeta, botones y bolsillos cosidos. La primera corrección independiente de cada accesorio dejaba una punta larga en la tapeta; se sustituyó por la transferencia desde la camisa. El resultado final se revisó en agachado_revision.png y faldon_flexion.png, con el faldón continuo y los accesorios siguiendo la prenda.

Se inspeccionaron también casco.png, uniforme.png, equipo.png, conjunto.png y espalda.png para verificar pintura, materiales, desgaste y lectura global. Las vistas de reposo conservan su validez tras el ajuste de pesos porque no se modificó geometría ni materiales con esa corrección. Las pruebas de torso/cintura corresponden al archivo corregido.

## Auditoría y límites del punto de control

- 13.523 vértices, 25.792 triángulos, 46 mallas, cinco materiales, 14 imágenes utilizadas y empaquetadas, 52 huesos.
- Geometría de 41 de las 44 mallas anteriores intacta. Solo se movieron vértices de calota y dos tirantes, más los dos remiendos nuevos.
- Pesos de siete objetos de camisa y faldón corregidos; el resto de pesos anteriores se conserva. Todos normalizados y con máximo cuatro influencias.
- UV del uniforme reorganizadas para incluir las reparaciones. Atlas de equipo y cantimplora mantienen la distribución de su fase anterior.
- Todas las mallas admiten tangentes, sin caras de área nula ni aristas con más de dos caras. Rig guardado en reposo; las poses solo se usaron para los renders.
- Geometría y autoría sincronizadas con los pesos corregidos.

La biblioteca modular todavía no incluye los remiendos ni todas las revisiones recientes: corresponde a fase 6. La revisión completa del rig, el presupuesto de triángulos y la entrega final siguen pendientes de fases 7–9. Estas pruebas estáticas no son animaciones terminadas.
