# app.py

import streamlit as st
import os
import tempfile
from procesador_pdf import ProcesadorPDF
from separador_texto import SeparadorTexto
from buscador_documentos import BuscadorDocumentos
from procesador_qa import ProcesadorQA

# Título y descripción
st.title('Asistente de Análisis de PDF con QA')
st.markdown("""
Esta aplicación permite cargar archivos PDF para luego realizar preguntas específicas sobre su contenido.
""")

# Sidebar - Configuración y Acerca de
with st.sidebar:
    st.header("Acerca de")
    st.write("""
    Esta herramienta utiliza modelos de lenguaje NLP mediante LangChain para responder preguntas basadas en el contenido de documentos PDF.
    """)
    st.header("Configuración")
    temperatura = st.slider("Ajuste de temperatura", min_value=0.0, max_value=1.0, value=0.5, help="Ajusta la 'temperatura' para las predicciones del modelo.")

# Subida del archivo PDF
uploaded_file = st.file_uploader("Sube tu archivo PDF aquí:", type="pdf")
if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        pdf_path = tmp_file.name

    # Procesar PDF
    st.write("Procesando PDF...")
    procesador_pdf = ProcesadorPDF(pdf_path)
    texto_pdf = procesador_pdf.extraer_texto()
    if texto_pdf:
        st.success("PDF procesado correctamente.")
    else:
        st.error("No se pudo procesar el PDF.")
        st.stop()

    # Dividir texto
    separador = SeparadorTexto()
    segmentos_texto = separador.dividir_texto(texto_pdf)

    # Inicializar buscador de documentos y Procesador QA
    buscador = BuscadorDocumentos()
    buscador.inicializar_busqueda(segmentos_texto)
    procesador_qa = ProcesadorQA(buscador)

    # Sección de preguntas
    st.header("Haz una pregunta sobre el PDF")
    pregunta = st.text_input("Escribe tu pregunta aquí:")
    boton_pregunta = st.button("Enviar Pregunta")

    if boton_pregunta and pregunta:
        st.write("Buscando respuesta...")
        resultado_qa = procesador_qa.ejecutar_qa(pregunta)
        if resultado_qa:
            st.markdown(f"**Respuesta:** {resultado_qa}")
        else:
            st.error("No se pudo obtener una respuesta para tu pregunta.")

    # Opción para visualizar el texto completo del PDF (opcional)
    if st.checkbox('Mostrar texto completo del PDF'):
        st.subheader("Texto Completo del PDF")
        st.write(texto_pdf)