try:
    f = open("settings.txt","rt")
    print("File settings.txt is accessible!")
    # Do something with the file
    f.close()
except FileNotFoundError:
    print("File settings.txt is not accessible, now we make this file")
    f = open("settings.txt","wt")
    f.close()
    print("File settings.txt made!")