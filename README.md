# 📚 Plataforma Educativa de Morfosintaxis

## Nombre del proyecto

**Morfosintaxis Platform**
Plataforma educativa digital para el aprendizaje de la morfosintaxis del español, con analíticas docentes, retroalimentación automática y certificación por logros.

---

## 🎓 Resumen académico

Este proyecto corresponde al diseño y desarrollo de una **plataforma educativa basada en tecnologías web**, orientada al fortalecimiento del aprendizaje morfosintáctico en estudiantes de español. Integra principios de la **pedagogía digital**, la **evaluación formativa**, el **aprendizaje adaptativo** y la **analítica educativa**.

La plataforma permite a estudiantes interactuar con contenidos estructurados, ejercicios, juegos lingüísticos y evaluaciones, mientras que los docentes acceden a paneles visuales de seguimiento del progreso y desempeño.

---

## 🧠 Fundamentación pedagógica

La plataforma se apoya en los siguientes enfoques:

* **Constructivismo**: el estudiante construye el conocimiento a partir de la práctica y la retroalimentación.
* **Aprendizaje basado en errores**: feedback automático según el tipo de error morfosintáctico.
* **Evaluación formativa continua**: seguimiento progresivo por competencias.
* **Aprendizaje autónomo y guiado**: itinerarios desbloqueables por logro.
* **Analítica del aprendizaje (Learning Analytics)**: visualización de datos para la toma de decisiones docentes.

---

## 🧩 Funcionalidades principales

### 👩‍🎓 Estudiante

* Acceso a contenidos morfosintácticos estructurados
* Ejercicios interactivos y juegos lingüísticos
* Feedback textual automático por tipo de error
* Progreso visible por unidades y logros
* Generación automática de certificados

### 👨‍🏫 Docente

* Panel visual de seguimiento del alumnado
* Gráficas de desempeño (Chart.js)
* Análisis por tipo de error
* Informes académicos automáticos por estudiante

### 🛠️ Sistema

* Desbloqueo progresivo de contenidos
* Certificación automática por logro alcanzado
* Arquitectura modular y escalable

---

## 🏗️ Arquitectura del proyecto

```text
morfosintaxis_platform/
├── backend/            # Backend Django
│   ├── config/         # Configuración del proyecto
│   ├── morfo_accounts/ # Gestión de usuarios
│   ├── morfo_content/  # Contenidos educativos
│   ├── morfo_learning/ # Lógica de aprendizaje
│   ├── morfo_analytics/# Analíticas y reportes
│   ├── morfo_certificates/ # Certificación
│   ├── manage.py
│   └── requirements.txt
├── frontend/           # Interfaz (Bootstrap / JS)
├── docs/               # Documentación académica
├── scripts/            # Scripts auxiliares
└── .gitignore
```

---

## 🧪 Tecnologías utilizadas

* **Backend**: Python 3.13, Django 6.x
* **Frontend**: HTML5, CSS3, Bootstrap 5
* **Visualización**: Chart.js
* **Base de datos**: SQLite (desarrollo)
* **Control de versiones**: Git & GitHub

---

## 📊 Evaluación y analítica

La plataforma registra:

* Errores morfológicos y sintácticos
* Frecuencia y tipo de fallos
* Avance por unidad
* Indicadores de logro

Estos datos se visualizan mediante gráficas para facilitar la **interpretación pedagógica**.

---

## 📜 Certificación

El sistema genera **certificados automáticos** cuando el estudiante alcanza criterios definidos de logro, lo que refuerza la motivación y el aprendizaje basado en objetivos.

---

## 🔬 Proyección académica

Este proyecto es apto para:

* Trabajo de grado / TFM
* Ponencia en educación digital
* Artículo académico sobre evaluación automática
* Desarrollo futuro con IA educativa

---

## 👤 Autor

**Hernán Acevedo Mar**
Proyecto académico-profesional en educación digital y desarrollo web.

---

## 📌 Estado del proyecto

🟡 En desarrollo — arquitectura base y módulos principales en construcción.

---

## 📄 Licencia

Proyecto académico. Uso educativo y de investigación.

