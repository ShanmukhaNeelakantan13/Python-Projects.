from tkinter import*
from time import *
def update():
    time=strftime('%I:%M:%S %p')
    timelabel.config(text=time)
    timelabel.after(1000,update)
window=Tk()
window.title('Digital Clock')
window.geometry('500x200')
window.configure(bg='grey')
timelabel=Label(window,text=time,font=('Arial',50),foreground='black',background='grey')
timelabel.pack()
date=strftime('%B %d,%Y')
date=Label(window,text=date,font=('Ink Free',30),background='grey',foreground='black')
date.pack()
day=strftime('%A')
day=Label(window,text=day,font=('Ink Free',30),background='grey',foreground='black')
day.pack()
update()
window.mainloop()