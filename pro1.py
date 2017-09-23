

# hangman game--------guessing game-----

import Tkinter
from Tkinter import *
import tkMessageBox
import Tkinter
import random

# three diffrent frames
top=Tk()

frame=Frame(top,bg='lightgreen')
frame.grid(row=0,column=0)

bframe=Frame(top)
bframe.grid(row=1,column=0)

frameb=Frame(top)
frameb.grid(row=3,column=0,pady=5)

Var1=IntVar()
Var1.set(3)
mvar=StringVar()
maxno=0
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
def clear():
     a=mvar.get()
     mvar.set('')

def instructions():
    tkMessageBox.showinfo("Instructions","1.Guess the word shown in the box.\n 2.you have only 3 choices to guess the word.\n 3. By guessing one word you can score 10.\n")

def types():
    tkMessageBox.showinfo("Types","1.Animals.\n 2.Fruits \n 3.Cars Tag \n 4.Equipments\n")

def maxno():
    tkMessageBox.showinfo("Maximum score","Maximum score:150")
                          
def settings():
    tkMessageBox.showinfo("Settings","1.maximum guess: 3 \n 2.sound : pop sound")
    
def rewards():
    tkMessageBox.showinfo("Rewards","Rewards \n 1.you wil get 100 bonus if you guess 10 words continously.\n 2.you wil get 200 bonus if you guess 15 words continously. ")

# submit function to check the guess is correct or not

def submit():
     var=mvar.get()
     if var==picflag[1]:
          tkMessageBox.showinfo("Event Triggered","Congratulations")
          mvar.set('')
          msg()
     else:
          tkMessageBox.showinfo("Sorry","Worng Guess")
          mvar.set('')
          num=Var1.get()
          if num==3:
              hang2(B1)
              Var1.set(num-1)
          elif num==2:
              hang2(B2)
              Var1.set(num-1)
          elif num==1:
              hang2(B3)
              Var1.set(num-1)
          if num==1:
               tkMessageBox.askretrycancel("Game Over","Game Over \n Click on retry to play again")
               Var1.set(3)
               hang2(B4)
          
# replay function execute when replay button is pressed
def replay():
    tkMessageBox.askretrycancel("REPLAY","REPLAY \n Click on PLAY to play again")
    Var1.set(3)
    hang2(B4)
    
def play():
    Var1.set(3)
    msg()
    hang2(B4)
# this function choose the random image   
def mainset():
    global picflag
    pic=[[A0,"ORANGE"],[A1,"GRAPES"],[A2,"TIGER"],[A3,"APPLE"],[A4,"MIKE"],[A5,"RHINOSORUS"],[A6,"ZEBRA"],[A7,"WATERMELON"],[A8,"AUDI"],[A9,"EAGAL"],[C1,"SHAKTIMAN"],[C2,"SUPERMAN"],[C3,"IRONMAN"],[C4,"KRISH"],[C5,"ELEPHANT"],[C6,"BATMAN"]]
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

C1=PhotoImage(file="shaktiman.gif")
C2=PhotoImage(file="superman.gif")
C3=PhotoImage(file="iron.gif")
C4=PhotoImage(file="krish.gif")
C5=PhotoImage(file="elephant.gif")
C6=PhotoImage(file="batman.gif")

B1=PhotoImage(file="1.gif")
B2=PhotoImage(file="2.gif")
B3=PhotoImage(file="3.gif")
B4=PhotoImage(file="4.gif")

canvas = Canvas(frame,width = 1000, height = 145, bg = 'powderblue')
gif1 = PhotoImage(file = 'amri.gif')
canvas.create_image(0, 0, image = gif1, anchor = NW)
canvas.grid(row=0,column=0,padx=110,pady=20)

qu=Button(frame,text='QUIT', relief=RAISED,width=15 ,command=top.destroy,height=1 ,activeforeground='blue', bd=4,bg='lightgreen')
qu.grid(row=0,column=2,padx=0)

types=Button(bframe,text='Types', relief=RAISED,width=30 ,height=1 ,activeforeground='blue', bd=4,bg='lightgreen',command=types )
types.grid(row=1,column=0,pady=3,padx=2)

