"""Streamlit: muestra las dos pantallas holográficas (Antioquia + Colombia)
con hojas de cálculo animadas. Reutiliza el index.html de esta misma carpeta.

Ejecutar:  streamlit run app.py
"""
import json
import pathlib

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Centro de Análisis Territorial", layout="wide")
st.markdown(
    "<style>.block-container{padding-top:1rem;padding-bottom:0.5rem}"
    "header[data-testid='stHeader']{display:none}</style>",
    unsafe_allow_html=True,
)

with st.sidebar:
    st.header("Controles")
    speed = st.slider("Velocidad de desplazamiento", 0.2, 3.0, 1.0, 0.1)
    rate = st.slider("Frecuencia de cálculo", 0.2, 3.0, 1.0, 0.1)
    alto = st.slider("Alto de la escena (px)", 600, 1100, 800, 10)

html = pathlib.Path(__file__).with_name("index.html").read_text(encoding="utf-8")
cfg = "<script>window.__CFG__=" + json.dumps({"speed": speed, "rate": rate}) + "</script>"
html = html.replace("<!--CFG-->", cfg)

components.html(html, height=alto, scrolling=False)
st.caption("Diseño Vibe Coding por Ing. Hernán Quiroz")
