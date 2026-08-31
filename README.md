# Siniestralidad y Accidentes de Tránsito en Chile

Visualización de datos de accidentes viales por región. Proyecto del curso **EIN092B – Visualización Profesor Jesús A. Parra**, UTFSM.

## Equipo

-Gonzalo Quiroga
-Bastian Quijanes
## Descripción

Chile presenta una alta tasa de accidentes de tránsito, pero su distribución y gravedad no es homogénea entre regiones. Este proyecto busca entender dónde, cuándo y por qué ocurren los accidentes más graves, para apoyar la focalización de campañas de concientización, la mejora de infraestructura crítica y la optimización de controles policiales.

**Pregunta principal:** ¿Cómo varía la frecuencia y gravedad (lesionados y fallecidos) de los accidentes de tránsito a través de las diferentes regiones de Chile, y de qué manera estas cifras son impactadas por la estacionalidad y sus principales causas?

## Alcance

**Dentro del alcance**
- Fenómeno: frecuencia de siniestros, víctimas fatales y lesionados.
- Unidad de observación: registros y partes policiales de accidentes.
- Población: las 16 regiones de Chile.
- Periodo: 2019–2023.

**Fuera de alcance (por ahora)**
- Modelamiento predictivo o de machine learning.
- Análisis a nivel de calle o intersección específica.
- Estimación de costos económicos o daños materiales.
- Dashboard final terminado

## Estructura de la pregunta (X, Y, T)

| | Variables |
|---|---|
| **X** — Información disponible | Región / comuna, causa basal del accidente (velocidad, alcohol, etc.), tipo de accidente (colisión, atropello, volcamiento), tipo de zona (urbana/rural) |
| **Y** — Objetivo | Cantidad total de accidentes, cantidad de víctimas fatales, cantidad de lesionados (graves, menos graves, leves) |
| **T** — Contexto temporal | Evolución anual (2019–2023), comparación por meses, días de la semana y horas del día |

**Síntesis:** ¿Cómo se relacionan las causas, ubicación geográfica y zona (X) con la frecuencia y gravedad de los siniestros (Y) a lo largo del tiempo (T)?

## Fuente de datos

- **CONASET** y **Observatorio de Seguridad Vial** (Datos Abiertos de Carabineros de Chile).
- Unidad de observación: siniestros agregados o individuales anonimizados.
- Atributos principales: ubicación, temporalidad exacta, causa basal y recuento de víctimas.
