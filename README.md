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
| **Sprint 2 – Ingesta & limpieza**        | ✅ Completado (27 abr → 03 may 2025) |
| **Sprint 3 – Indexado vectorial**        | ✅ Completado (04 may → 10 may 2025) |
| **Sprint 4 – Optimización RAG**          | 🔄 En curso (11 may → 17 may 2025) |
| Integración LLM y API REST               | ⏳ Pendiente |
| UI web/chatbot                           | ⏳ Pendiente |
| Pruebas piloto con estudiantes           | ⏳ Futuro |

---

## 🗺️ Hoja de ruta en 8 sprints (1 semana c/u)

| Sprint | Fechas 2025 (lun-dom) | Objetivo técnico                                               | Pareja inicial | Revisor |
|-------:|----------------------|----------------------------------------------------------------|----------------|---------|
| **1** | 19 abr → 26 abr | **Tokenizer MVP + CI**                                | CS + DG | JV |
| **2** | 27 abr → 03 may | Ingesta & limpieza PDFs/HTML                           | DG + JV | CS |
| **3** | 04 may → 10 may | Indexado vectorial (FAISS/Chroma)                      | JV + CS | DG |
| **4** | 11 may → 17 may | **Optimización RAG avanzada** *(Sprint actual)*        | CS + DG | JV |
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
| HU-1 | Tokenizar texto crudo (UTF-8, puntuación) | 3 | #01 |
| HU-2 | Configurar CI (Black, Ruff, pytest-cov)   | 2 | #02 |
| HU-3 | CLI round-trip encode → decode            | 1 | #03 |

</details>

<details>
<summary><strong>Sprint 2 — Ingesta & limpieza (✅ cerrado)</strong></summary>

| HU | Título                                     | Pts | PR / Issue |
|----|--------------------------------------------|-----|-----------|
| HU-4 | ETL de PDFs/HTML a texto plano            | 3 | #04 |
| HU-5 | Aplicar algoritmos de OCR                 | 2 | #05 |
| HU-6 | Normalización y limpieza de texto         | 1 | #06 |

</details>

<details>
<summary><strong>Sprint 3 — Indexado vectorial (✅ cerrado)</strong></summary>

| HU | Título                                     | Pts | PR / Issue |
|----|--------------------------------------------|-----|-----------|
| HU-7 | Implementar vector store con FAISS        | 3 | #07 |
| HU-8 | Embeddings con modelo SentenceTransformers| 2 | #08 |
| HU-9 | Sistema de búsqueda semántica básica      | 2 | #09 |
| HU-10| Métricas de evaluación de retrieval       | 1 | #10 |

</details>

<details>
<summary><strong>Sprint 4 — Optimización RAG avanzada (🔄 en curso)</strong></summary>

| HU | Título                                     | Pts | Estado |
|----|--------------------------------------------|-----|--------|
| HU-11| Mejora de prompt engineering con templates | 3 | 🔄 En desarrollo |
| HU-12| Chunking avanzado (semantic chunking)     | 3 | 🔄 En desarrollo |
| HU-13| Optimización del formato JSON de respuesta| 2 | ⏳ Pendiente |
| HU-14| Implementar reranking con Cross-Encoder   | 2 | ⏳ Pendiente |

**Objetivos del Sprint 4:**
- **Prompt Engineering**: Implementar templates dinámicos y técnicas de few-shot learning para mejorar la calidad de las respuestas
- **Chunking Avanzado**: Aplicar semantic chunking y recursive character splitting para optimizar la segmentación de documentos
- **Formato JSON**: Estandarizar y optimizar el esquema de respuestas JSON para mejor integración con el frontend
- **Reranking**: Implementar un sistema de reordenamiento de resultados para mejorar la precisión del retrieval

</details>

<details>
<summary><strong>Sprint 5 — LLM wrapper & prompt-engineering</strong></summary>

| HU | Título                                     | Pts | Estado |
|----|--------------------------------------------|-----|--------|
| HU-15| Integración con LLM (OpenAI/Anthropic)   | 3 | ⏳ Pendiente |
| HU-16| Sistema de fallback y manejo de errores   | 2 | ⏳ Pendiente |
| HU-17| Cache de respuestas frecuentes            | 2 | ⏳ Pendiente |
| HU-18| Logging y monitoreo de queries            | 1 | ⏳ Pendiente |

