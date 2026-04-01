from tkinter import *

class Person:
    def __init__(self, first_name, last_name, age, mobile_phone):
        """Function defines Person object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.mobile_phone = mobile_phone
        self.mobile_phone = "Yes" if self.mobile_phone == 1 else "No"

class GUI:
    def __init__(self, parent):
        """Function establishes structure of GUI, two frames which can alternate"""
        self.parent = parent
        self.people = []

        self.f_input = Frame(parent)
        self.f_show = Frame(parent)

        # input frame
        self.fil1 = Label(self.f_input, text="Collecting person data")
        self.fil1.grid(column=0, row=0)
        
        self.fib1 = Button(self.f_input, text="View all", command=self.switch)
        self.fib1.grid(column=1, row=0, columnspan=2)

        self.fil2 = Label(self.f_input, text="First name:")
        self.fil2.grid(column=0, row=1, sticky=W)

        e1 = StringVar()
        self.fie1 = Entry(self.f_input, textvariable=e1)
        self.fie1.grid(column=1, row=1, columnspan=2)

        self.fil3 = Label(self.f_input, text="Last name:")
        self.fil3.grid(column=0, row=2, sticky=W)

        e2 = StringVar()
        self.fie2 = Entry(self.f_input, textvariable=e2)
        self.fie2.grid(column=1, row=2, columnspan=2)

        self.fil4 = Label(self.f_input, text="Age:")
        self.fil4.grid(column=0, row=3, sticky=W)

        e3 = IntVar(value=None)
        self.fie3 = Entry(self.f_input, textvariable=e3)
        self.fie3.grid(column=1, row=3, columnspan=2)

        self.fil5 = Label(self.f_input, text="Mobile phone owned?")
        self.fil5.grid(column=0, row=4, sticky=W)

        self.rbv = IntVar(value=0)
        self.firb1 = Radiobutton(self.f_input, variable=self.rbv, value=1, text="Yes")
        self.firb2 = Radiobutton(self.f_input, variable=self.rbv, value=0, text="No")

        self.firb1.grid(column=1, row=4)
        self.firb2.grid(column=2, row=4)

        self.fib2 = Button(self.f_input, text="Add data", command=self.add_data)
        self.fib2.grid(column=0, row=5, columnspan=3)


        # show frame
        self.current_person = 0
        self.fsl1 = Label(self.f_show, text="Displaying person data")
        self.fsl1.grid(column=0, row=0, columnspan=3)
        
        self.fsb1 = Button(self.f_show, text="Add new person", command=self.switch)
        self.fsb1.grid(column=3, row=0, columnspan=3)

        self.fsl2 = Label(self.f_show, text="First name:")
        self.fsl2.grid(column=0, row=1, columnspan=3, sticky=W)

        self.fsl3 = Label(self.f_show, text=self.people[self.current_person].first_name if self.people else "")
        self.fsl3.grid(column=3, row=1, columnspan=3, sticky=W)

        self.fsl4 = Label(self.f_show, text="Last name:")
        self.fsl4.grid(column=0, row=2, columnspan=3, sticky=W)

        self.fsl5 = Label(self.f_show, text=self.people[self.current_person].last_name if self.people else "")
        self.fsl5.grid(column=3, row=2, columnspan=3, sticky=W)

        self.fsl6 = Label(self.f_show, text="Age:")
        self.fsl6.grid(column=0, row=3, columnspan=3, sticky=W)

        self.fsl7 = Label(self.f_show, text=self.people[self.current_person].age if self.people else "")
        self.fsl7.grid(column=3, row=3, columnspan=3, sticky=W)

        self.fsl8 = Label(self.f_show, text="Mobile phone owned?")
        self.fsl8.grid(column=0, row=4, columnspan=3, sticky=W)

        self.fsl9 = Label(self.f_show, text=self.people[self.current_person].mobile_phone if self.people else "")
        self.fsl9.grid(column=3, row=4, columnspan=3, sticky=W)

        self.fsb2 = Button(self.f_show, text="Previous", command=self.prev, state=DISABLED)
        self.fsb2.grid(column=0, row=5, columnspan=2, sticky=W)
        
        self.fsl10 = Label(self.f_show, text=f"{self.current_person+1}/{len(self.people)}")
        self.fsl10.grid(column=2, row=5, columnspan=2)

        self.fsb3 = Button(self.f_show, text="Next", command=self.next, state=DISABLED)
        self.fsb3.grid(column=4, row=5, columnspan=2, sticky=E)

        self.f_input.pack()

        self.fie1.focus()
        self.fib1.configure(state=DISABLED)


    def prev(self):
        """Shifts to the previous person"""
        self.current_person -= 1
        if self.current_person < 0:
            self.current_person = len(self.people)-1
        self.shift()


    def next(self):
        """Shifts to the next person"""
        self.current_person += 1
        if self.current_person > len(self.people)-1:
            self.current_person = 0
        self.shift()


    def switch(self):
        """Changes the frame that is shown"""
        if self.f_input.winfo_ismapped():
            self.f_input.pack_forget()
            self.f_show.pack()
            self.shift()
        else:
            self.f_show.pack_forget()
            self.f_input.pack()


    def add_data(self):
        """Adds data to list and clears Entry widgets and resets Radiobuttons"""
        self.people.append(Person(self.fie1.get(), self.fie2.get(), self.fie3.get(), self.rbv.get()))
        self.fie1.delete(0, END)
        self.fie2.delete(0, END)
        self.fie3.delete(0, END)
        self.rbv.set(0)
        self.fie1.focus()
        self.fib1.configure(state=NORMAL)


    def shift(self):
        """Reconfigures shown text to match with the current person"""
        self.fsl3.configure(text=self.people[self.current_person].first_name if self.people else "")
        self.fsl5.configure(text=self.people[self.current_person].last_name if self.people else "")
        self.fsl7.configure(text=self.people[self.current_person].age if self.people else "")
        self.fsl9.configure(text=self.people[self.current_person].mobile_phone if self.people else "")
        self.fsl10.configure(text=f"{self.current_person+1}/{len(self.people)}" if self.people else "0/0")

        if len(self.people) > 1:
            self.fsb2.configure(state=NORMAL)
            self.fsb3.configure(state=NORMAL)



if __name__ == "__main__":
    root = Tk()
    root.geometry("300x250")
    g = GUI(root)

    root.mainloop()