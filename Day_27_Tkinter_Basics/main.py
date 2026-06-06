import tkinter


def button_clicked():
    my_label["text"] = input.get()
    # my_label.config(text="Clicked")


window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500,height=300)
window.config(padx=50,pady=50)

my_label = tkinter.Label(text="I Am a Label",font=("Arial",21,"bold"))
my_label.grid(column=0,row=0)

button = tkinter.Button(text="CLick",command=button_clicked)
button.grid(column=1,row=1)

button2 = tkinter.Button(text="New_CLick")
button2.grid(column=2,row=0)

input = tkinter.Entry(width=10)
input.grid(column=3,row=2)




window.mainloop()