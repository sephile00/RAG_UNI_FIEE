# RAG-UNI-FIEE

Repositorio del proyecto de **Recuperación de Información Aumentada (RAG)** para la Facultad de Ingeniería Eléctrica y Electrónica de la Universidad Nacional de Ingeniería (UNI).

---
## Objetivo principal:
Facilitar los procesos largos y la difusión de reglamentos mediante un chatbot interactivo que responda de forma inmediata y precisa a las dudas más comunes de los estudiantes de la FIEE.


## 🎯 Objetivos del Proyecto

1. Brindar respuestas claras sobre reglamentos y normas académicas de la FIEE (créditos, repitencia, requisitos de egreso, etc.).
2. Facilitar el acceso a información detallada sobre los cursos (syllabus, bibliografía, contenidos).
3. Automatizar la atención de consultas frecuentes mediante IA.
4. Utilizar un modelo de lenguaje (como GPT) potenciado por recuperación de documentos oficiales (RAG).
5. Construir una herramienta útil, extensible y validada para estudiantes y docentes de la FIEE.

---

## 🤖 ¿Qué es un sistema RAG?

Un sistema de **Recuperación de Información Aumentada (RAG)** combina dos tecnologías:

- **Recuperación** de documentos relevantes (PDFs, syllabus, reglamentos).
- **Generación** de respuestas usando un modelo de lenguaje (como GPT), con base en esos documentos.

Esto permite ofrecer respuestas **confiables, actualizadas y contextualizadas**, evitando "alucinaciones" del modelo.

---

## 📌 Estado Actual del Proyecto

| Etapa | Estado |
|-------|--------|
| Recolección de reglamentos oficiales | ✅ En progreso |
| Estructura base del README.md | ✅ Listo |
| Definición de herramientas (LangChain, FAISS, etc.) | 🔄 En evaluación |
| Integración de syllabus y bibliografía | 🔜 Pendiente |
| Interfaz de usuario (web/chatbot) | 🔜 Pendiente |
| Fase de pruebas con estudiantes | 🔜 Futura |

---
## Trabajos 
https://www.edutec.es/revista/index.php/edutec-e/article/view/2971/1185
https://repositorio.uvm.edu.ve/server/api/core/bitstreams/2b68d8ed-5297-4a9c-9a20-da15347cfebe/content

## 🗂️ Estructura esperada del proyecto
RAG_UNI_FIEE/
│
├── data/                        # Datos de entrada
│   ├── raw/                    # PDFs originales
│   └── processed/              # Chunks limpios y listos
│
├── notebooks/                  # Pruebas y exploración en Jupyter
│   └── 01_exploracion.ipynb
│
├── src/                        # Código fuente principal
│   ├── ingestion/              # Carga y extracción de PDFs
│   │   └── load_documents.py
│   ├── processing/             # Limpieza, chunking, normalización
│   │   └── chunking.py
│   ├── embeddings/             # Generación de embeddings
│   │   └── generate_embeddings.py
│   ├── retriever/              # Búsqueda semántica (FAISS)
│   │   └── vector_search.py
│   ├── rag/                    # RAG: contexto + pregunta + respuesta
│   │   └── query_with_context.py
│   └── app/                    # Interfaz del usuario (Streamlit/Gradio)
│       └── interface.py
│
├── tests/                      # Pruebas unitarias
│   └── test_chunking.py
│
├── .gitignore
├── README.md
├── requirements.txt
├── LICENSE
└── retrospectiva.md            # Lecciones aprendidas por semana

## 🔁 Metodología Ágil (SCRUM adaptado)

Se usa SCRUM con sprints semanales y retrospectivas, adaptado para un equipo pequeño de desarrolladores. Cada semana tiene un objetivo técnico claro y entregable.

---

## 📅 Plan Semanal

### Semana 1:
- Estructura, carga inicial, chunking

### Semana 2:
- Embeddings y recuperación semántica

### Semana 3:
- RAG completo (pregunta + contexto + respuesta)

### Semana 4:
- Interfaz y demo funcional

---

## 🚀 Cómo ejecutar

```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar carga
python src/ingestion/load_documents.py

# Ejecutar interfaz
streamlit run src/app/interface.py



