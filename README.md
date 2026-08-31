# Siniestralidad y Accidentes de Tránsito en Chile

Visualización de datos de accidentes viales por región. Proyecto del curso **EIN092B – Visualización Profesor Jesús A. Parra**, UTFSM.

## Equipo

- Gonzalo Quiroga
- Bastian Quijanes
  
## Descripción

Chile presenta una alta tasa de accidentes de tránsito, pero su distribución y gravedad no es homogénea entre regiones. Este proyecto busca entender dónde, cuándo y por qué ocurren los accidentes más graves, para apoyar la focalización de campañas de concientización, la mejora de infraestructura crítica y la optimización de controles policiales.

## Motivación

Detrás de cada cifra de siniestralidad hay una historia real: una familia, un trayecto cotidiano, una vida que se ve afectada en cuestión de segundos. En Chile, miles de personas mueren o resultan gravemente heridas cada año en accidentes de tránsito, muchos de ellos evitables, y sin embargo tendemos a hablar de estas cifras como algo distante o inevitable.

Elegimos este tema porque los datos para entender el problema existen —Carabineros y CONASET los registran de forma sistemática—, pero hoy están dispersos y son difíciles de interpretar para quienes podrían actuar con ellos: autoridades que deciden dónde reforzar la fiscalización, municipios que priorizan mejoras en infraestructura, y ciudadanos que quieren saber si las rutas que usan a diario son seguras.

Creemos que visualizar esta información de forma clara puede ayudar a transformar datos en decisiones concretas: campañas dirigidas a las causas que más pesan, controles en los horarios y zonas de mayor riesgo, y una mejor comprensión pública de un problema que nos afecta a todos como país.

## Pregunta principal
¿Cómo varía la frecuencia y gravedad (lesionados y fallecidos) de los accidentes de tránsito a través de las diferentes regiones de Chile, y de qué manera estas cifras son impactadas por la estacionalidad y sus principales causas?

## Alcance

**Dentro del alcance**
- Fenómeno: frecuencia de siniestros, víctimas fatales y lesionados.
- Unidad de observación: registros y partes policiales de accidentes.
- Población: las 16 regiones de Chile.
- Periodo: 2019–2023.

**Fuera de alcance**
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

## Descripcion de los datos

Qué representa una observación: cada fila corresponde a un siniestro de tránsito registrado mediante parte policial, ya sea como evento individual o agregado por región/comuna, según la fuente.

Variables principales: fecha y hora del siniestro, región y comuna, tipo de accidente (colisión, atropello, volcamiento, etc.), causa basal (velocidad, alcohol, imprudencia, etc.), tipo de zona (urbana/rural), y el recuento de víctimas (fallecidos, lesionados graves, menos graves y leves).

Cobertura temporal: registros desde 2019 hasta 2023, lo que permite observar evolución anual, así como patrones por mes, día de la semana y hora del día.

Cobertura espacial: las 16 regiones de Chile, con desagregación disponible a nivel de comuna según la fuente.

Historia que se busca explorar: identificar patrones estacionales (por ejemplo, peaks en Fiestas Patrias o recambios de verano), comparar regiones según volumen total de accidentes frente a aquellas con mayor proporción de letalidad, y visibilizar los horarios y causas de mayor riesgo en las rutas del país.

## Estructura del repositorio

```
proyecto-visualizacion/
├── data/
│   ├── raw/                                  
│   └── processed/                            
├── notebooks/
│   └── 01_exploracion_siniestralidad.ipynb   
├── src/                                       
├── figures/                                   
├── app/                                       
├── README.md
└── .gitignore
```
