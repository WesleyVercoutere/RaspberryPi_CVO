from pathlib import Path

if Path('settings.txt').is_file():
    print ("File exist")
else:
    print ("File not exist")