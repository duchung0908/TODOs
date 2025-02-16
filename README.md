# TODOs API 

################## Getting Started With Linux/Ubuntu OR Windows ######################
## Steps to Install and Run
1. Clone the repository:
   ```bash
   git clone https://github.com/duchung0908/TODOs.git


2. Navigate to the project directory:
    ```bash
    cd your_project_folder


3. Install virtual environment and active (optional if not the packages will install directly on your device)

--Linux/Ubuntu
    ```bash
    python3 -m venv venv
    . venv/bin/activate

--Windows
    ```bash
    python -m venv venv
    . venv\Scripts\activate 

---Note: If you can not activate virtual environment on Windows because of the PowerShell on your device, follow the step bellow:
    - Run Windows PowerShell as administrator
        ```bash
        Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
    - And type "yes"

4. Install requirement file
    ```bash
    pip install -r requirements.txt

5. Migrate DB and create super user or use my account ("username": "duchung","password": "123456789@")

    5.1 Linux/Ubuntu
        ```bash
        python3 manage.py makemigrations
        python3 manage.py migrate
        python3 manage.py createsuperuser

    5.2 Windows
        ```bash
        python manage.py makemigrations
        python manage.py migrate
        python manage.py createsuperuser

6. Runserver

    6.1 Linux/Ubuntu
    
        ```bash
        cd TodoAPI folder
        python3 manage.py runserver

    6.2 Windows

        ```bash
        cd TodoAPI folder
        python manage.py runserver

## Testing
    
1. Linux/Ubuntu

    ```bash
    python3 manage.py test

2. Windows

    ```bash
    python manage.py test

#### 
If you need help, contact me via email "tranduchung0908@gmail.com". Thanks
####