from tkinter import *

root=Tk()
root.title("calculator")
root.geometry("490x240")
eq=StringVar()
get=""
f=Frame(root,bg="black",padx=20,pady=10)
e=Entry(f,background="gray",width=50,borderwidth=10,textvariable=eq,border=15)
e.grid(row=0,column=0,columnspan=3)

def clear():
    global get
    eq.set("")
    get = ""
def buttonseter(num):
    global get

    get =get+str(num)
    eq.set(get)
def buttoneq():
    global get
    try:

        tot=str(eval(get))
        eq.set(tot)
        get=""
    except:
        eq.set("error")
        get=""
def delete():
    global get
    eq.set(get[:-1])
    get=get[:-1]

butcl=Button(f,text="c",background="white",padx=50,pady=10,command=clear)
but1=Button(f,text="1",background="white",padx=50,pady=10,command=lambda:buttonseter(1))
but2=Button(f,text="2",background="white",padx=50,pady=10,command=lambda:buttonseter(2))
but3=Button(f,text="3",background="white",padx=50,pady=10,command=lambda:buttonseter(3))
but4=Button(f,text="4",background="white",padx=50,pady=10,command=lambda:buttonseter(4))
but5=Button(f,text="5",background="white",padx=50,pady=10,command=lambda:buttonseter(5))
but6=Button(f,text="6",background="white",padx=50,pady=10,command=lambda:buttonseter(6))
but7=Button(f,text="7",background="white",padx=50,pady=10,command=lambda:buttonseter(7))
but8=Button(f,text="8",background="white",padx=50,pady=10,command=lambda:buttonseter(8))
but9=Button(f,text="9",background="white",padx=50,pady=10,command=lambda:buttonseter(9))
but0=Button(f,text="0",background="white",padx=50,pady=10,command=lambda:buttonseter(0))
buteq=Button(f,text="=",background="white",padx=50,pady=10,command=buttoneq)
butplus=Button(f,text="+",background="white",padx=48,pady=10,command=lambda:buttonseter("+"))
butmyns=Button(f,text="-",background="white",padx=50,pady=10,command=lambda:buttonseter("-"))
butdiv=Button(f,text="/",background="white",padx=50,pady=10,command=lambda:buttonseter("/"))
butmul=Button(f,text="*",background="white",padx=50,pady=10,command=lambda:buttonseter("*"))
butdel=Button(f,text="del",background="white",padx=45,pady=10,command=delete)

but1.grid(row=1,column=0)
but2.grid(row=1,column=1)
but3.grid(row=1,column=2)
but4.grid(row=2,column=0)
but5.grid(row=2,column=1)
but6.grid(row=2,column=2)
but7.grid(row=3,column=0)
but8.grid(row=3,column=1)
but9.grid(row=3,column=2)
but0.grid(row=4,column=1)
butdel.grid(row=4,column=0)
buteq.grid(row=4,column=2)
butcl.grid(row=0,column=3)
butplus.grid(row=1,column=3)
butmyns.grid(row=2,column=3)
butdiv.grid(row=3,column=3)
butmul.grid(row=4,column=3)
f.grid()
root.mainloop()
