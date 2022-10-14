

from tkinter import *
from AssnCL22_Classes import *
from tkinter import Image
from AssnCl22_Gui2 import *


window = Tk()
#window= Toplevel()
window.geometry("450x550")
window.title("Welcome")

#============================================================
# Event Handling Methods

def displayChange():
    global current
    display(current)

def display(index):
    print('here')
    global current
    global product
    product = productList[index]
    current = index
    entry2.delete(0, END)
    entry2.insert(END, product.readName())
    entry3.delete(0, END)
    entry3.insert(END, product.readAge())
    entry4.delete(0, END)
    entry4.insert(END, product.readCity())
    entry5.delete(0, END)
    entry5.insert(END, product.readCountry())
    entry6.delete(0, END)
    entry6.insert(END, product.readWins())
    productType = product.readType()
    productTypeVar.set(productType)

    available = product.readFit()
    if (available==True):
        var_cb1.set(1)
    else:
        var_cb1.set(0)
    entry7.delete(0, END)
    entry7.insert(END, product.readDescriptionPart1())
    entry8.delete(0, END)
    entry8.insert(END, product.readDescriptionPart2())
    entry9.delete(0, END)
    entry9.insert(END, product.readDescriptionPart3())


# new Methods

def markAvail():
    product.markFit()
    display(current)

def markNotAvail():
    product.markUnfit()
    display(current)

def updateCmd():
    global current
    global product
    product = productList[current]
    newPrice = int(entry11.get())
    product.stepWins(newPrice)
    display(current)




def orderCmd():
    global current
    global product
    product = productList[current]
    product.stepWins(int(product.readWins()) + 1)
    display(current)

def nextCmd():
    global current
    if (current<(len(productList)-1) ):
        current += 1
        display(current)

def prevCmd():
    global current
    if (current > 0):
        current -= 1
        display(current)


def closeCmd():
    exit()



def clearCmd():
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)
    entry6.delete(0, END)
    entry7.delete(0, END)
    entry8.delete(0, END)
    entry9.delete(0, END)
    productTypeVar.set("Runner")
    var_cb1.set(1)




def insertCmd():
    name=entry2.get()
    price=int(entry3.get())
    make=entry4.get()
    location=entry5.get()
    description1=entry7.get()
    description2=entry8.get()
    description3=entry9.get()


    newType = productTypeVar.get()
    newProduct = Runner(name,price, make,location,description1,description2,description3)
    if (newType=='Swimmer'):
        newProduct = Swimmer(name, price, make, location, description1,description2,description3)
    elif (newType=='Cyclist'):
        newProduct = Cyclist(name, price, make, location, description1,description2,description3)

    productList.append(newProduct)
    display(len(productList)-1)


# End of Method Declarations
#========================================================================



# Definitions
#=====================================================================
product1 = Runner("Cian Martin", 21, "Tullamore", "Ireland",  "10000m", "Nike", True)
product2 = Runner("Jakob Ingebrigtsen", 21, "Sandnes", "Norway",  "1500m", "Nike", True)
product3 = Swimmer("Michael Phelps", 36, "Maryland", "Usa",  "Breast Stroke", "Speedo", True)
product4 = Swimmer("Katie Ledecky", 24, "Washingtion D.C", "Usa",  "Freestyle", "Adidas", True)
product5 = Cyclist("Christopher Froome", 36, "Nairobi",  "British",  "Road", "Cube", "SKY Cycling")
product6 = Cyclist("Marianne Vos", 34, "S-Hertogenbosch",  "Netherlands",  "Road", "Giant", "Jumbo Cycling")
productList=[product1, product2,product3 ,product4, product5,product6]
global current     # current product
global product

product = productList[0]  # initialize to first student

#========= End of Definitions ============================

#=======================================================
# Menu to Add New Student
menu1 = Menu(window) #MenuBar
window.config(menu=menu1)
subm1=Menu(menu1)  #Menu
menu1.add_cascade(label="Admin", menu=subm1)
subm1.add_command(label="mark fit",  font=("arial", 11, "bold"),command = markAvail)   # menu item
subm1.add_command(label="mark not fit", font=("arial", 11, "bold"), command = markNotAvail)

#======= End of Menu Definition ============================

canvas = Canvas(window, width=550, height=490)
canvas.grid(row=0, column=0)
img = PhotoImage(file='Tour.png')
#canvas.create_image(440, 200, anchor=CENTER, image=img)
canvas.create_image(340, 360, image=img)
canvas.place(x=10,y=10)

frame = Frame(window, width=200, height=200)
frame.place(x=90,y=80)