ins=Button(bframe,text='Instructions', relief=RAISED,width=30 ,height=1 ,activeforeground='blue',bd=4,bg='lightgreen',command=instructions )
ins.grid(row=1,column=1,pady=3)

se=Button(bframe,text='Settings', relief=RAISED,width=30 ,height=1 ,activeforeground='blue', bd=4 ,bg='lightgreen',command=settings)
se.grid(row=1,column=2,pady=3)

rew=Button(bframe,text='Rewards', relief=RAISED,width=25 ,height=1 ,activeforeground='blue', bd=4 ,bg='lightgreen',command=rewards)
rew.grid(row=1,column=3,pady=3)

maxs=Button(bframe,text='Maximun score', relief=RAISED,width=25 ,height=1 ,activeforeground='blue', bd=4 ,bg='lightgreen',command=maxno)
maxs.grid(row=1,column=4,pady=3)

def hang(Apic):
    But1=Button(bframe,image=Apic[0],height=180,width=180,bd=0)
    But1.grid(row=2,column=0,rowspan=2,pady=5)   

label0 = Tkinter.Label(bframe,text="Guess the word from Image",font='Helvetica -13 bold',bg='green')
label0.grid(row=2,column=1)

# entry to enter the word

E1=Entry(bframe,bd=7,width=35,textvariable=mvar)
E1.grid(row=2,column=2)


clear=Button(bframe,text='clear', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4 ,bg='powderblue',command=clear)
clear.grid(row=2,column=3,columnspan=2)

submit=Button(bframe,text='Submit', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4 ,bg='powderblue',command=submit)
submit.grid(row=2,column=4)

label0 = Tkinter.Label(bframe,text=E1.get(),font='Helvetica -13 bold')
label0.grid(row=2,column=3)

# vaiable is defined to show the remaining choice for word guessing 
Var1=IntVar()
Var1.set(3)

label1 = Tkinter.Label(bframe, text='Total number of choice : 3',font='Helvetica -13 bold',height=2)
label1.grid(row=3,column=1,columnspan=1)

label2 = Tkinter.Label(bframe, text='Remaining number of choice = ',font='Helvetica -13 bold')
label2.grid(row=3,column=2,columnspan=2)

en=Label(bframe,textvariable=Var1,width=4,bd=4,font="Times 15 bold italic")
en.grid(row=3,column=3,rowspan=1)

play=Button(bframe,text='PLAY', relief=RAISED,width=20 ,height=7 ,activeforeground='red', bd=4 ,bg='powderblue',command=play)
play.grid(row=2,column=5,pady=3)

rplay=Button(bframe,text='REPLAY', relief=RAISED,width=10 ,height=5 ,activeforeground='blue', bd=4 ,bg='powderblue',command=replay)
rplay.grid(row=2,column=6,pady=3,padx=6)

nextp=Button(bframe,text='NEXT IMAGE', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4,bg='powderblue',command=msg)
nextp.grid(row=4,column=0,pady=20)


a1=Button(frameb,text='1', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4,command=f1f,bg='powderblue')
a1.grid(row=1,column=3)
a2=Button(frameb,text='2', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4,command=f2f,bg='powderblue')
a2.grid(row=1,column=4)
a3=Button(frameb,text='3', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4,command=f3f ,bg='powderblue')
a3.grid(row=1,column=5)
a4=Button(frameb,text='4', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4 ,command=f4f,bg='powderblue')
a4.grid(row=1,column=6)
a5=Button(frameb,text='5', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4,command=f5f,bg='powderblue')
a5.grid(row=1,column=7)
a6=Button(frameb,text='6', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4 ,command=f6f,bg='powderblue')
a6.grid(row=1,column=8)
a7=Button(frameb,text='7', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4 ,command=f7f,bg='powderblue')
a7.grid(row=1,column=9)
a8=Button(frameb,text='8', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4 ,command=f8f,bg='powderblue')
a8.grid(row=1,column=10)
a9=Button(frameb,text='9', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4,command=f9f,bg='powderblue')
a9.grid(row=1,column=11)
a0=Button(frameb,text='0', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4 ,command=f0f,bg='powderblue')
a0.grid(row=1,column=12)


