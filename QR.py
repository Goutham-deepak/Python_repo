from flask import Flask, request, send_file
import qrcode 
import os

img=qrcode.make('')
img.save('new_imageOR.jpg')
os.startfile("new_imageOR.jpg")



