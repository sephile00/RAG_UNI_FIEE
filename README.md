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


## 🔁 Metodología Ágil (SCRUM adaptado)

Se usa SCRUM con sprints semanales y retrospectivas, adaptado para un equipo pequeño de desarrolladores. Cada semana tiene un objetivo técnico claro y entregable.

### 🎯 ¿Por qué SCRUM?

SCRUM es ideal para este tipo de proyectos porque:
- Se puede dividir el trabajo en etapas claras (sprints).
- Permite avanzar con entregables pequeños y funcionales.
- Fomenta la reflexión y mejora continua (retrospectivas).
- Es adaptable a equipos de uno o más integrantes.

---

### 🧠 Roles definidos en el proyecto

| Rol              | Persona responsable                                      |
|------------------|----------------------------------------------------------|
| Product Owner    | César Silva y equipo – Definen funcionalidades y metas   |
| Scrum Master     | César Silva – Organiza los sprints y gestiona el flujo   |
| Developers       | Todos los miembros del equipo – Implementan el sistema   |

---

### 🕓 Duración de los sprints

Cada sprint dura **una semana**, y al finalizar se realiza una revisión y una retrospectiva breve para analizar:

- Qué se logró
- Qué bloqueos hubo
- Qué se puede mejorar para el siguiente sprint

---

### 📋 Artefactos del SCRUM adaptado

| Artefacto         | Descripción                                                                 |
|-------------------|-----------------------------------------------------------------------------|
| Backlog del producto | Lista priorizada de funcionalidades y tareas técnicas                    |
| Sprint backlog    | Subconjunto del backlog que se abordará en la semana                        |
| Retrospectiva     | Documento semanal (`retrospectiva.md`) con reflexiones y aprendizajes       |
| Commit y Push     | Cada sprint culmina con un commit en GitHub con lo logrado                  |

---

### 📅 Plan de trabajo semanal (sprints)

#### 🔹 Sprint 1 – Preparación inicial
- Crear estructura del proyecto y repositorio
- Subir a GitHub
- Cargar documentos oficiales (reglamentos, syllabus)
- Implementar carga y segmentación de textos

#### 🔹 Sprint 2 – Embeddings y búsqueda semántica
- Generar embeddings de los documentos
- Crear índice vectorial (FAISS)
- Implementar motor de búsqueda de contexto relevante

#### 🔹 Sprint 3 – RAG: Generación de respuestas con contexto
- Integrar embeddings con preguntas de usuario
- Conectar con un modelo LLM (ej. GPT o local)
- Probar flujo completo: pregunta + contexto → respuesta

#### 🔹 Sprint 4 – Interfaz y presentación
- Desarrollar interfaz con Streamlit o Gradio
- Probar localmente
- Preparar demo o presentación para exposición

---

### ✅ Beneficios esperados

- Mayor organización del trabajo semanal
- Resultados visibles al final de cada semana
- Mejora continua con base en retros
- Código siempre subido y versionado en GitHub




