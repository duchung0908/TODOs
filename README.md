# TODOs API 

################## Getting Started With Linux/Ubuntu ######################
## Steps to Install and Run
1. Clone the repository:
   ```bash
   git clone https://github.com/duchung0908/TODOs.git


2. Navigate to the project directory:
    ```bash
    cd your_project_folder


3. Install virtual environment and active (optional)
    ```bash
    python3 -m venv venv
    . venv/bin/activate

4. Install requirement file
    ```bash
    pip install -r requirements.txt

5. Migrate DB and create super user
    ```bash
    python3 manage.py makemigrations
    python3 manage.py migrate
    python3 manage.py createsuperuser

6. Runserver
    ```bash
    python3 manage.py runserver