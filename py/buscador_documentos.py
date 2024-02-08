# buscador_documentos.py

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
import logging


class BuscadorDocumentos:
    def __init__(self):
        self.embeddings = OpenAIEmbeddings()
        self.docsearch = None

    def inicializar_busqueda(self, texts):
        try:
            self.docsearch = FAISS.from_texts(texts, self.embeddings)
            logging.info("Motor de búsqueda FAISS inicializado con éxito.")
        except Exception as e:
            logging.error(f"Error al inicializar FAISS: {e}")
            self.docsearch = None

    def buscar(self, query, top_n=5, search_type='similarity'):
        if not self.docsearch:
            logging.error("Motor de búsqueda FAISS no inicializado.")
            return []
        try:
            resultados = self.docsearch.search(query, top_n=top_n, search_type=search_type)
            logging.info(f"Búsqueda realizada con éxito. {len(resultados)} resultados encontrados.")
            return resultados
        except Exception as e:
            logging.error(f"Error durante la búsqueda: {e}")
            return []

