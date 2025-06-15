This is a project that uses Flask

To ensure proper functionality, do the following:

1. After cloning the repository, go into the terminal and run: 
        
        python -m venv venv
        .\venv\Scripts\activate
        pip install -r requirements.txt

        python app.py


2. If the system is not authorized to run scripts, on Windows powershell (admin):


        Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
        Get-ExecutionPolicy  ## Should say 'RemoteSigned'