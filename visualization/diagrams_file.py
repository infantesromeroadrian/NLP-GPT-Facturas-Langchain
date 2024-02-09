from diagrams import Diagram, Edge
from diagrams.generic.device import Mobile
from diagrams.generic.network import Router
from diagrams.generic.storage import Storage
from diagrams.onprem.compute import Server
from diagrams.programming.framework import Spring

with Diagram("Arquitectura Estilo IoT del Sistema de QA PDF", show=False, direction="TB"):

    user = Mobile("Usuario")
    app = Router("App Streamlit")
    pdf_processor = Server("Procesador PDF")
    text_splitter = Server("Separador de Texto")
    doc_search = Spring("Buscador Documentos")
    faiss_db = Storage("FAISS DB")
    qa_processor = Server("Procesador QA")
    model = Server("Modelo OpenAI")

    user - Edge(color="darkgreen", style="dashed") >> app
    app - Edge(color="darkorange") >> pdf_processor >> text_splitter >> doc_search
    doc_search - Edge(color="red") >> faiss_db
    doc_search - Edge(color="blue") >> qa_processor >> model
    model - Edge(color="darkgreen", style="dashed") >> app
    app - Edge(color="darkgreen", style="dashed") >> user
