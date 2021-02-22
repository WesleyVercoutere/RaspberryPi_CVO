#Import required libraries in Thonny via Tools/ Manage Packages for PC
# en by command line terminal on RP  sudo apt-get install python3-pil

# on RP possible no default viewer to open this image, can try :
'''
sudo apt-get install xli
cd /usr/local/bin
sudo ln -s /usr/bin/xli xv
'''


from PIL import Image#, ImageDraw # PIL manage packages pillow-pil

#Create image object
im = Image.open("pianoles.jpg")

# show image object
im.show()