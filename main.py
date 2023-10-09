from classes.input_validator import InputValidator
from classes.project_creator import ProjectCreator

if __name__ == "__main__":
    # Dando nombre al proyecto
    name = input("Nombre del Proyecto: ")

    # Dandole una descripcion al proyecto
    description = input("Descripción (Enter para saltar descripcion):\n")

    # Defiendo privacidad del proyecto
    private = InputValidator().validate_variable(
        text_input="¿El proyecto debe ser privado? (s/n): "
    )

    # Definimos la instalacion de librerias
    install_default_dependencies = InputValidator().validate_variable(
        text_input="¿Desea agregar las librerias por defecto? (s/n): "
    )

    # Creacion del proyecto
    ProjectCreator().create_project(
        name=name,
        description=description,
        private=private,
        install_default_dependencies=install_default_dependencies,
    )
