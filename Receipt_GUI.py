from tkinter import *

window = Tk()

window.geometry("400x400")

def displayMsg():
    item = entryItem.get()
    price = entryPrice.get()
    price = float(price)
    entry = "%-25s $%10.2f\n" % (item, price)
    T.insert(END, entry) 

# Create label 
l = Label(window, text = "Receipt") 
l.pack() 

# Create text widget and specify size. 
T = Text(window, height = 10, width = 42) 
T.pack()  

l1 = Label(window, text="Item name: ")
l2 = Label(window, text="Item price: ")
entryItem = Entry(window)
entryPrice = Entry(window)

#position the UI
l1.pack()  
entryItem.pack()  
l2.pack() 
entryPrice.pack()  

#create and place button
button1 = Button(window, text="Start", bg="lightgreen", command=displayMsg)
button1.pack(side='top', expand=YES)

window.mainloop()