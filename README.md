# RAG-UNI-FIEE

Repositorio oficial del proyecto **Recuperación de Información Aumentada (RAG)**  
para la Facultad de Ingeniería Eléctrica y Electrónica – **Universidad Nacional de Ingeniería (UNI)**.

<p align="center">
  <img src="https://img.shields.io/github/actions/workflow/status/&lt;ORG&gt;/&lt;REPO&gt;/ci.yml?label=CI" alt="CI Status"/>
  <img src="https://img.shields.io/endpoint?url=https://codecov.io/api/gh/&lt;ORG&gt;/&lt;REPO&gt;/coverage_badge.json" alt="Coverage"/>
  <a href="https://github.com/&lt;ORG&gt;/&lt;REPO&gt;/projects/1">
    <img src="https://img.shields.io/badge/kanban-board-blueviolet" alt="Project Board"/>
  </a>
</p>

---

## 🎯 Objetivo general
Construir un **chatbot RAG** que responda de forma inmediata, confiable y con referencias a:

* Reglamentos académicos (créditos, repitencia, egreso, etc.).
* Sílabos, bibliografía y contenidos de los cursos.
* Procedimientos administrativos frecuentes.

---

## 🤖 ¿Qué es un sistema RAG?
*Recuperación* + *Generación*:  
1. **Recuperador** (vector store) trae los documentos más relevantes  
2. **Generador** (LLM) redacta la respuesta citando las fuentes  
➡️ Respuestas actualizadas, con grounding documental y mínimas alucinaciones.

---

## 🧑‍🤝‍🧑 Equipo XP

| Inicial | Nombre  | Ubicación | Rol XP† |
|---------|---------|-----------|---------|
| **CS**  | César   | Lima-PE   | Dev / PO |
| **DG**  | Diego   | Lima-PE   | Dev |
| **JV**  | Javier  | Lima-PE   | Dev |

† _Programación Extrema_ → todos son desarrolladores, el **Product Owner** rota cada sprint para fomentar _collective ownership_.

*Pair-programming rotativo*: cada día se forma una dupla distinta; la tercera persona revisa el PR.

---

## 🚦 Estado actual

| Entregable                               | Progreso |
|------------------------------------------|----------|
| **Sprint 1 – Tokenizer MVP**             | ✅ Completado (19 → 26 abr 2025) |
| Recolección de reglamentos oficiales     | 🔄 En curso |
| Selección de componentes (LangChain, FAISS, etc.) | 🔄 Evaluación |
| Integración de sílabos y bibliografía    | ⏳ Pendiente |
| UI web/chatbot                           | ⏳ Pendiente |
| Pruebas piloto con estudiantes           | ⏳ Futuro |

---

## 🗺️ Hoja de ruta en 8 sprints (1 semana c/u)

| Sprint | Fechas 2025 (lun-dom) | Objetivo técnico                                               | Pareja inicial | Revisor |
|-------:|----------------------|----------------------------------------------------------------|----------------|---------|
| **1** | 19 abr → 26 abr | **Tokenizer MVP + CI**                                | CS + DG | JV |
| **2** | 27 abr → 03 may | Ingesta & limpieza PDFs/HTML                           | DG + JV | CS |
| **3** | 04 may → 10 may | Indexado vectorial (FAISS/Chroma)                      | JV + CS | DG |
| **4** | 11 may → 17 may | Recuperador semántico + reranking                      | CS + DG | JV |
| **5** | 18 may → 24 may | LLM wrapper & prompt-engineering                       | DG + JV | CS |
| **6** | 25 may → 31 may | API REST (FastAPI) + Docker                            | JV + CS | DG |
| **7** | 01 jun → 07 jun | Front-end React/Tailwind + pruebas e2e                 | CS + DG | JV |
| **8** | 08 jun → 14 jun | Observabilidad, Helm chart y despliegue                | DG + JV | CS |

---

## 📑 Historias de usuario (HU) por sprint

<details>
<summary><strong>Sprint 1 — Tokenizer MVP (✅ cerrado)</strong></summary>

| HU | Título                                    | Pts | PR / Issue |
|----|-------------------------------------------|-----|-----------|
| HU-1 | Tokenizar texto crudo (UTF-8, puntuación) | 3 | # xx |
| HU-2 | Configurar CI (Black, Ruff, pytest-cov)   | 2 | # xx |
| HU-3 | CLI round-trip encode → decode            | 1 | # xx |

</details>

<details>
<summary><strong>Sprint 2 — Ingesta & limpieza</strong></summary>

| HU | Título                                     | Pts | Estado |
|----|--------------------------------------------|-----|--------|
| HU-4 | ETL de PDFs/HTML a texto plano            | 3 | ☐ |
| HU-5 | Normalizar acentos y caracteres           | 2 | ☐ |
| HU-6 | QA tamaño y duplicados                    | 1 | ☐ |
</details>

<!-- Copiar/pegar y adaptar para HUs de sprints 3-8 -->

---

## 🛠️ Estructura del repositorio

