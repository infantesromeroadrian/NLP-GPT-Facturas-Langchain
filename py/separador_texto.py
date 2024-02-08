# separador_texto.py

from langchain.text_splitter import CharacterTextSplitter
import logging


class SeparadorTexto:
    def __init__(self, separator=".", chunk_size=1000, chunk_overlap=200):
        self.text_splitter = CharacterTextSplitter(
            separator=separator,
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len,
        )

    def dividir_texto(self, texto):
        try:
            texts = self.text_splitter.split_text(texto)
            logging.info(f"Texto dividido en {len(texts)} segmentos.")
            return texts
        except Exception as e:
            logging.error(f"Error al dividir texto: {e}")
            return []
