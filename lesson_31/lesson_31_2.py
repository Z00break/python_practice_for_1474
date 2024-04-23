from tkinter import Tk, Button, Entry, Label, LEFT, Frame


def hello():
    name = entry_name.get()
    age = entry_age.get()
    text = "привет " + name + " " + age
    # print(int(age))
    label.configure(text=text)
    label.configure(width=20)
    entry_name.delete(0, "end")
    entry_age.delete(0, "end")


root = Tk()
root.title("моё приложение")
root.geometry("600x200+100+0")
root.resizable(False, False)

name_frame = Frame(root)
age_frame = Frame(root)
start = Button(root, text="start", background="red", command=hello, width=10, relief="ridge")
entry_name = Entry(name_frame)
entry_age = Entry(age_frame)
label = Label(root, relief="raised", font=15)
label_name = Label(name_frame, text="Введите имя ", width=20, anchor="e")
label_age = Label(age_frame, text="Введите возраст ", width=20, anchor="e")

name_frame.pack(pady=10)
label_name.pack(side=LEFT)
entry_name.pack()
age_frame.pack(pady=10)
label_age.pack(side=LEFT)
entry_age.pack()
start.pack()
label.pack(padx=10, pady=5)


root.mainloop()
