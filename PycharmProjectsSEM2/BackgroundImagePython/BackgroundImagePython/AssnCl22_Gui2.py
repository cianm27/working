

from tkinter import *

from AssnCL22_Classes import *

def displayDialog(window, product_list):
    window2 = Toplevel(window)
    window2.geometry("1300x650")
    window2.title("Add Dialog")
    productList = product_list





#============================================================
# Event Handling Methods

    def displayAll():

        for product in productList:
            print('hello')
            line=product.readType()
            line+= '\t\t'+product.readName()
            line+= '\t\t'+ str(product.readAge())
            line += '\t\t' + str(product.readCity())
            line += '\t\t' + product.readDescriptionPart1()
            line += '\t\t\t\t' + product.readDescriptionPart2()
            line += '\n\n'
            text.insert(END, line)
        print(line)



    def closeEvent():
        window2.destroy()

    button6 = Button(window2, text="Close", fg="black", font=("arial", 12, "bold"), command=closeEvent)
    button6.place(x=10, y=10)

    text = Text(window2, undo=True, height=34, width=150)
    text.place(x=20, y=60)

    displayAll()














