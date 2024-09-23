# blog-base

## 1. Configura repo

1. Crear el repositorio
2. Agregar companeros (1 por grupo)
3. Copiar los archivos de este repo al nuevo
  - git clone https://github.com/xlmriosx/blog-base.git
4. Subir los cambios a su repositorio del grupo
  - git add .
  - git commit -m "initial commit project"
  - git push
5. Verificar que se subio el proyecto

## 2. Verificar dependencias

1. Configurar un entorno virtual
  - python -m venv ve
  - ./ve/Scripts/activate (Windows)
  - Nos paramos donde esta el archivo requirements.txt (puedo verlo con `dir` o `ls`)
  - pip install -r requirements.txt
  
  
2. Correr proyecto
  - Nos paramos donde esta el manage.py
  - python manage.py runserver (para cortar apreto CTRL + C)
  - python manage.py migrate (para migrar)

3. Verificar que esta corriendo
  - Entrar a localhost:8000
