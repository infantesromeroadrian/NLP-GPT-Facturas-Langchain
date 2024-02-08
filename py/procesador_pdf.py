# procesador_pdf.py

from PyPDF2 import PdfReader
import logging


class ProcesadorPDF:
    def __init__(self, ruta_archivo):
        self.ruta_archivo = ruta_archivo

    def extraer_texto(self):
        try:
            reader = PdfReader(self.ruta_archivo)
            raw_text = ""
            for page in reader.pages:
                raw_text += page.extract_text() or ""
            logging.info("Texto extraído del PDF con éxito.")
            return raw_text
        except Exception as e:
            logging.error(f"Error al extraer texto del PDF: {e}")
            return None
