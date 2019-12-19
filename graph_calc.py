#from tkinter import *
import Pmw
from tkinter import Button, Label
import string
from math import *
import numpy as np

Calculadora = Pmw.initialise(fontScheme = 'pmw1')
#Calculadora = Tk()
Calculadora.title("GRAPH_CALC")
Calculadora.config(bg='gray40')
Calculadora.geometry("321x668")
formula = ""
result = ""
mem = ""
ndact = False
type_op = "MATH"

def push(car):
    global formula
    formula=formula+car
    #print(formula)
    display.appendtext(car)

def typer(m):
    global type_op
    type_op = m
    print(type_op)
    clear()
    #display.appendtext(type_op+"\n")

def del_():
    global mem
    if mem!="":
        mem=""
    
def clear():
    global formula, mem, result
    formula = ""
    mem = ""
    result = ""
    display.clear()

def store():
    global mem
    if mem=="" and result!="" and result!="ERROR":
        mem = str(result)
        #display.appendtext("STORED: "+mem+"\n\n")
    else:
        push(mem)
    
def matr_demo():
    a1 = np.array([[1,2,3],[1,2,8]], float)
    a2 = np.array([[4,5,6],[2,3,4]], float)
    display.appendtext(a1+a2)

def change_sign():
    global result
    if result!="ERROR" and result!="":
        result = eval(str(result)+"*(-1)")
        text = '{:^29}'.format(str(result))
        display.appendtext((text)+"\n")

def nd():
    global ndact
    if ndact == False:
        ndact = True

def pi():
    if ndact == True:
        #numb = pi
        #display.appendtext(pi)
        push('3.141592653589793')
        
def operation():
    global formula, result
    print(formula)
    if type_op=="MATH" and formula!="":
        try:
            result = eval(formula)
        except:
            result = "ERROR"
        text = '{:^30}'.format(str(result))
        display.appendtext("\n"+text+"\n\n")
        formula=""

#PANTALLA
display = Pmw.ScrolledText(Calculadora, hscrollmode='none',#dynamic
                      vscrollmode='dynamic', hull_relief='sunken',#vscrollmode=dynamic
                      hull_background='gray40', hull_borderwidth=10, 
                      text_background='honeydew4', text_width=29, #ancho pantalla #29
                      text_foreground='black', text_height=9,#alto pantalla
          text_padx=10, text_pady=10, text_relief='groove',
                      text_font=('Arial', 12, 'bold') )
display.place(x=0,y=0)



Label(master=Calculadora,text='Quit',fg='steelblue3',bg='gray40').place(x=69,y=215)
Label(master=Calculadora,text='Ins',fg='steelblue3',bg='gray40').place(x=133,y=215)
Label(master=Calculadora,text='Lock',fg='steelblue3',bg='gray40').place(x=197,y=215)
Label(master=Calculadora,text='List',fg='steelblue3',bg='gray40').place(x=261,y=215)
Label(Calculadora,text='Test',fg='steelblue3',bg='gray40').place(x=5,y=270)
Label(Calculadora,text='Angle',fg='steelblue3',bg='gray40').place(x=69,y=270)
Label(Calculadora,text='Draw',fg='steelblue3',bg='gray40').place(x=133,y=270)
Label(Calculadora,text='YVars',fg='steelblue3',bg='gray40').place(x=197,y=270)
Label(Calculadora,text='Abs',fg='steelblue3',bg='gray40').place(x=5,y=325)
Label(Calculadora,text='Sin-1',fg='steelblue3',bg='gray40').place(x=69,y=325)
Label(Calculadora,text='Cos-1',fg='steelblue3',bg='gray40').place(x=133,y=325)
Label(Calculadora,text='Tan-1',fg='steelblue3',bg='gray40').place(x=197,y=325)
Label(Calculadora,text='π',fg='steelblue3',bg='gray40').place(x=261,y=325)
Label(Calculadora,text='Root',fg='steelblue3',bg='gray40').place(x=5,y=380)
Label(Calculadora,text='EE',fg='steelblue3',bg='gray40').place(x=69,y=380)
Label(Calculadora,text='{',fg='steelblue3',bg='gray40').place(x=133,y=380)
Label(Calculadora,text='}',fg='steelblue3',bg='gray40').place(x=197,y=380)
Label(Calculadora,text='10x',fg='steelblue3',bg='gray40').place(x=5,y=435)
Label(Calculadora,text='Un-1',fg='steelblue3',bg='gray40').place(x=69,y=435)
Label(Calculadora,text='Vn-1',fg='steelblue3',bg='gray40').place(x=133,y=435)
Label(Calculadora,text='n',fg='steelblue3',bg='gray40').place(x=197,y=435)
Label(Calculadora,text='[',fg='steelblue3',bg='gray40').place(x=261,y=435)
Label(Calculadora,text='ex',fg='steelblue3',bg='gray40').place(x=5,y=490)
Label(Calculadora,text='L4',fg='steelblue3',bg='gray40').place(x=69,y=490)
Label(Calculadora,text='L5',fg='steelblue3',bg='gray40').place(x=133,y=490)
Label(Calculadora,text='L6',fg='steelblue3',bg='gray40').place(x=197,y=490)
Label(Calculadora,text=']',fg='steelblue3',bg='gray40').place(x=261,y=490)
Label(Calculadora,text='RCL',fg='steelblue3',bg='gray40').place(x=5,y=545)
Label(Calculadora,text='L1',fg='steelblue3',bg='gray40').place(x=69,y=545)
Label(Calculadora,text='L2',fg='steelblue3',bg='gray40').place(x=133,y=545)
Label(Calculadora,text='L3',fg='steelblue3',bg='gray40').place(x=197,y=545)
Label(Calculadora,text='MEM',fg='steelblue3',bg='gray40').place(x=261,y=545)
Label(Calculadora,text=':',fg='steelblue3',bg='gray40').place(x=133,y=600)
Label(Calculadora,text='ANS',fg='steelblue3',bg='gray40').place(x=197,y=600)
Label(Calculadora,text='Entry',fg='steelblue3',bg='gray40').place(x=261,y=600)
Label(Calculadora,text='√',fg='steelblue3',bg='gray40').place(x=261,y=325)

