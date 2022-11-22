from tkinter import *

def next_1():
    destroy_object = [welcome_lbl, main_lbl, next_btn]
    for object_name in destroy_object:
        object_name.destroy()

tk = Tk()
tk.title('Разрушители')
main_lbl = Label(tk, text='Приветствую в "Разрушителях"', fg='red', font='Arial 20')
welcome_lbl = Label(tk, text='Бродя по лесу ты наткнулся на своего первого противника - ВОЛКА'
                             '\n эти опасные твари никогда не отступают, так что В БОЙ!!!!!',
                    fg='black', font='Arial 20')
next_btn = Button(tk, text='Далее', width=30, height=5, font=20, command=next_1)
main_lbl.pack()
welcome_lbl.pack()
next_btn.pack()
tk.mainloop()