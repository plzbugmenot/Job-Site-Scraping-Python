@echo off
call .venv\Scripts\activate.bat
python main.py
del 1.json
del 2.json
del 3.json
del 4.json
del total_data.json

pause
