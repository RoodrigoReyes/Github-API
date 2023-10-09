import os
import time

from github import Github

import credentials.keys as git_env


class ProjectCreator:
    def create_project_folder(self, path):
        """Crea el folder los archivos que compondran el proyecto Return: None"""
        print(f"Creando carpeta del proyecto -> {path}\n")
        os.mkdir(path)
        time.sleep(3)

    def create_venv(self):
        """Crea el entorno virtual del proyecto Return: None"""
        print("Creando entorno virtual -> 'venv'")
        time.sleep(4)
        os.system("virtualenv venv")

    def activate_venv(self):
        """Activar el entorno virtual creado por la funcion 'create_venv Return None"""
        print("Activando entorno.... ", end="")
        time.sleep(4)
        activate_this_file = os.path.join(
            os.getcwd(), "venv\\Scripts\\activate_this.py"
        )
        exec(
            compile(open(activate_this_file, "rb").read(), activate_this_file, "exec"),
            dict(__file__=activate_this_file),
        )
        time.sleep(3)
        print("Entorno virtual creado\n")

    def install_dependencies(self, requirements_file):
        """Instalacion de librerias Return None"""
        print(f"Instalando paquetes desde el archivo {requirements_file}")
        os.system(f'pip install --upgrade -q -r "{requirements_file}"')

    def create_readme(self):
        """Creacion de archivo markdown README.md"""
        print("Creando archivo README.md")
        open("README.md", "a").close()
        time.sleep(3)

    def create_main(self):
        """Creacion de archivo main.py Return None"""
        print("Creando archivo main.py")
        open("main.py", "a").close()
        time.sleep(3)

    def create_notebook(self):
        """Creando archivo Jupyter Notebook Return None"""
        print("Creando archivo notebook.ipynb")
        open("notebook.ipynb", "a").close()
        time.sleep(3)

    def initialize_git(self):
        """Inicializamos git para el proyecto Return None"""
        os.system("git init")
        os.system("echo venv/ > .gitignore")

    def create_github_repo(self, name: str, description: str, private: str):
        """Creacion de repositorio Github a traves de API Return None"""
        g = Github(git_env.token)
        u = g.get_user()
        u.create_repo(name, description=description, private=private)

    def add_git_remote(self, name: str):
        """Inicializamos conexion remota con el proyecto creado en Github Return None"""
        name = name.replace(" ", "-")
        git_remote = (
            f"git remote add origin https://github.com/RoodrigoReyes/{name}.git"
        )
        os.system(git_remote)

    def commit_and_push_to_github(self):
        """Ejecutar commit y push de los archivos creados Return None"""
        os.system("git add .")
        os.system('git commit -m "Initial Commit"')
        os.system("git push -u origin master")

    def open_visual_studio(self):
        """Abrir Visual Studio Code Return None"""
        os.system("code .")

    def create_project(
        self,
        name: str,
        description: str,
        private: str,
        install_default_dependencies: bool,
    ):
        """Crea un proyecto en Github a partir de los parámetros indicados. Args: name (str): Nombre del proyecto. description (str): Descripción del proyecto. private (bool, optional): Privacidad del proyecto. Por defecto es True."""
        # Path donde se creara la carpeta del proyecto
        folder_name = name.lower().replace(" ", "-")
        path = f"C:\\Users\\Rodrigo\\Documents\\Python Projects\\{folder_name}"

        # Creando carpeta del proyecto
        self.create_project_folder(path)
        os.chdir(path)

        # Creando entorno virtual
        self.create_venv()

        # Activando entorno virtual
        self.activate_venv()

        # Condicional que determina si se instalaran las librerias por defecto
        # de esta automatizacion o si se instalaran las 3 más basicas
        # pandas - numpy- matplotlib
        if install_default_dependencies:
            # Instalando paquetes predeterminados
            print("Instalando paquetes predeterminados")
            os.system("pip install --upgrade -q pandas numpy matplotlib")
        else:
            # Instalando paquetes desde el archivo requirements.txt
            requirements_file = "C:\\requirements.txt"
            self.install_dependencies(requirements_file)

        # Creando archivo markdown README.md
        self.create_readme()

        # Creando archivo main.py del proyecto
        self.create_main()

        # Creando archivo Jupyer Notebook
        self.create_notebook()

        # Inicializamos Git
        self.initialize_git()

        # Creando repositorio por medio de la API de Github
        self.create_github_repo(name, description, private)

        # Inizializamos el repositorio remoto del proyecto creado en Github
        self.add_git_remote(name)

        # Ejecutando commit y push con los archivos anteriormente creados
        self.commit_and_push_to_github()

        # Abrir Visual Studio Code
        self.open_visual_studio()
