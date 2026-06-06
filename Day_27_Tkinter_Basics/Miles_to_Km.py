from tkinter import *

def calc():
    miles = int(input.get())
    km = round(miles * 1.609344)
    kmNum_label.config(text=f"{km}")
    
window = Tk()
window.title("Miles to Km Converter")
# window.minsize(width=250,height=100)
window.config(padx=25,pady=25)

input = Entry(width=10)
input.grid(column=1,row=0)

mile_label=Label(text="Miles")
mile_label.grid(column=2,row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0,row=1)

kmNum_label = Label(text=" ")
kmNum_label.grid(column=1,row=1)

km_label = Label(text="Km")
km_label.grid(column=2,row=1)

button = Button(text="Calculate",command=calc)
button.grid(column=1,row=3)







window.mainloop()