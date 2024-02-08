# main.py

import os
from configuracion_logging import logging
from procesador_pdf import ProcesadorPDF
from separador_texto import SeparadorTexto
from buscador_documentos import BuscadorDocumentos
from procesador_qa import ProcesadorQA

def cargar_clave_api(ruta_archivo):
    """Carga la clave API de OpenAI desde un archivo de configuración."""
    with open(ruta_archivo, 'r') as archivo:
        for linea in archivo:
            if 'OPENAI_API_KEY' in linea:
                # Asume el formato: OPENAI_API_KEY=clave_api
                return linea.strip().split('=')[1]
    return None

# Ruta al archivo de configuración oculto
ruta_archivo_config = os.path.join(os.path.expanduser('~'), '/Users/adrianinfantes/Desktop/AIR/CollegeStudies/MachineLearningPath/Portfolio/NlpProjects/DecideSoluciones/py/.openai_api_key')
api_key = cargar_clave_api(ruta_archivo_config)

if not api_key:
    logging.error("No se encontró la clave API de OpenAI. Asegúrate de que el archivo de configuración esté presente y correctamente formateado.")
    exit()

# Configurar la clave API en el entorno
os.environ['OPENAI_API_KEY'] = api_key

# Ruta al archivo PDF que deseas procesar
pdf_path = '/Users/adrianinfantes/Desktop/AIR/CollegeStudies/MachineLearningPath/Portfolio/NlpProjects/DecideSoluciones/data/training/factura_0.pdf'

# Procesar PDF
procesador_pdf = ProcesadorPDF(pdf_path)
texto_pdf = procesador_pdf.extraer_texto()
if texto_pdf:
    logging.info("Extracción de texto PDF completada.")
else:
    logging.error("Falló la extracción de texto del PDF.")
    exit()

# Dividir texto
separador = SeparadorTexto()
segmentos_texto = separador.dividir_texto(texto_pdf)
if segmentos_texto:
    logging.info("División de texto completada.")
else:
    logging.error("Falló la división de texto.")
    exit()

# Inicializar buscador de documentos
buscador = BuscadorDocumentos()
buscador.inicializar_busqueda(segmentos_texto)

# Realizar consultas de QA
procesador_qa = ProcesadorQA(buscador)

# Define tus consultas aquí
consultas = [
    "¿Cuál es el total de la factura?",
    "¿Cuál es la empresa que emite la factura?",
    "Haz un resumen completo de la factura."
]

# Ejecutar consultas de QA
for consulta in consultas:
    resultado_qa = procesador_qa.ejecutar_qa(consulta)
    if resultado_qa:
        print(f"Resultado de '{consulta}': {resultado_qa}")
    else:
        print(f"No se pudo ejecutar la consulta de QA para: '{consulta}'")
