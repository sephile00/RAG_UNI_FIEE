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

<p align="center">
  <img src="https://img.shields.io/github/actions/workflow/status/<ORG>/<REPO>/ci.yml?label=CI" alt="CI Status"/>
  <img src="https://img.shields.io/badge/coverage-80%25-brightgreen" alt="Coverage"/>
  <a href="https://github.com/<ORG>/<REPO>/projects/1"><img src="https://img.shields.io/badge/kanban-board-blueviolet" alt="Project Board"/></a>
</p>

## 📜 Visión
Asistente RAG para reglamentos, normas y syllabus de la Facultad.  
Desarrollado con Programación Extrema (XP) en **8 sprints** semanales.

## 👥 Equipo
| Inicial | Nombre | Zona pairing |
|---------|--------|--------------|
| **CS**  | César  | Lima-PE |
| **DG**  | Diego  | Lima-PE |
| **JV**  | Javier | Lima-PE |

> _Pair-programming rotativo_: cada día se cambia la dupla; la tercera persona revisa el PR.

---

## 🗓️ Cronograma de sprints

| Sprint | Semana (2025) | Objetivo técnico | Pareja inicial | Revisor |
|-------:|---------------|------------------|----------------|---------|
| **1** | 28 abr → 4 may | **Tokenizer MVP + CI** | CS + DG | JV |
| **2** | 5 may → 11 may | Ingesta & limpieza PDFs/HTML | DG + JV | CS |
| **3** | 12 may → 18 may | Indexado vectorial (FAISS) | JV + CS | DG |
| **4** | 19 may → 25 may | Recuperador y reranking | CS + DG | JV |
| **5** | 26 may → 1 jun | LLM wrapper & prompts | DG + JV | CS |
| **6** | 2 jun → 8 jun | API FastAPI + Docker | JV + CS | DG |
| **7** | 9 jun → 15 jun | Front-end React/Tailwind | CS + DG | JV |
| **8** | 16 jun → 22 jun | Deploy & observabilidad | DG + JV | CS |

---

## 🎯 Historias de usuario por sprint

<details>
<summary><strong>Sprint 1 — Tokenizer MVP</strong></summary>

| HU | Título | Puntos | Estado |
|----|--------|--------|--------|
| **HU-1** | Tokenizar texto crudo | 3 | ☐ |
| **HU-2** | Configurar pruebas automatizadas | 2 | ☐ |
| **HU-3** | CLI round-trip encode→decode | 1 | ☐ |

</details>

<details>
<summary><strong>Sprint 2 — Ingesta & limpieza</strong></summary>

| HU | Título | Puntos | Estado |
|----|--------|--------|--------|
| **HU-4** | ETL de PDFs/HTML a texto | 3 | ☐ |
| **HU-5** | Normalizar caracteres y acentos | 2 | ☐ |
| **HU-6** | QA de tamaño/documento | 1 | ☐ |

</details>

<!-- Repetir blocks de <details> para sprints 3-8 … -->

---

## 🧑‍💻 Estructura del repositorio

