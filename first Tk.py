import tkinter as tk

from tkinter import messagebox 

def show_messagebox():
    messagebox.showinfo("Details saved", "Your data has been submitted.")

mainscreen=tk.Tk()
mainscreen.title("my first screen")
mainscreen.geometry("800x800")
mainscreen.configure(bg="black")

l1=tk.Label(text="enter your name:", width=20, height=1, bg="red", fg="blue")
l1.place(x=50, y=50 )
e1=tk.Entry(width=20, bg="white", fg="blue")
e1.place(x=200, y=50)

l2=tk.Label(text="enter your age:", width=20, height=1, bg="red", fg="blue")
e2=tk.Spinbox(width=20, from_=0, to=100)

l2.place(x=50, y=100)
e2.place(x=200, y=100)

l3=tk.Label(text="enter your adress:", width=20, height=1, bg="red", fg="blue")
l3.place(x=50, y=200)

t1=tk.Text(width=20, height=4, bg="white", fg="blue")
t1.place(x=200, y=200)

l4=tk.Label(text="select your gender:", width=20, height=1, bg="red", fg="blue")
l4.place(x=50, y=300)

r1=tk.Radiobutton(text="female", value=1)
r1.place(x=200, y=300)
r2=tk.Radiobutton(text="male", value=0)
r2.place(x=300, y=300)

l5=tk.Label(text="select known languages:", width=20, height=1, bg="red", fg="blue")
l5.place(x=50, y=400)

c1=tk.Checkbutton(text="English", onvalue=1, offvalue=0)
c1.place(x=200, y=400)

c2=tk.Checkbutton(text="Hindi", onvalue=1, offvalue=0)
c2.place(x=300, y=400)

c3=tk.Checkbutton(text="French", onvalue=1, offvalue=0)
c3.place(x=400, y=400)

b1=tk.Button(text="submit", width=20, height=1, bg="green", fg="black", command=show_messagebox)
b1.place(x=300, y=650)


l6=tk.Label(text="select the coding languages you know:", width=20, height=1, bg="red", fg="blue")
l6.place(x=50, y=500)

l7=tk.Label(text="Rate yourself:", width=20, height=1, bg="red", fg="blue")
l7.place(x=50, y=600)

coding_languages=["c+", "Java", "Typescript", "Python", "c++"]

lb1=tk.Listbox(width=50, height=5)

lb1.place(x=200, y=500)

for i in coding_languages:
    lb1.insert(tk.END, i)

s1=tk.Scale(from_=0, to=100, orient=tk.HORIZONTAL)

s1.place(x=200, y=600)











mainscreen.mainloop()