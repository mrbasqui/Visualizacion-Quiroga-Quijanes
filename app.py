import streamlit as st

st.set_page_config(page_title="Siniestralidad Vial Chile", page_icon="🚗", layout="wide")

st.title("🚗 Siniestralidad y Accidentes de Tránsito en Chile")
st.sidebar.success("Selecciona una página arriba para explorar el análisis.")

st.markdown('''
Bienvenido a la aplicación interactiva del proyecto de visualización sobre siniestros viales en Chile. 
Utiliza el menú lateral para navegar por las siguientes secciones:

- **1. Contexto y Datos:** Describe la problemática, alcance y estructura del dataset utilizado.
- **2. Análisis Exploratorio (EDA):** Explora cómo se comportan los datos, sus distribuciones y variables principales.
- **3. Análisis de la Pregunta:** Conecta los hallazgos con la pregunta principal del proyecto mediante visualizaciones de relación y temporalidad.
''')