label1 = Label(canvas, text="Athlete Application", fg="blue",bg="yellow", font=("arial", 16, "bold"))
label1.place(x=90, y=30)                            # place on screen


label2 = Label(frame, text="Name", fg="blue",width=15, font=("arial", 10, "bold"))   #
label2.grid(row=0, column=0, sticky=W+E)

entry2 = Entry(frame)
entry2.insert(END, '0')
entry2.grid(row=0, column=1, sticky=W+E)

label3 = Label(frame, text="Age", fg="blue",width=15, font=("arial", 10, "bold"))   #
label3.grid(row=1, column=0, sticky=W+E)

entry3 = Entry(frame)
entry3.insert(END, '0')
entry3.grid(row=1, column=1, sticky=W+E)

label4 = Label(frame, text="City", fg="blue",width=15, font=("arial", 10, "bold"))   #
label4.grid(row=2, column=0, sticky=W+E)

entry4 = Entry(frame)
entry4.insert(END, '0')
entry4.grid(row=2, column=1, sticky=W+E)


label5 = Label(frame, text="Country", fg="blue",width=15, font=("arial", 10, "bold"))   #
label5.grid(row=3, column=0, sticky=W+E)

entry5 = Entry(frame)
entry5.insert(END, '0')
entry5.grid(row=3, column=1, sticky=W+E)

label6 = Label(frame, text="Wins", fg="blue",width=15, font=("arial", 10, "bold"))   #
label6.grid(row=4, column=0, sticky=W+E)

entry6 = Entry(frame)
entry6.insert(END, '0')
entry6.grid(row=4, column=1, sticky=W+E)

label7 = Label(frame, text="Type", fg="blue",width=15, font=("arial", 10, "bold"))   #
label7.grid(row=5, column=0, sticky=W+E)

list1=['Runner','Swimmer','Cyclist']
productTypeVar = StringVar()
combo1= OptionMenu(frame, productTypeVar, *list1)
productTypeVar.set("Runner")
combo1.grid(row=5,column=1, sticky=W+E)


var_cb1 = IntVar()  # 0 unchecked, 1 checked
cb1 = Checkbutton(frame, text="Fit", variable=var_cb1)
cb1.grid(row=6,column=0,columnspan=2)
#---------------------------

entry7 = Entry(frame)
entry7.insert(END, '')
entry7.grid(row=7, column=0, columnspan=2, sticky=W+E)

entry8 = Entry(frame)
entry8.insert(END, '')
entry8.grid(row=8, column=0, columnspan=2, sticky=W+E)

entry9 = Entry(frame)
entry9.insert(END, '')
entry9.grid(row=9, column=0, columnspan=2, sticky=W+E)



labelBlank = Label(frame, text=" ", fg="blue",width=15, font=("arial", 10, "bold"))   #
labelBlank.grid(row=10, column=0, columnspan=2,sticky=W+E)

button5 = Button(frame, text="Next", fg="black", font=("arial", 10, "bold"), command=nextCmd)
button5.grid(row=11, column=0, sticky=W+E)

button6 = Button(frame, text="Prev", fg="black", font=("arial", 10, "bold"), command=prevCmd)
button6.grid(row=11, column=1, sticky=W+E)

button7 = Button(frame, text="Clear", fg="black", font=("arial", 10, "bold"), command=clearCmd)
button7.grid(row=12, column=0, sticky=W+E)

button8 = Button(frame, text="InsertAthlete", fg="black", font=("arial", 10, "bold"), command=insertCmd)
button8.grid(row=12, column=1, sticky=W+E)

button9 = Button(frame, text="StepWins", fg="black", font=("arial", 10, "bold"), command=orderCmd)
button9.grid(row=13, column=0, sticky=W+E)



button10 = Button(frame, text="Exit", fg="black", font=("arial", 10, "bold"), command=closeCmd)
button10.grid(row=13, column=1, sticky=W+E)

labelBlank2 = Label(frame, text=" ", fg="blue",width=15, font=("arial", 10, "bold"))   #
labelBlank2.grid(row=14, column=0, columnspan=2,sticky=W+E)

button11 = Button(frame, text="Reset Wins", fg="black", font=("arial", 10, "bold"), command=updateCmd)
button11.grid(row=15, column=0, sticky=W+E)

entry11 = Entry(frame)
entry11.insert(END, '1')
entry11.grid(row=15, column=1,  sticky=W+E)

button12 = Button(frame, text="displayAllItems", fg="black", font=("arial", 11, "bold"), command=lambda : displayDialog(window, productList))
button12.grid(row=16, column=0, columnspan=2, sticky=W+E)





display(0)









mainloop()




