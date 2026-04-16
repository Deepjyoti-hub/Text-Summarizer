import os
from pathlib import Path
import logging # to log all information during runtime as well
logging.basicConfig(level=logging.INFO, format='%(asctime)s: %(message)s:')

project_name="TextSummarizer"

# used whenever we do CICD deployment or run on cloud server, we can use this variable to get the current working directory
# current_working_directory = Path.cwd()
# It will take code from github and will deployment on cloud server. 
list_of_files=[
    ".github/workflows/.gitkeep", # It is hidden file which is used to keep the folder in github, because github does not allow empty folder. 
    f"src/{project_name}/__init__.py", # It is used to make the folder as a local package, so that we can import the modules from it.
    f"src/{project_name}/components/__init__.py", # It is used to make the folder as a local package, so that we can import the modules from it.
    f"src/{project_name}/utils/common.py", # It is used to make the folder as a local package, so that we can import the modules from it.
    f"src/{project_name}/logging/__init__.py", # It is used to make the folder as a local package, so that we can import the modules from it.
    f"src/{project_name}/config/__init__.py", 
    f"src/{project_name}/config/configuration.py", # It is used to store all the configuration related to the project, such as database connection, API keys, etc.
    f"src/{project_name}/pipeline/__init__.py", # It is used to ingest the data from the source, such as web scraping, API calls, etc.
    f"src/{project_name}/entity/__init__.py", # It is used to validate the data, such as checking for missing values, outliers, etc.
    f"src/{project_name}/constants/__init__.py", # It is used to store all the constants related to the project, such as file paths, database names, etc.
    "config/config.yaml", # It is used to store all the configuration related to the project, such as database connection, API keys, etc.
    "params.yaml", # It is used to store all the parameters related to the project, such as hyperparameters for machine learning models, etc.
    "app.py", # It is used to run the application, such as starting the server, etc.
    "main.py", # It is used to run the main function, such as training the model, etc.
    "Dockerfile", # It is used to create a docker image of the application, so that we can deploy it on cloud server, etc.
    "requirements.txt", # It is used to store all the dependencies of the project, so that we can install them using pip, etc.
    "setup.py", # It is used to create a package of the application, so that we can install it using pip, etc.
    "research/trials.ipynb", # It is used to store all the research related to the project, such as experiments, etc.
    "test.py" 
]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir, filename=os.path.split(filepath)
    if filedir!="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass # it will create an empty file if it does not exist or if it is empty
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")