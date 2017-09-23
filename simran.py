

# hangman game--------guessing game-----

import Tkinter
from Tkinter import *
import tkMessageBox
import Tkinter
import random

# three diffrent frames
top=Tk()

frame=Frame(top,bg='black')
frame.grid(row=0,column=0)

bframe=Frame(top)
bframe.grid(row=1,column=0,pady=30)

frameb=Frame(top)
frameb.grid(row=4,column=0,pady=30)

Var1=IntVar()
Var1.set(3)

mvar=StringVar()

global picflag

# function define to generate random pics on the screen
def randompics():
    global picflag
    Apic=picflag
    hang(Apic)

def msg(event=None):
     mainset()
     randompics()

     

#functions of buttons
def f1f():
     a=mvar.get()
     mvar.set(a+'1')
def f2f():
     a=mvar.get()
     mvar.set(a+'2')
def f3f():
     a=mvar.get()
     mvar.set(a+'3')
def f4f():
     a=mvar.get()
     mvar.set(a+'4')
def f5f():
     a=mvar.get()
     mvar.set(a+'5')
def f6f():
     a=mvar.get()
     mvar.set(a+'6')
def f7f():
     a=mvar.get()
     mvar.set(a+'7')
def f8f():
     a=mvar.get()
     mvar.set(a+'8')
def f9f():
     a=mvar.get()
     mvar.set(a+'9')
def f0f():
     a=mvar.get()
     mvar.set(a+'0')

     
def af():
     a=mvar.get()
     mvar.set(a+'A')
def bf():
     a=mvar.get()
     mvar.set(a+'B')
def cf():
     a=mvar.get()
     mvar.set(a+'C')
def df():
     a=mvar.get()
     mvar.set(a+'D')
def ef():
     a=mvar.get()
     mvar.set(a+'E')
def ff():
     a=mvar.get()
     mvar.set(a+'F')
def gf():
     a=mvar.get()
     mvar.set(a+'G')
def hf():
     a=mvar.get()
     mvar.set(a+'H')
def iif():
     a=mvar.get()
     mvar.set(a+'I')
def jf():
     a=mvar.get()
     mvar.set(a+'J')
def kf():
     a=mvar.get()
     mvar.set(a+'K')
def lf():
     a=mvar.get()
     mvar.set(a+'L')
def mf():
     a=mvar.get()
     mvar.set(a+'M')
def nf():
     a=mvar.get()
     mvar.set(a+'N')
def of():
     a=mvar.get()
     mvar.set(a+'O')
def pf():
     a=mvar.get()
     mvar.set(a+'P')
def qf():
     a=mvar.get()
     mvar.set(a+'Q')
def rf():
     a=mvar.get()
     mvar.set(a+'R')
def sf():
     a=mvar.get()
     mvar.set(a+'S')
def tf():
     a=mvar.get()
     mvar.set(a+'T')
def uf():
     a=mvar.get()
     mvar.set(a+'U')
def vf():
     a=mvar.get()
     mvar.set(a+'V')
def wf():
     a=mvar.get()
     mvar.set(a+'W')
def xf():
     a=mvar.get()
     mvar.set(a+'X')
def yf():
     a=mvar.get()
     mvar.set(a+'Y')
def zf():
     a=mvar.get()
     mvar.set(a+'Z')
def space():
     a=mvar.get()
     mvar.set(a+' ')                         

# submit function to check the guess is correct or not

def submit():
     var=mvar.get()
     global picflag
     if var==picflag[1]:
          tkMessageBox.showinfo("Event Triggered","Congratulations")
          mvar.set('')
          msg()
     else:
          tkMessageBox.showinfo("Sorry","Worng Guess")
          mvar.set('')
          num=Var1.get()
          Var1.set(num-1)
          if num==1:
               tkMessageBox.askretrycancel("Game Over","Game Over \n Click on retry to play again")
               Var1.set(3)
          
def play():
    Var1.set(3)
    msg()
    
  
