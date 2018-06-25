from tkinter import filedialog
from tkinter import*
import cv2

def img_browse():
	filename = filedialog.askopenfilename(initialdir = "/home/david",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
	e1.delete(0,END)
	e1.insert(END,filename)
	data = image_dir.get().split("/")
	global img
	img = cv2.imread(data[-1],1)
	image_height=img.shape[0]
	image_width=img.shape[1]
	e2.delete(0,END)
	e2.insert(END,image_height)
	e3.delete(0,END)
	e3.insert(END,image_width)
		

def save_image():
	r_img=cv2.resize(img, (int(new_width.get()),int(new_height.get())))
	cv2.imwrite("resized.jpg",r_img)

def bw_image():
	bw_img=cv2.resize(img, (int(new_width.get()),int(new_height.get())))
	cv2.imwrite("resized_bw.jpg",bw_img)

window=Tk()
window.title("Image Resizer")

l1=Label(window,text="Browse Image")
l1.grid(row=0,column=0)
l2=Label(window,text="Height")
l2.grid(row=2,column=0)
l3=Label(window,text="Width")
l3.grid(row=2,column=2)
l2=Label(window,text="Enter Height")
l2.grid(row=4,column=0)
l3=Label(window,text="Enter Width")
l3.grid(row=4,column=2)
l4=Label(window,text="Image Details:")
l4.grid(row=1,column=0)
l5=Label(window,text="Resized Image Details:")
l5.grid(row=3,column=0)

image_dir=StringVar()
e1=Entry(window,textvariable=image_dir)
e1.grid(row=0,column=1)

image_height=StringVar()
e2=Entry(window,textvariable=image_height)
e2.grid(row=2,column=1)

image_width=StringVar()
e3=Entry(window,textvariable=image_width)
e3.grid(row=2,column=3)

new_height=StringVar()
e4=Entry(window,textvariable=new_height)
e4.grid(row=4,column=1)

new_width=StringVar()
e5=Entry(window,textvariable=new_width)
e5.grid(row=4,column=3)

b1=Button(window,text="Browse Files",width =12,command=img_browse)
b1.grid(row=0,column=2)

b2=Button(window,text="Save Image",width =12,command=save_image)
b2.grid(row=5,column=0)

b3=Button(window,text="Save in B&W",width =12,command=bw_image)
b3.grid(row=5,column=1)

b4=Button(window,text="Close Window",width =12,command=window.destroy)
b4.grid(row=5,column=2)

window.mainloop()# Image_resizer