</details>

<details>
<summary><strong>Sprint 6 — API REST + Docker</strong></summary>

| HU | Título                                     | Pts | Estado |
|----|--------------------------------------------|-----|--------|
| HU-19| API REST con FastAPI                      | 3 | ⏳ Pendiente |
| HU-20| Containerización con Docker               | 2 | ⏳ Pendiente |
| HU-21| Documentación API con Swagger             | 1 | ⏳ Pendiente |
| HU-22| Tests de integración API                  | 2 | ⏳ Pendiente |

</details>

<details>
<summary><strong>Sprint 7 — Frontend & UI</strong></summary>

| HU | Título                                     | Pts | Estado |
|----|--------------------------------------------|-----|--------|
| HU-23| Interfaz React con Tailwind CSS           | 4 | ⏳ Pendiente |
| HU-24| Componente de chat interactivo            | 3 | ⏳ Pendiente |
| HU-25| Sistema de historial de conversaciones    | 2 | ⏳ Pendiente |
| HU-26| Tests end-to-end con Cypress              | 1 | ⏳ Pendiente |

</details>

<details>
<summary><strong>Sprint 8 — Deploy & Observabilidad</strong></summary>

| HU | Título                                     | Pts | Estado |
|----|--------------------------------------------|-----|--------|
| HU-27| Configuración Helm chart para Kubernetes  | 3 | ⏳ Pendiente |
| HU-28| Métricas y alertas con Prometheus         | 2 | ⏳ Pendiente |
| HU-29| Dashboard de monitoreo                     | 2 | ⏳ Pendiente |
| HU-30| Documentación de deployment               | 1 | ⏳ Pendiente |

</details>

---

## 🛠️ Estructura del repositorio

```
rag-uni-fiee/
├── src/
│   ├── tokenizer/          # Sprint 1: Tokenización básica
│   ├── ingestion/          # Sprint 2: ETL y limpieza
│   ├── vectorstore/        # Sprint 3: Indexado vectorial
│   ├── retrieval/          # Sprint 4: RAG optimizado
│   ├── llm/               # Sprint 5: Wrapper LLM
│   └── api/               # Sprint 6: FastAPI
├── frontend/              # Sprint 7: React UI
├── deploy/                # Sprint 8: K8s configs
├── tests/
├── docs/
└── requirements.txt
```

---

## 🚀 Instalación y uso

```bash
# Clonar repositorio
git clone https://github.com/ORG/rag-uni-fiee.git
cd rag-uni-fiee

# Instalar dependencias
pip install -r requirements.txt

# Ejemplo de uso del tokenizer (Sprint 1)
python -m src.tokenizer "¡Hola, UNI!"
# IDs : [0, 1, 2, 3]
# Back: ¡ hola , uni !

# Ejecutar ingesta de documentos (Sprint 2+)
python -m src.ingestion --input docs/ --output vectorstore/

# Consultar el sistema RAG (Sprint 4+)
python -m src.retrieval --query "¿Cuáles son los requisitos para graduarse?"
```

---

## 📊 Métricas de calidad

| Sprint | Cobertura de tests | Precisión@10 | Latencia avg |
|--------|-------------------|--------------|--------------|
| 1      | 85%              | N/A          | N/A          |
| 2      | 82%              | N/A          | N/A          |
| 3      | 79%              | 0.73         | 1.2s         |
| 4      | TBD              | TBD          | TBD          |

---

## 🤝 Contribución

1. **Fork** el repositorio
2. Crear una **rama feature** (`git checkout -b feature/nueva-funcionalidad`)
3. **Commit** cambios (`git commit -m 'Agregar nueva funcionalidad'`)
4. **Push** a la rama (`git push origin feature/nueva-funcionalidad`)
5. Crear un **Pull Request**

**Estándares de código:**
- Formateo: `black src/`
- Linting: `ruff check src/`
- Tests: `pytest --cov=src/`

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

---

## 🙋‍♂️ Contacto

Para preguntas sobre el proyecto:
- **Email**: contacto@fiee.uni.edu.pe
- **Issues**: [GitHub Issues](https://github.com/ORG/rag-uni-fiee/issues)
- **Discusiones**: [GitHub Discussions](https://github.com/ORG/rag-uni-fiee/discussions)
