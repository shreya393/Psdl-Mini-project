from tkinter import *
#from tkinter import tkk
from PIL import ImageTk,Image

root=Tk()
root.title("BMI Calculator")
root.geometry("470x580+300+200")
root.resizable(False,False)
root.configure(bg="#f0f1f5")

#icons
root.iconbitmap('c:/PSDL/icon.ico')

#top image
my_img=ImageTk.PhotoImage(Image.open("top.png"))
my_label=Label(image=my_img)
my_label.pack()

# bottom box
Label(root,width=72,height=18,bg="#F3CCFF").pack(side=BOTTOM)

#two boxes
box=ImageTk.PhotoImage(Image.open("box.png"))
Label(root,text="Height",image=box,bg="black").place(x=20,y=100)
Label(root,text="Weight",image=box,bg="black").place(x=240,y=100)

#scale
scale=ImageTk.PhotoImage(Image.open("scale.png"))
Label(root,image=scale,bg="lightblue").place(x=20,y=310)


#man image
secondimage=Label(root,bg="lightblue")
secondimage.place(x=70,y=530)


#button
label1=Label(root,font="arial 60 bold",bg="lightblue",fg="#fff")
label1.place(x=125,y=305)

label2=Label(root,font="arial 20 bold",bg="lightblue",fg="#3b3a3a")
label2.place(x=280,y=430)

label3=Label(root,font="arial 10 bold",bg="lightblue")
label3.place(x=200,y=500)

def BMI():
	h=float(Height.get())
	w=float(Weight.get())

	#convert height into meters
	m=h/100
	bmi=float(w/m*m)
	label1.config(text=bmi)

	if bmi<=18.5:
		label2.config(text="Underweight!!")
		label3.config(text="you have lower body weight tha normal!")

	elif bmi<=18.5 and bmi<=25:
		label2.config(text="NORMAl:)!!")
		label3.config(text="Boi! U are healthy!!")

	elif bmi>25 and bmi<=30:
		label2.config(text="Overweight:(!!")
		label3.config(text="U are a bit overweight!!")

	else: 
		label2.config(text="OBESEE!!")
		label3.config(text="Health risk may arise,doctor may\n advise you to loose some weight!!")



Button(root,text="View Report", width=10,height=2,font="arial 10 bold",bg="#1f6e68",fg="white",command=BMI).place(x=320,y=340)


###########SLIDER 1###########
current_value=DoubleVar()
def get_current_value():
	return '{: .2f}'.format(current_value.get())

def slider_changed(event):
	Height.set(get_current_value())


size=int(float(get_current_value()))
img=(Image.open("human.png"))
resized_image=img.resize((50,10+size))
photo2=ImageTk.PhotoImage(resized_image)
secondimage.config(image=photo2)
secondimage.place(x=70,y=550-size)
secondimage.image=photo2



###########SLIDER 2###########
current_value2=DoubleVar()
def get_current_value2():
	return '{: .2f}'.format(current_value2.get())

def slider_changed2(event):
	Weight.set(get_current_value2())



#changing bg colour of sllider
#height slider
slider=Scale(root,from_=0,to=220,orient="horizontal",background="lightblue",
	command=slider_changed,variable=current_value)
slider.place(x=80,y=250)

#weight slider
slider2=Scale(root,from_=0,to=220,orient="horizontal",background="lightblue",
	command=slider_changed2,variable=current_value2)
slider2.place(x=300,y=250)




#entry box
Height=StringVar()
Weight=StringVar()
#to align the text to the centre
height=Entry(root,textvariable=Height,width=5,font="arial 50",bg="#fff",fg="#000",bd=0,justify=CENTER)
height.place(x=35,y=160)
Height.set(get_current_value())

weight=Entry(root,textvariable=Weight,width=5,font="arial 50",bg="#fff",fg="#000",bd=0,justify=CENTER)
weight.place(x=255,y=160)
Weight.set(get_current_value2())





root.mainloop()
