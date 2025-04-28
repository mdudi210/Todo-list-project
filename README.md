python -m venv venv
Set-ExecutionPolicy Unrestricted -Scope Process
venv\Scripts\Activate.ps1

pip freeze > requirement.txt

fastapi dev main.py
