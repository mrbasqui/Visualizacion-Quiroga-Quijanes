# Siniestralidad y Accidentes de Tránsito en Chile - Avance 2

Visualización de datos de accidentes viales por región. Proyecto del curso **EIN092B – Visualización Profesor Jesús A. Parra**, UTFSM.

## Equipo
- Gonzalo Quiroga
- Bastian Quijanes

## Problema y Pregunta Principal
¿Cómo varía la frecuencia y gravedad (lesionados y fallecidos) de los accidentes de tránsito a través de las diferentes regiones de Chile, y de qué manera estas cifras son impactadas por la estacionalidad y sus principales causas?

## Dataset
- **Fuente:** CONASET y Observatorio de Seguridad Vial (Datos Abiertos de Carabineros de Chile).
- **Cobertura:** 2019-2023 en las 16 regiones de Chile.
- **Variables Principales:** Región, Comuna, Causa Basal, Zona (X), Fallecidos, Lesionados (Y), Fecha, Hora (T).

## Instrucciones de Ejecución

1. Clonar el repositorio.
2. Crear un entorno virtual e instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecutar la aplicación en Streamlit:
   ```bash
   streamlit run app.py
   ```

## Estructura de la Aplicación (Avance 2)
La aplicación cuenta con 3 páginas principales para abordar el Análisis Exploratorio de Datos (EDA):
1. **Contexto y Datos:** Describe la problemática, variables (X, Y, T) e indicadores generales.
2. **Análisis Exploratorio:** Contiene visualizaciones interactivas de la distribución de siniestros, causas y gravedad.
3. **Análisis de la Pregunta:** Relaciona las variables espaciales y temporales para responder a la pregunta original del proyecto.
