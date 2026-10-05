import streamlit as st
import pandas as pd
import plotly.express as px

st.title("3. Análisis de la Pregunta")
st.markdown("¿Cómo se relacionan las causas, ubicación y zona (X) con la gravedad de los siniestros (Y) a lo largo del tiempo (T)?")

@st.cache_data
def load_data():
    df = pd.read_csv("data/processed/accidentes_procesados_2019_2023.csv")
    df['Fecha_Hora'] = pd.to_datetime(df['Fecha_Hora'])
    df['Año'] = df['Fecha_Hora'].dt.year
    df['Mes'] = df['Fecha_Hora'].dt.month
    df['Dia_Semana'] = df['Fecha_Hora'].dt.day_name()
    df['Hora'] = df['Fecha_Hora'].dt.hour
    return df

df = load_data()

st.subheader("4. Evolución Temporal (Componente T)")

# Control interactivo exigido en la Rúbrica (Selección de Métricas)
metrica = st.radio("Selecciona la métrica de gravedad (Y) a visualizar:", ('Fallecidos', 'Lesionados_Graves', 'Total_Siniestros'))

# Preparar datos corrigiendo el formato de fecha para la agregación
df_tiempo = df.groupby(['Año', 'Mes']).agg({
    'Fallecidos': 'sum', 
    'Lesionados_Graves': 'sum',
    'Total_Siniestros': 'count'
}).reset_index()

df_tiempo['Fecha'] = pd.to_datetime(
    df_tiempo[['Año', 'Mes']].rename(columns={'Año': 'year', 'Mes': 'month'}).assign(day=1)
)

fig4 = px.line(df_tiempo, x='Fecha', y=metrica, markers=True, 
               title=f"Tendencia Mensual de {metrica.replace('_', ' ')} (2019-2023)",
               labels={metrica: f'Cantidad de {metrica.replace("_", " ")}', 'Fecha': 'Mes y Año'})
st.plotly_chart(fig4, use_container_width=True)
st.caption(f"Interpretación: Permite observar fluctuaciones atípicas (como la baja drástica de movilidad en cuarentenas de 2020) y peaks estacionales.")

st.subheader("5. Riesgo Temporal Acumulado (Mapa de Calor T vs Y)")
heatmap_data = df.groupby(['Dia_Semana', 'Hora'])['Total_Siniestros'].count().reset_index()
orden_dias = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

fig5 = px.density_heatmap(heatmap_data, x='Hora', y='Dia_Semana', z='Total_Siniestros', 
                          category_orders={'Dia_Semana': orden_dias}, title="Concentración de Accidentes por Día y Hora",
                          color_continuous_scale='Viridis',
                          labels={'Hora': 'Hora del Día', 'Dia_Semana': 'Día de la Semana', 'Total_Siniestros': 'N° Siniestros'})
st.plotly_chart(fig5, use_container_width=True)
st.caption("Interpretación: El análisis conjunto muestra claramente los 'puntos calientes' de riesgo: horas punta de tarde en días hábiles y madrugadas de fines de semana.")

st.subheader("Conclusiones y Conexión con la Pregunta")
st.success('''
* **Variable Y (Gravedad) vs X (Ubicación/Zona):** Si bien las áreas urbanas agrupan la mayoría de los eventos, la gravedad (letalidad) muestra una fuerte dependencia hacia vías rápidas y sectores rurales.
* **Impacto Estacional (T):** La estacionalidad horaria y mensual condiciona drásticamente la frecuencia de accidentes, respondiendo parcialmente a la pregunta inicial.
* **Siguientes pasos:** Para la entrega final, calcularemos tasas relativas cruzando estos datos con población para verificar el nivel de riesgo real de cada región, no solo el volumen absoluto.
''')