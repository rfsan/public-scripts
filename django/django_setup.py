# Python standard library
from pathlib import Path
import subprocess
from typing import Optional
# Typer
import typer

CWD = Path.cwd()
app = typer.Typer()

@app.command()
def startproject(
        name: str, 
        path: Optional[Path] = typer.Option(None)
    ):
    """
    Keyword Arguments:
        creation_path: If not creation_path is provided bla bla
    """
    if path is None:
        path = CWD
    project_path = path.resolve()/name
    # 1. Creation of project directory
    project_path.mkdir()
    # 2. Create a new python environment
    subprocess.run(['virtualenv', f'{project_path/"env"}'])
    # 3. Install Django
    pip = project_path/'env'/'bin'/'pip'
    subprocess.run([str(pip), 'install', 'django'])
    # 4. Start project
    django_admin = project_path/'env'/'bin'/'django-admin'
    subprocess.run([str(django_admin), 'startproject', name, project_path])
    # 5. Start main app
    startapp('main', project_path=project_path)


@app.command()
def startapp(name: str, project_path: Optional[Path] = typer.Option(None)):
    if project_path is None:
        project_path = CWD
    project_path = project_path.resolve()
    if not (project_path/'manage.py').exists():
        raise Exception(f'{project_path} is not a Django project')
    django_admin = project_path/'env'/'bin'/'django-admin'
    app_path = project_path/name
    app_path.mkdir()
    subprocess.run([django_admin, 'startapp', name, app_path])
    # Create other directories and files
    (app_path/'templates'/name).mkdir(parents=True)
    (app_path/'static'/name).mkdir(parents=True)
    
    
    
if __name__ == '__main__':
    app()