def mainset():
    global picflag
    pic=[[A0,"ORANGE"],[A1,"GRAPES"],[A2,"TIGER"],[A3,"APPLE"],[A4,"MIKE"],[A5,"RHINOSORUS"],[A6,"ZEBRA"],[A7,"WATERMELON"],[A8,"AUDI"],[A9,"EAGAL"]]
    picflag=random.choice(pic)
    
#photos in database
A0=PhotoImage(file="er.gif")
A1=PhotoImage(file="grape.gif")
A2=PhotoImage(file="tiger.gif")    
A3=PhotoImage(file="apple.gif")
A4=PhotoImage(file="mike.gif")
A5=PhotoImage(file="rhino.gif")
A6=PhotoImage(file="zebra.gif")
A7=PhotoImage(file="water.gif")
A8=PhotoImage(file="audi.gif")
A9=PhotoImage(file="eagal.gif")

canvas = Canvas(frame,width = 800, height = 145)
gif1 = PhotoImage(file = 'hangm.gif')
canvas.create_image(0, 0, image = gif1, anchor = NW)
canvas.grid(row=0,column=0,padx=250,pady=20)

qu=Button(bframe,text='EXIT', relief=RAISED,width=20 ,command=top.destroy,height=1 ,activeforeground='blue', bd=4)
qu.grid(row=2,column=10,padx=30)

def hang(Apic):
    But1=Button(bframe,image=Apic[0],height=180,width=180,bd=0)
    But1.grid(row=2,column=0,rowspan=2,pady=5)   

label0 = Tkinter.Label(bframe,text="GUESS WORD ",font='Helvetica -13 bold',height=3)
label0.grid(row=2,column=1)


E1=Entry(bframe,bd=7,width=35,textvariable=mvar)
E1.grid(row=2,column=2)


submit=Button(bframe,text='OK', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4 ,bg='powderblue',command=submit)
submit.grid(row=2,column=4)

label0 = Tkinter.Label(bframe,text=E1.get(),font='Helvetica -13 bold')
label0.grid(row=2,column=3)



label1 = Tkinter.Label(bframe, text='Total number of choice : 3',font='Helvetica -13 bold',height=2)
label1.grid(row=3,column=1,columnspan=1)

label2 = Tkinter.Label(bframe, text='Remaining number of choice = ',font='Helvetica -13 bold')
label2.grid(row=3,column=2,columnspan=2)

en=Label(bframe,textvariable=Var1,width=4,bd=4,font="Times 15 bold italic")
en.grid(row=3,column=3,rowspan=1)

play=Button(bframe,text='GUESS NOW', relief=RAISED,width=30 ,height=3 ,activeforeground='red', bd=4 ,command=play)
play.grid(row=2,column=6,pady=3,padx=10)

nextp=Button(bframe,text='NEXT IMAGE', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4,command=msg)
nextp.grid(row=4,column=0,pady=20)

q=Button(frameb,text='Q', relief=RAISED,width=15 ,height=1 ,activeforeground='blue', bd=3 ,command=qf)
q.grid(row=2,column=3)
w=Button(frameb,text='W', relief=RAISED,width=15 ,height=1 ,activeforeground='blue', bd=3,command=wf)
w.grid(row=2,column=4)
e=Button(frameb,text='E', relief=RAISED,width=15 ,height=1 ,activeforeground='blue', bd=4,command=ef)
e.grid(row=2,column=5)
r=Button(frameb,text='R', relief=RAISED,width=15 ,height=1 ,activeforeground='blue', bd=4,command=rf)
r.grid(row=2,column=6)
t=Button(frameb,text='T', relief=RAISED,width=15 ,height=1 ,activeforeground='blue', bd=4,command=tf)
t.grid(row=2,column=7)
y=Button(frameb,text='Y', relief=RAISED,width=15 ,height=1 ,activeforeground='blue', bd=4 ,command=yf)
y.grid(row=2,column=8)
u=Button(frameb,text='U', relief=RAISED,width=15 ,height=1 ,activeforeground='blue', bd=4 ,command=uf)
u.grid(row=2,column=9)
i=Button(frameb,text='I', relief=RAISED,width=15 ,height=1 ,activeforeground='blue', bd=4 ,command=iif)
i.grid(row=2,column=10)
o=Button(frameb,text='O', relief=RAISED,width=15 ,height=1 ,activeforeground='blue', bd=4 ,command=of)
o.grid(row=2,column=11)
p=Button(frameb,text='P', relief=RAISED,width=15 ,height=1 ,activeforeground='blue', bd=4,command=pf)
p.grid(row=2,column=12)

