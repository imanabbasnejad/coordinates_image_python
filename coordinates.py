import os
import Tkinter as tk
import cv2
import Image, ImageTk, tkFileDialog
import time
import matplotlib.pyplot as plt

def click(event):
	print ('Cordinates', event.x-20, event.y-20)
	cv.bind("<Button-1>", click)

cv = tk.Canvas()
cv.pack()
filename = tkFileDialog.askopenfilename(parent = cv)
photo = tk.PhotoImage(file = filename)
cv.pack(side = 'top', fill = 'both', expand = 'yes')
image = cv.create_image(20,20, image = photo, anchor = 'nw')
cv.tag_bind(image, '<ButtonPress-1>', click)       

cv.mainloop()
