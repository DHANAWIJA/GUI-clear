#DELETE FUNCTION

from tkinter import*

def delete():
    myentry.delete(0,END)

root=Tk()
root.geometry('180x120')

myentry=Entry(root,width=30)
myentry.pack(pady=10)

mybutton=Button(root,text="Delete",command=delete)
mybutton.pack(pady=10)

root.mainloop()
