from tkinter import Tk, Button, Frame, LEFT, Label, BOTTOM

def change_text(button_text):
    # 1.получить ключ(ключ это текст на кнопки )
    # print(pressed_button)
    # 2. получаем текст,цвет
    color = RESOURCES[button_text]["color"]
    text = RESOURCES[button_text]["text"]
    print(button_text, "->", text)
    texts.configure(text=text)
    # b = buttons[0]
    # b.configure(background=color)
    for b in buttons:
        b_text = b.cget("text")
        if b_text == button_text:
            b.configure(background=color)
            b.configure(foreground="white")
        else:
            b.configure(background="white")
            b.configure(foreground=RESOURCES[b_text]["color"])
root = Tk()
root.title("Python_Helper")
root.geometry("800x400+200+0")
root.resizable(False, False)

buttons_frame = Frame(root)
RESOURCES = {
    "print": {"color": "purple", "text": "Название: \n print \n Описание: \n Printing output"},
    "for": {"color": "orange", "text": "Название: \n for \n Описание: \n Loops reserved word"},
    "def": {"color": "purple", "text": "Название: \n def \n Описание: \n Special word for define a function"},
    "list": {"color": "purple", "text": "Название: \n list \n Описание: \n Function to create sequence or cast other types"},
    "return": {"color": "orange", "text": "Название: \n return \n Описание: \n Reserved word for give  function results back"},
    "while": {"color": "orange", "text": "Название: \n while \n Описание: \n Reserved word for give function results back"}
}


buttons = []

texts =  Label(root, text="HELLO", anchor="center", relief="groove", border=20, width=90)

for button_text, button_data in RESOURCES.items():
    b = Button(
        buttons_frame,
        text=button_text,
        # background="red",
        foreground=button_data["color"],
        command=lambda w = button_text: change_text(w),
        width=10,
        relief="ridge"
    )
    b.pack(pady=10)
    buttons.append(b)

# buttons_frame.pack(side=LEFT)
# texts.pack(side=BOTTOM)
buttons_frame.grid(row=0, column=0)
texts.grid(row=0, column=3, padx=30)
# print(buttons)



root.mainloop()