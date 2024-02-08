# procesador_qa.py

from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
import logging


class ProcesadorQA:
    def __init__(self, buscador_documentos):
        self.buscador_documentos = buscador_documentos
        self.chain = load_qa_chain(OpenAI(), chain_type="stuff")

    def ejecutar_qa(self, query):
        try:
            docs = self.buscador_documentos.docsearch.similarity_search(query)
            resultado = self.chain.run(question=query, input_documents=docs)
            logging.info("Consulta de QA ejecutada con éxito.")
            return resultado
        except Exception as e:
            logging.error(f"Error al ejecutar la consulta de QA: {e}")
            return None
