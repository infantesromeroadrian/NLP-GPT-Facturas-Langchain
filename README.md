# Proyecto de Análisis de PDF con Preguntas y Respuestas

Este proyecto permite a los usuarios cargar documentos PDF y realizar preguntas específicas sobre su contenido, utilizando tecnologías avanzadas de procesamiento de lenguaje natural proporcionadas por LangChain y OpenAI.

## Características

- Extracción de texto de documentos PDF.
- División de texto en segmentos manejables.
- Búsqueda semántica en segmentos de texto utilizando FAISS.
- Generación de respuestas a preguntas utilizando modelos de lenguaje de OpenAI.

## Tecnologías Utilizadas

- Python
- Streamlit
- LangChain
- OpenAI GPT
- PyPDF2
- FAISS

## Estructura del Proyecto

El proyecto está organizado en varios scripts de Python, cada uno manejando una parte específica del flujo de trabajo:

- `procesador_pdf.py`: Extrae texto de documentos PDF.
- `separador_texto.py`: Divide el texto en segmentos.
- `buscador_documentos.py`: Indexa los segmentos de texto y permite búsquedas semánticas.
- `procesador_qa.py`: Responde a preguntas basadas en el texto.
- `app.py`: Interfaz de usuario de Streamlit para interactuar con el proyecto.

## Instalación

Para ejecutar este proyecto, necesitarás Python 3.6 o superior y pip. Sigue estos pasos para configurar tu entorno:

1. Clona este repositorio:

```bash
git clone https://NLP-LangChain-Facturas.git
cd tu-repositorio

```

2. Instala las dependencias:

```bash

poetry install
```

3. Configuración
- Antes de lanzar la aplicación, necesitas configurar tu clave API de OpenAI. Sigue estos pasos para hacerlo de manera segura:
- Crea un archivo oculto .openai_api_key en tu directorio home con tu clave API de OpenAI:

```bash

 echo "OPENAI_API_KEY=tu_clave_api_aquí" > ~/.openai_api_key
``` 

- Asegúrate de que tu aplicación app.py esté configurada para leer esta clave desde el archivo .openai_api_key.

## Ejecución
Para lanzar la aplicación de Streamlit, ejecuta el siguiente comando desde el directorio del proyecto:

```bash
streamlit run app.py
```

## Licencia
[MIT License](


## Contribuciones
Las contribuciones son bienvenidas. Por favor, envía un pull request o abre un issue para discutir los cambios propuestos o las adiciones.