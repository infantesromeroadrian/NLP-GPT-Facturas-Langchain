# app.py

import streamlit as st
import os
import tempfile
import json
from procesador_pdf import ProcesadorPDF
from separador_texto import SeparadorTexto
from buscador_documentos import BuscadorDocumentos
from procesador_qa import ProcesadorQA


# Función auxiliar para cargar la clave API de un archivo de configuración
def cargar_clave_api(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        for linea in archivo:
            if 'OPENAI_API_KEY' in linea:
                return linea.strip().split('=')[1]
    return None


# Cargar la clave API desde un archivo de configuración oculto
ruta_archivo_config = '/Users/adrianinfantes/Desktop/AIR/CollegeStudies/MachineLearningPath/Portfolio/NlpProjects/DecideSoluciones/py/.openai_api_key'
api_key = cargar_clave_api(ruta_archivo_config)

if api_key:
    os.environ['OPENAI_API_KEY'] = api_key
else:
    st.error(
        "No se encontró la clave API de OpenAI. Asegúrate de que el archivo de configuración esté presente y correctamente formateado.")
    st.stop()

st.title('Asistente de Análisis de PDF con QA')

with st.sidebar:
    st.header("Acerca de")
    st.write(
        "Esta herramienta utiliza modelos de lenguaje NLP para responder preguntas basadas en el contenido de documentos PDF.")

uploaded_file = st.file_uploader("Sube tu archivo PDF aquí:", type="pdf")
if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        pdf_path = tmp_file.name

    st.write("Procesando PDF...")
    procesador_pdf = ProcesadorPDF(pdf_path)
    texto_pdf = procesador_pdf.extraer_texto()
    if texto_pdf:
        st.success("PDF procesado correctamente.")

        separador = SeparadorTexto()
        segmentos_texto = separador.dividir_texto(texto_pdf)

        buscador = BuscadorDocumentos()
        buscador.inicializar_busqueda(segmentos_texto)
        procesador_qa = ProcesadorQA(buscador)

        pregunta = st.text_input("Escribe tu pregunta aquí:")
        boton_pregunta = st.button("Enviar Pregunta")

        if boton_pregunta and pregunta:
            st.write("Buscando respuesta...")
            resultado_qa = procesador_qa.ejecutar_qa(
                pregunta)  # Asegúrate de que `ejecutar_qa` no espera el argumento `temperatura`
            if resultado_qa:
                st.markdown(f"**Respuesta:** {resultado_qa}")

                # Aquí añadimos la capacidad de guardar la pregunta y respuesta en JSON
                respuestas_dict = {pregunta: resultado_qa}
                with open("respuestas.json", "w") as f:
                    json.dump(respuestas_dict, f, ensure_ascii=False, indent=4)
                st.success("Respuesta guardada en 'respuestas.json'.")
            else:
                st.error("No se pudo obtener una respuesta para tu pregunta.")
    else:
        st.error("No se pudo procesar el PDF.")
        st.stop()
