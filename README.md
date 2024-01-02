## Descripción
Este script Python proporciona una solución automatizada para la creación y configuración inicial de proyectos. Facilita la generación de carpetas, entornos virtuales, instalación de dependencias y configuración de repositorios GitHub. Ahorra tiempo y esfuerzo al iniciar nuevos proyectos.

## Instrucciones de Uso

### Requisitos Previos
- Asegúrese de tener Python instalado en su sistema.
- Es recomendable tener [Visual Studio Code](https://code.visualstudio.com/) instalado.

### Pasos para Crear un Nuevo Proyecto

1. Ejecute el script `main.py`.
2. Proporcione el nombre del proyecto cuando se le solicite.
3. Agregue una descripción opcional del proyecto.
4. Seleccione la privacidad del repositorio (público o privado).
5. Indique si desea instalar las bibliotecas por defecto.
6. Espere a que el script complete la creación y configuración del proyecto.

### Estructura del Proyecto
El proyecto se creará en la carpeta especificada y contendrá:

- Carpeta `venv`: Entorno virtual del proyecto.
- Archivo `README.md`: Documentación del proyecto.
- Archivo `main.py`: Archivo principal del proyecto.
- Archivo `notebook.ipynb`: Cuaderno Jupyter para análisis.
- Archivo `.gitignore`: Configuración de Git para ignorar la carpeta `venv`.
- Repositorio GitHub: Se creará automáticamente (requiere credenciales de GitHub).

## Contribuciones
Siéntase libre de contribuir al desarrollo de este proyecto. Abra problemas para informar errores o proponer nuevas características.

---
**¡Gracias por usar el Proyecto Automatizado!**
