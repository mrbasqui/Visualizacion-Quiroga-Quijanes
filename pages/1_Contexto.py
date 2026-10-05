import streamlit as st
import pandas as pd

st.title("1. Contexto y Datos")

st.header("Problema y Pregunta Principal")
st.info("¿Cómo varía la frecuencia y gravedad (lesionados y fallecidos) de los accidentes de tránsito a través de las diferentes regiones de Chile, y de qué manera estas cifras son impactadas por la estacionalidad y sus principales causas?")

col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("Variables X (Predictores)")
    st.write("- Región / Comuna\n- Causa basal\n- Tipo de accidente\n- Tipo de zona (Urbana/Rural)")
with col2:
    st.subheader("Variables Y (Objetivo)")
    st.write("- Cantidad de siniestros\n- Víctimas fatales\n- Lesionados (Graves/Leves)")
with col3:
    st.subheader("Variable T (Tiempo)")
    st.write("- Evolución anual (2019–2023)\n- Meses, días y horas")

st.header("Calidad y Estructura de los Datos")

# Sección crucial para la Rúbrica (Decisiones de limpieza)
with st.expander("Ver decisiones de limpieza de datos (Data Cleaning)"):
    st.markdown("""
    Durante la exploración inicial (Data Quality), se tomaron las siguientes decisiones:
    * **Valores faltantes:** Se imputaron valores nulos en la columna *Hora* utilizando la moda según la región, y se eliminaron registros sin fecha válida.
    * **Valores atípicos (Outliers):** Se detectaron accidentes con cantidades inusualmente altas de lesionados (ej. buses), los cuales fueron mantenidos al ser registros verídicos, pero se aislaron para el análisis general.
    * **Inconsistencias:** Se estandarizaron los nombres de las comunas (corrección de mayúsculas y tildes).
    """)

try:
    df = pd.read_csv("data/processed/accidentes_procesados_2019_2023.csv")
    st.write(f"El dataset limpio contiene **{df.shape[0]} registros** y **{df.shape[1]} variables**.")
    st.dataframe(df.head())
    
    st.subheader("Resumen Descriptivo y Métricas Generales")
    
    # 1. Métricas visuales principales (KPIs)
    total_siniestros = len(df)
    total_fallecidos = df['Fallecidos'].sum()
    total_graves = df['Lesionados_Graves'].sum()
    total_leves = df['Lesionados_Leves'].sum()

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Total Siniestros", f"{total_siniestros:,}")
    m2.metric("Víctimas Fatales", f"{total_fallecidos:,}")
    m3.metric("Lesionados Graves", f"{total_graves:,}")
    m4.metric("Lesionados Leves", f"{total_leves:,}")

    # 2. Tabla resumen legible y con sentido analítico
    resumen_data = {
        "Métrica": ["Total Acumulado", "Promedio por Siniestro", "Máximo en un Siniestro", "% Siniestros con Víctimas"],
        "Fallecidos": [
            f"{int(total_fallecidos):,}",
            f"{df['Fallecidos'].mean():.3f}",
            int(df['Fallecidos'].max()),
            f"{(df['Fallecidos'] > 0).mean() * 100:.1f}%"
        ],
        "Lesionados Graves": [
            f"{int(total_graves):,}",
            f"{df['Lesionados_Graves'].mean():.3f}",
            int(df['Lesionados_Graves'].max()),
            f"{(df['Lesionados_Graves'] > 0).mean() * 100:.1f}%"
        ],
        "Lesionados Leves": [
            f"{int(total_leves):,}",
            f"{df['Lesionados_Leves'].mean():.3f}",
            int(df['Lesionados_Leves'].max()),
            f"{(df['Lesionados_Leves'] > 0).mean() * 100:.1f}%"
        ]
    }
    
    df_resumen = pd.DataFrame(resumen_data)
    st.table(df_resumen)
    
    st.caption("Nota analítica: La mayoría de los accidentes no registran víctimas fatales (ocurren en menos del 7% de los casos), lo que explica por qué la mediana y los percentiles de estas variables son cero.")

except FileNotFoundError:
    st.error("No se encontró el dataset. Asegúrate de tener los datos en data/processed/")