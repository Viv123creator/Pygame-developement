import tkinter as tk

def weight_converter():
    kg=float(e1.get())
    grams=kg*1000
    ounces=kg/35.274
    pounds=kg/2.205
    e2.delete(0, tk.END)
    e3.delete(0, tk.END)
    e4.delete(0, tk.END)

    e2.insert(0, ounces)
    e3.insert(0, pounds)
    e4.insert(0, grams)




mainscreen=tk.Tk()
mainscreen.title("Weight converter")
mainscreen.geometry("1000x1000")
mainscreen.configure(bg="white")

l1=tk.Label(text="weight converter", font=("Arial", 20), width=20, height=1, bg="white", fg="black")
l1.place(x=300, y=20)

l2=tk.Label(text="Enter your weight in kilograms: ", width=40, height=1, bg="white", fg="black")
e1=tk.Entry(width=20, bg="white", fg="black")

l2.place(x=100, y=120)
e1.place(x=400, y=120)

b1=tk.Button(text="Convert", width=20, height=1, bg="green", fg="black", command=weight_converter)
b1.place(x=350, y=200)

l3=tk.Label(text="Ounces:", width=30, height=2, bg="white", fg="black")
l4=tk.Label(text="Pounds:", width=30, height=2, bg="white", fg="black")
l5=tk.Label(text="Grams:", width=30, height=2, bg="white", fg="black")

e2=tk.Entry(width=20, bg="white", fg="black")
e3=tk.Entry(width=20, bg="white", fg="black")
e4=tk.Entry(width=20, bg="white", fg="black")

l3.place(x=100, y=300)
l4.place(x=100, y=400)
l5.place(x=100, y=500)

e2.place(x=300, y=300)
e3.place(x=300, y=400)
e4.place(x=300, y=500)









mainscreen.mainloop()