# this function executes and show the photos according to the choice you choose
#if wrong then photo will update in thus section

def hang2(Apic2):
    But2=Button(frameb,image=Apic2,height=180,width=180,bd=0)
    But2.grid(row=0,column=13,rowspan=10,padx=20,pady=10 ,columnspan=3)

q=Button(frameb,text='Q', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=3 ,command=qf,bg='powderblue')
q.grid(row=2,column=3)
w=Button(frameb,text='W', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=3,command=wf,bg='powderblue')
w.grid(row=2,column=4)
e=Button(frameb,text='E', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4,command=ef ,bg='powderblue')
e.grid(row=2,column=5)
r=Button(frameb,text='R', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4,command=rf ,bg='powderblue')
r.grid(row=2,column=6)
t=Button(frameb,text='T', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4,command=tf,bg='powderblue')
t.grid(row=2,column=7)
y=Button(frameb,text='Y', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4 ,command=yf,bg='powderblue')
y.grid(row=2,column=8)
u=Button(frameb,text='U', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4 ,command=uf,bg='powderblue')
u.grid(row=2,column=9)
i=Button(frameb,text='I', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4 ,command=iif,bg='powderblue')
i.grid(row=2,column=10)
o=Button(frameb,text='O', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4 ,command=of,bg='powderblue')
o.grid(row=2,column=11)
p=Button(frameb,text='P', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4,command=pf,bg='powderblue')
p.grid(row=2,column=12)

a=Button(frameb,text='A', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4 ,command=af,bg='powderblue')
a.grid(row=3,column=3,columnspan=2)
s=Button(frameb,text='S', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4 ,command=sf,bg='powderblue')
s.grid(row=3,column=4,columnspan=2)
d=Button(frameb,text='D', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4,command=df,bg='powderblue')
d.grid(row=3,column=5,columnspan=2)
f=Button(frameb,text='F', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4 ,command=ff,bg='powderblue')
f.grid(row=3,column=6,columnspan=2)
g=Button(frameb,text='G', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4 ,command=gf,bg='powderblue')
g.grid(row=3,column=7,columnspan=2)
h=Button(frameb,text='H', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4 ,command=hf,bg='powderblue')
h.grid(row=3,column=8,columnspan=2)
j=Button(frameb,text='J', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4,command=jf,bg='powderblue')
j.grid(row=3,column=9,columnspan=2)
k=Button(frameb,text='K', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4,command=kf,bg='powderblue')
k.grid(row=3,column=10,columnspan=2)
l=Button(frameb,text='L', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4,command=lf,bg='powderblue')
l.grid(row=3,column=11,columnspan=2)

z=Button(frameb,text='Z', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4,command=zf,bg='powderblue')
z.grid(row=4,column=4,columnspan=2)
x=Button(frameb,text='X', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4 ,command=xf,bg='powderblue')
x.grid(row=4,column=5,columnspan=2)
c=Button(frameb,text='C', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4,command=cf,bg='powderblue')
c.grid(row=4,column=6,columnspan=2)
v=Button(frameb,text='V', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4 ,command=vf,bg='powderblue')
v.grid(row=4,column=7,columnspan=2)
b=Button(frameb,text='B', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4,command=bf,bg='powderblue')
b.grid(row=4,column=8,columnspan=2)
n=Button(frameb,text='N', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4 ,command=nf,bg='powderblue')
n.grid(row=4,column=9,columnspan=2)
m=Button(frameb,text='m', relief=RAISED,width=10 ,height=1 ,activeforeground='blue', bd=4,command=mf,bg='powderblue')
m.grid(row=4,column=10,columnspan=2)

space=Button(frameb,text='Space', relief=RAISED,width=40 ,height=1 ,activeforeground='blue', bd=4,command=space,bg='powderblue')
space.grid(row=5,column=5,columnspan=4)

    
top.mainloop()
