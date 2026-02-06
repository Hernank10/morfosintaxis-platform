# 🎓 Plataforma de Morfosintaxis Interactiva

¡Bienvenido a la plataforma de aprendizaje de lingüística! Este sistema está diseñado para enseñar **Morfosintaxis** de manera dinámica, combinando teoría estructurada con un potente motor de autoevaluación.

## 🚀 Características Principales
* **Banco de 100 Ejercicios:** Preguntas automatizadas de Sintaxis y Morfología con niveles (Básico, Intermedio, Avanzado).
* **Retroalimentación Inmediata:** Explicaciones pedagógicas tras cada respuesta para reforzar el aprendizaje.
* **Gamificación:** Barra de progreso en tiempo real y sistema de logros (80% para completar curso).
* **Interfaz Moderna:** Diseño responsivo basado en Bootstrap 5 y animaciones fluidas.

## 🛠️ Tecnologías Utilizadas
* **Backend:** Django 6.0.2 (Python)
* **Frontend:** HTML5, CSS3, JavaScript (Vanilla), Bootstrap 5
* **Base de Datos:** SQLite 3

## 📦 Instalación y Configuración

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/Hernank10/morfosintaxis-platform.git
   cd morfosintaxis-platform/backend
   ```

2. **Entorno Virtual:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Migraciones:**
   ```bash
   python3 manage.py makemigrations
   python3 manage.py migrate
   ```

4. **Poblar la base de datos (Ejercicios y Cursos):**
   Para generar automáticamente los 100 ejercicios y la estructura de cursos, ejecuta:
   ```bash
   python3 manage.py shell < populate_data.py
   ```

## 🖥️ Uso
Para iniciar el servidor de desarrollo:
```bash
python3 manage.py runserver 0.0.0.0:8000
```
Accede a la plataforma en `http://localhost:8000` o a través de la URL de tu Codespace.

## 👥 Contribuciones
Este es un proyecto de código abierto con fines educativos. Siéntete libre de clonarlo y mejorarlo.

---
Desarrollado con ❤️ por **HernanK10**