Button(Calculadora,text='2nd',bg='steelblue3',fg='white',width=5).place(x=5,y=236) #activebackground="blue".place(x=8,y=243)
Button(Calculadora,text='Mode',bg='gray30',fg='white',width=5).place(x=69,y=236)
Button(Calculadora,text='Del',bg='gray30',fg='white',width=5).place(x=133,y=236)
Button(Calculadora,text='Alpha',bg='gray50',fg='white',width=5).place(x=197,y=236)
Button(Calculadora,text='Stat',bg='gray30',fg='white',width=5).place(x=261,y=236)

Button(Calculadora,text='Math',bg='gray30',fg='white',width=5).place(x=5,y=291)
Button(Calculadora,text='Mtrx',bg='gray30',fg='white',width=5).place(x=69,y=291)
Button(Calculadora,text='Prgm',bg='gray30',fg='white',width=5).place(x=133,y=291)
Button(Calculadora,text='Vars',bg='gray30',fg='white',width=5).place(x=197,y=291)
Button(Calculadora,text='Clr',bg='gray30',fg='white',width=5).place(x=261,y=291)

Button(Calculadora,text='x-1',bg='gray30',fg='white',width=5).place(x=5,y=346)
Button(Calculadora,text='Sin',bg='gray30',fg='white',width=5,command=lambda:push("sin(")).place(x=69,y=346)
Button(Calculadora,text='Cos',bg='gray30',fg='white',width=5,command=lambda:push("cos(")).place(x=133,y=346)
Button(Calculadora,text='Tan',bg='gray30',fg='white',width=5,command=lambda:push("tan(")).place(x=197,y=346)
Button(Calculadora,text='^',bg='gray30',fg='white',width=5).place(x=261,y=346)

Button(Calculadora,text='x2',bg='gray30',fg='white',width=5).place(x=5,y=401)
Button(Calculadora,text=',',bg='gray30',fg='white',width=5,command=lambda:push(",")).place(x=69,y=401)
Button(Calculadora,text='(',bg='gray30',fg='white',width=5,command=lambda:push("(")).place(x=133,y=401)
Button(Calculadora,text=')',bg='gray30',fg='white',width=5,command=lambda:push(")")).place(x=197,y=401)
Button(Calculadora,text='/',bg='steelblue3',fg='white',width=5,command=lambda:push("/")).place(x=261,y=401)

Button(Calculadora,text='Log',bg='gray30',fg='white',width=5).place(x=5,y=456)
Button(Calculadora,text='7',bg='gray50',fg='white',width=5,command=lambda:push("7")).place(x=69,y=456)
Button(Calculadora,text='8',bg='gray50',fg='white',width=5,command=lambda:push("8")).place(x=133,y=456)
Button(Calculadora,text='9',bg='gray50',fg='white',width=5,command=lambda:push("9")).place(x=197,y=456)
Button(Calculadora,text='x',bg='steelblue3',fg='white',width=5,command=lambda:push("*")).place(x=261,y=456)

Button(Calculadora,text='Ln',bg='gray30',fg='white',width=5).place(x=5,y=511)
Button(Calculadora,text='4',bg='gray50',fg='white',width=5,command=lambda:push("4")).place(x=69,y=511)
Button(Calculadora,text='5',bg='gray50',fg='white',width=5,command=lambda:push("5")).place(x=133,y=511)
Button(Calculadora,text='6',bg='gray50',fg='white',width=5,command=lambda:push("6")).place(x=197,y=511)
Button(Calculadora,text='-',bg='steelblue3',fg='white',width=5,command=lambda:push("-")).place(x=261,y=511)

Button(Calculadora,text='STO',bg='gray30',fg='white',width=5,command=store).place(x=5,y=566)
Button(Calculadora,text='1',bg='gray50',fg='white',width=5,command=lambda:push("1")).place(x=69,y=566)
Button(Calculadora,text='2',bg='gray50',fg='white',width=5,command=lambda:push("2")).place(x=133,y=566)
Button(Calculadora,text='3',bg='gray50',fg='white',width=5,command=lambda:push("3")).place(x=197,y=566)
Button(Calculadora,text='+',bg='steelblue3',fg='white',width=5,command=lambda:push("+")).place(x=261,y=566)

Button(Calculadora,text='Off',bg='gray30',fg='white',width=5,command=clear).place(x=5,y=621)
Button(Calculadora,text='0',bg='gray50',fg='white',width=5,command=lambda:push("1")).place(x=69,y=621)
Button(Calculadora,text='.',bg='gray50',fg='white',width=5,command=lambda:push(".")).place(x=133,y=621)
Button(Calculadora,text='(-)',bg='gray50',fg='white',width=5).place(x=197,y=621)
Button(Calculadora,text='Enter',bg='steelblue3',fg='white',width=5,command=operation).place(x=261,y=621)

Calculadora.mainloop()





