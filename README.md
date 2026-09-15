# Evaluación Sumativa N° 01: Programación Back End

## Información del Estudiante
- **Nombre Completo:** Benjamín Rivas
- **Asignatura:** Programación Back End (Primavera 2026)
- **Docente:** Luis Arriagada Cerda
- **Institución:** INACAP - Área de Informática y Ciberseguridad

---

## Descripción del Proyecto
Este proyecto fue desarrollado en el framework **Django**, utilizando **Git y GitHub** para la gestión de versiones mediante ramas (*branches*) y solicitudes de extracción (*Pull Requests*).

### Estructura de Ramas y Aplicaciones
1. **`main`**: Rama principal con el proyecto base limpio y la posterior integración final de ambas aplicaciones.
2. **`rivasbenjaminrama1`**: Contiene la aplicación `catalogo` con sus respectivas vistas y plantillas HTML.
3. **`rivasbenjaminrama2`**: Contiene la aplicación `contacto` con sus respectivas vistas y plantillas HTML.

---

## Instrucciones para Ejecutar Localmente

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/algo1-2/evaluacion1-backend-django.git
   cd evaluacion1-backend-django
   ```

2. Activar el entorno virtual:
   - En Windows (PowerShell):
     ```powershell
     .\.venv\Scripts\Activate.ps1
     ```
   - En Linux/Mac:
     ```bash
     source .venv/bin/activate
     ```

3. Instalar dependencias:
   ```bash
   pip install django
   ```

4. Ejecutar el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

5. Acceder a las vistas desde el navegador:
   - Catálogo de Productos: `http://127.0.0.1:8000/catalogo/`
   - Detalle de Producto: `http://127.0.0.1:8000/catalogo/detalle/`
   - Centro de Contacto: `http://127.0.0.1:8000/contacto/`
   - Preguntas Frecuentes (FAQ): `http://127.0.0.1:8000/contacto/faq/`
