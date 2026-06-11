import tkinter as tk



def convert_currency():
    dollars=int(e1.get())
    rupees=dollars*95.8
    rupees=round(rupees, 2)
    t1.delete("1.0", tk.END)
    t1.insert("1.0", rupees)

mainscreen=tk.Tk()
mainscreen.title("Currency Converter")
mainscreen.geometry("300x200")
mainscreen.configure(bg="white")

l1=tk.Label(text="Enter USD($): ", width=20, height=1, bg="white", fg="black")
e1=tk.Entry(width=20, bg="white", fg="black")
b1=tk.Button(text="Convert to INR", width=20, height=1, bg="green", fg="black", command=convert_currency)


l2=tk.Label(text="Result in INR: ", width=20, height=1, bg="white", fg="black")
t1=tk.Text(width=20, height=1, bg="white", fg="black")

l1.place(x=-20, y=20)
e1.place(x=100, y=20)
b1.place(x=70, y=70)

l2.place(x=-20, y=120)
t1.place(x=100, y=120)


mainscreen.mainloop()