a=Button(frameb,text='A', relief=RAISED,width=15 ,height=1 ,activeforeground='blue', bd=4 ,command=af)
a.grid(row=3,column=3,columnspan=2)
s=Button(frameb,text='S', relief=RAISED,width=15 ,height=1 ,activeforeground='blue', bd=4 ,command=sf)
s.grid(row=3,column=4,columnspan=2)
d=Button(frameb,text='D', relief=RAISED,width=15 ,height=1 ,activeforeground='blue', bd=4,command=df)
d.grid(row=3,column=5,columnspan=2)
f=Button(frameb,text='F', relief=RAISED,width=15 ,height=1 ,activeforeground='blue', bd=4 ,command=ff)
f.grid(row=3,column=6,columnspan=2)
g=Button(frameb,text='G', relief=RAISED,width=15 ,height=1 ,activeforeground='blue', bd=4 ,command=gf)
g.grid(row=3,column=7,columnspan=2)
h=Button(frameb,text='H', relief=RAISED,width=15 ,height=1 ,activeforeground='blue', bd=4 ,command=hf)
h.grid(row=3,column=8,columnspan=2)
j=Button(frameb,text='J', relief=RAISED,width=15 ,height=1 ,activeforeground='blue', bd=4,command=jf)
j.grid(row=3,column=9,columnspan=2)
k=Button(frameb,text='K', relief=RAISED,width=15 ,height=1 ,activeforeground='blue', bd=4,command=kf)
k.grid(row=3,column=10,columnspan=2)
l=Button(frameb,text='L', relief=RAISED,width=15 ,height=1 ,activeforeground='blue', bd=4,command=lf)
l.grid(row=3,column=11,columnspan=2)

z=Button(frameb,text='Z', relief=RAISED,width=15 ,height=1 ,activeforeground='blue', bd=4,command=zf)
z.grid(row=4,column=4,columnspan=2)
x=Button(frameb,text='X', relief=RAISED,width=15 ,height=1 ,activeforeground='blue', bd=4 ,command=xf)
x.grid(row=4,column=5,columnspan=2)
c=Button(frameb,text='C', relief=RAISED,width=15 ,height=1 ,activeforeground='blue', bd=4,command=cf)
c.grid(row=4,column=6,columnspan=2)
v=Button(frameb,text='V', relief=RAISED,width=15 ,height=1 ,activeforeground='blue', bd=4 ,command=vf)
v.grid(row=4,column=7,columnspan=2)
b=Button(frameb,text='B', relief=RAISED,width=15 ,height=1 ,activeforeground='blue', bd=4,command=bf)
b.grid(row=4,column=8,columnspan=2)
n=Button(frameb,text='N', relief=RAISED,width=15 ,height=1 ,activeforeground='blue', bd=4 ,command=nf)
n.grid(row=4,column=9,columnspan=2)
m=Button(frameb,text='m', relief=RAISED,width=15 ,height=1 ,activeforeground='blue', bd=4,command=mf)
m.grid(row=4,column=10,columnspan=2)
space=Button(frameb,text='Space', relief=RAISED,width=50 ,height=1 ,activeforeground='blue', bd=4,command=space)
space.grid(row=5,column=5,columnspan=4)

    
top.mainloop()
