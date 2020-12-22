#
# ---------------------------------------------
# Image Crop
# ---------------------------------------------
# Author: Adam Blaszczyk
#         http://wyciekpamieci.blogspot.com
# Date:   2020-12-22
# ---------------------------------------------
#
# Requirements:
#         - Python 3.x
#         - OpenCV library (pip install opencv-python)
#

from tkinter import *
from tkinter import filedialog as fd
import cv2

def sx1_move(xx1):
    global x1, y1, x2, y2
    global sx1
    print(x1, y1, x2, y2)
    x1 = int(xx1)
    if x1 >= x2:
        x1 = x2 - 1
    sx1.set(x1)
    img = img_clone.copy()
    cv2.rectangle(img, (x1,y1), (x2,y2), (0,0,255), 1)
    cv2.imshow("Input", img)
    
def sx2_move(xx2):
    global x1, y1, x2, y2
    global sx2
    print(x1, y1, x2, y2)
    x2 = int(xx2)
    if x2 <= x1:
        x2 = x1 + 1
    sx2.set(x2)
    img = img_clone.copy()
    cv2.rectangle(img, (x1,y1), (x2,y2), (0,0,255), 1)
    cv2.imshow("Input", img)

def sy1_move(yy1):
    global x1, y1, x2, y2
    global sy1
    print(x1, y1, x2, y2)
    y1 = int(yy1)
    if y1 >= y2:
        y1 = y2 - 1
    sy1.set(y1)
    img = img_clone.copy()
    cv2.rectangle(img, (x1,y1), (x2,y2), (0,0,255), 1)
    cv2.imshow("Input", img)

def sy2_move(yy2):
    global x1, y1, x2, y2
    global sy2
    print(x1, y1, x2, y2)
    y2 = int(yy2)
    if y2 <= y1:
        y2 = y1 + 1
    sy2.set(y2)
    img = img_clone.copy()
    cv2.rectangle(img, (x1,y1), (x2,y2), (0,0,255), 1)
    cv2.imshow("Input", img)

def bt1_click():
    global img, img_clone
    global x1, y1, x2, y2
    global sx1, sx2, sy1, sy2
    
    filename = fd.askopenfilename(filetypes=[("JPG files","*.jpg"), ("PNG files","*.png"), ("BMP files","*.bmp")])
    
    img = cv2.imread(filename)
    height = img.shape[0] #y
    width  = img.shape[1] #x
    
    x1, y1, x2, y2 = 0, 0, width-1, height-1
    print(x1, y1, x2, y2)
    
    img_clone = img.copy()
    
    xx1 = IntVar()
    sx1 = Scale(root, orient=HORIZONTAL, length=300, from_=0, to=width-1, variable=xx1, command=sx1_move)
    sx1.set(0)
    sx1.place(x=30, y=340)

    xx2 = IntVar()
    sx2 = Scale(root, orient=HORIZONTAL, length=300, from_=0, to=width-1, variable=xx2, command=sx2_move)
    sx2.set(width)
    sx2.place(x=370, y=340)

    yy1 = IntVar()
    sy1 = Scale(root, orient=VERTICAL, length=300, from_=0, to=height-1, variable=yy1, command=sy1_move)
    sy1.set(0)
    sy1.place(x=320, y=30)

    yy2 = IntVar()
    sy2 = Scale(root, orient=VERTICAL, length=300, from_=0, to=height-1, variable=yy2, command=sy2_move)
    sy2.set(height)
    sy2.place(x=320, y=400)

    cv2.rectangle(img, (0,0), (width-1,height-1), (0,0,255), 1)

    cv2.imshow("Input", img)
        
def bt2_click():
    global img, img_clone
    global x1, y1, x2, y2
    filename = fd.asksaveasfilename(filetypes=[("JPG files","*.jpg"), ("PNG files","*.png"), ("BMP files","*.bmp")], defaultextension = "*.jpg")
    print(filename)
    img_crop = img_clone[y1:y2+1, x1:x2+1] #y,x
    cv2.imwrite(filename, img_crop)


root = Tk()
root.title("Image Crop")
root.geometry("700x740")

bt1 = Button(root, bg="light sky blue", text="Open", width=10, command=bt1_click)
bt1.place(x=30, y=30)

bt2 = Button(root, fg="blue", bg="pale green", text="Save", width=10, command=bt2_click)
bt2.place(x=30, y=80)

bt3 = Button(root, bg="plum1", text="Quit", width=10, command=root.quit)
bt3.place(x=580, y=675)

root.mainloop()
