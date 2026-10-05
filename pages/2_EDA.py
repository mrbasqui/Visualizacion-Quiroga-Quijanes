import streamlit as st
import pandas as pd
import plotly.express as px

st.title("2. Análisis Exploratorio de Datos (EDA)")

@st.cache_data
def load_data():
    df = pd.read_csv("data/processed/accidentes_procesados_2019_2023.csv")
    df['Fecha_Hora'] = pd.to_datetime(df['Fecha_Hora'])
    return df

df = load_data()

st.sidebar.header("Filtros Interactivos")
zona_filtro = st.sidebar.multiselect("Filtrar por Zona (Urbana/Rural)", options=df['Zona'].unique(), default=df['Zona'].unique())
regiones_disponibles = df['Region'].unique()
region_filtro = st.sidebar.multiselect("Filtrar por Región", options=regiones_disponibles, default=regiones_disponibles)

# Aplicar filtros
df_filtrado = df[(df['Zona'].isin(zona_filtro)) & (df['Region'].isin(region_filtro))]

st.header("Análisis Univariado")

col1, col2 = st.columns(2)
with col1:
    st.subheader("1. Frecuencia de Siniestros por Región")
    siniestros_region = df_filtrado['Region'].value_counts().reset_index()
    siniestros_region.columns = ['Region', 'Cantidad']
    fig1 = px.bar(siniestros_region, x='Cantidad', y='Region', orientation='h', 
                  title="Total Siniestros por Región", color='Cantidad', 
                  color_continuous_scale='Reds', labels={'Cantidad': 'N° de Siniestros', 'Region': 'Región'})
    fig1.update_layout(yaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig1, use_container_width=True)
    st.caption("Interpretación: La Región Metropolitana concentra el mayor volumen absoluto de accidentes, correlacionado directamente con su densidad poblacional.")

with col2:
    st.subheader("2. Distribución de Causas Basales")
    causas = df_filtrado['Causa_Basal'].value_counts().reset_index()
    causas.columns = ['Causa', 'Cantidad']
    fig2 = px.pie(causas, values='Cantidad', names='Causa', hole=0.4, title="Proporción de Causas Basales")
    fig2.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig2, use_container_width=True)
    st.caption("Interpretación: Conducir no atento a las condiciones del tránsito y pérdida de control son los principales gatillantes (variable X).")

st.subheader("3. Severidad y Víctimas (Y) según Tipo de Accidente")

# Agrupar métricas de gravedad por tipo de accidente
df_severidad = df_filtrado.groupby('Tipo_Accidente').agg({
    'Total_Siniestros': 'count',
    'Fallecidos': 'sum',
    'Lesionados_Graves': 'sum'
}).reset_index()

# Calcular la tasa de lesionados graves por cada 100 accidentes
df_severidad['Tasa_Graves'] = (df_severidad['Lesionados_Graves'] / df_severidad['Total_Siniestros']) * 100

fig3 = px.bar(
    df_severidad.sort_values(by='Tasa_Graves', ascending=False),
    x='Tipo_Accidente',
    y='Tasa_Graves',
    color='Tasa_Graves',
    color_continuous_scale='Oranges',
    title="Tasa de Lesionados Graves por cada 100 Siniestros (según Tipo)",
    labels={'Tipo_Accidente': 'Tipo de Accidente', 'Tasa_Graves': 'Lesionados Graves / 100 Siniestros'},
    text_auto='.1f'
)
st.plotly_chart(fig3, use_container_width=True)
st.caption(
    "Interpretación: Al normalizar la gravedad, se observa que siniestros como el Atropello presentan "
    "una tasa significativamente mayor de lesionados graves en comparación con colisiones o choques menores."
)