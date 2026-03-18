# Estándares de Contribución - Equipo [Nombre]

Para asegurar la calidad del repositorio, todas las contribuciones deben seguir estas reglas:

### 1. Formato de Nombres
- **Archivos:** Todos los nombres deben usar `kebab-case` (ejemplo: `script-procesamiento-datos.py`).
- **Directorios:** Usar minúsculas y nombres descriptivos.

### 2. Estructura de Documentos Markdown
Todo archivo `.md` debe incluir el siguiente encabezado:
- # Título del Documento
- **Autor:** [Nombre del Alumno]
- **Fecha:** [DD/MM/AAAA]
- **Contenido:** (Descripción clara del propósito)

### 3. Mensajes de Commit (Conventional Commits)
Se debe seguir el formato: `
tipo: descripción corta`
- `feat:` Nuevas funcionalidades.
- `fix:` Corrección de errores.
- `docs:` Cambios en la documentación.
- `chore:` Tareas de mantenimiento.

### 4. Flujo de Trabajo
1. Crear una rama:
   git checkout -b feature/nombre-rama

2. Realizar cambios y commits

3. Subir la rama:
   git push origin feature/nombre-rama

4. Crear Pull Request

5. Esperar revisión y aprobación

---

## 📌 Reglas de calidad

- No se aceptan archivos sin estructura definida
- Todo commit debe seguir el estándar
- Se deben corregir los comentarios del revisor antes de aprobar
- Prohibido hacer push directo a `main`.
- Todo cambio requiere un **Pull Request (PR)** y la aprobación de un revisor.