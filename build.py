import os

os.system("pip install -r requirements.txt --break")
os.system("pyinstaller --onefile --noconsole patch.py")
