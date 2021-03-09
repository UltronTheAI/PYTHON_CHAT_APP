from tkinter import *
import time

file = open('chat_y.txt', 'w')
file.write(f'I, JOIN THE CHAT.')
file.close()
chat = Tk()
chat.title('chat app')
chat.geometry('800x800+700+300')
chat.configure(bg='yellow')
# chat.overrideredirect(1)
chat.wm_attributes('-transparentcolor', 'yellow')
chat.attributes('-alpha', 0.50)


def send_d(e=''):
    file = open('chat_y.txt', 'w')
    file.write(f'{E.get()}')
    file.close()
    global lx, ly, ly1, lx1
    ly += 30
    ly1 += 30
    L = Label(text=E.get(), fg='red')
    L.place(x=lx1, y=ly1)
    E.delete(0, END)
    if ly > 750:
        o = Label(bg='yellow', width=200, height=800)
        o.place(x=0, y=30)
        ly = 0
        ly1 = 0


E = Entry(bg='white', border=0, width=200)
E.place(x=0, y=0)
E.bind('<Return>', send_d)

i = 0
text = ''
lx = 200
ly = 30
lx1 = 0
ly1 = 30

while True:
    chat.update()
    i += 1
    chat.update_idletasks()
    time.sleep(0.01)
    print(i)
    file = open('chat.txt', 'r')
    fr = file.read()
    file.close()
    if fr in text:
        if ly > 750:
            o = Label(bg='yellow', width=200, height=800)
            o.place(x=0, y=30)
            ly = 0
            ly1 = 0
    else:
        ly += 30
        ly1 += 30
        L = Label(text=fr)
        L.place(x=lx, y=ly)
        text = fr
        if ly > 750:
            o = Label(bg='yellow', width=200, height=800)
            o.place(x=0, y=30)
            ly = 0
            ly1 = 0

chat.mainloop()
