import os

from pathlib import Path

import logging


logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "cnnClssifier"

#
list_of_files = [
    #we need it during deployment
    #.gitkeep is for to reflect it in github empty folder wont reflect anything
    ".github/workflows/.gitkeep",
    #since it is local package, construtor __init__.py is given
    # by this we can import other py files from same folder 
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",


    "config/config.yaml",

    "dvc.yaml",

    "params.yaml",
    "requirements.txt",
    "setup.py",

    "research/trials.ipynb",
    'templates/index.html'

]

for filePath in list_of_files:
    filePath = Path(filePath)
    fileDir,fileName = os.path.split(filePath)

    if fileDir != "":
        os.makedirs(fileDir,exist_ok=True)
        logging.info(f"creating the directory: {fileDir} for the file : {fileName}")
   
   
    #checking file exists or size of file
    if (not os.path.exists(filePath)) or (os.path.getsize(filePath) == 0):
        with open(filePath,'w') as f:
            pass
            logging.info(f"creating empty file: {filePath}")

    else:
        logging.info(f"{fileName} is already exists")


   
