from tkinter import *

root = Tk()
# the_Label = Label(root, text="Chemical Compound Nomenclature")
# the_Label.pack()
# topFrame = Frame(root)
# topFrame.pack()
# bottomFrame = Frame(root)
# bottomFrame.pack(side=BOTTOM)
#
# button1 = Button(topFrame, text="Button 1", fg="red")
# button2 = Button(topFrame, text="Button 2", fg="yellow")
# button3 = Button(topFrame, text="Button 3", fg="green")
# button4 = Button(bottomFrame, text="Button 4", fg="purple")
#
# button1.pack(side=LEFT)
# button2.pack(side=LEFT)
# button3.pack(side=LEFT)
# button4.pack(side=BOTTOM)
label1_1 = Label(root, text="Name")
label1_2 = Label(root, text="Password")
entry1_1 = Entry(root)
entry1_2 = Entry(root)

label1_1.grid(row=0, sticky=E)
label1_2.grid(row=1, sticky=E)

entry1_1.grid(row=0, column=1)
entry1_2.grid(row=1, column=1)

c = Checkbutton(root, text="Keep me logged in")
c.grid(columnspan=2)

root.mainloop()
