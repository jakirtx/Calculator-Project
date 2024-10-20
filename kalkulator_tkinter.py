from tkinter import *

def click(number):
    global expression
    expression = expression + number
    hasil.config(text=expression)

def Clear():
    global expression
    expression=''
    hasil.config(text=expression)

def calculate():
    global expression
    if expression != '':
        res = eval(expression)
        hasil.config(text= res)

root = Tk()

root.title('Kalkulator')
root.geometry('800x400')
root.resizable(False, False)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)
root.rowconfigure(5, weight=1)

expression = ''

#baris1
hasil = Label(root, text='')
hasil.grid(column=0, row=0, columnspan=4, sticky=E)
#baris2
clear = Button(root, text='C', command=Clear).grid(column=0, row=1, sticky=NSEW)
bagi = Button(root, text='/', command= lambda: click('/')).grid(column=1, row=1, sticky=NSEW)
persen = Button(root, text='%', command= lambda: click('%')).grid(column=2, row=1, sticky=NSEW)
kali = Button(root, text='*', command= lambda: click('*')).grid(column=3, row=1, sticky=NSEW)
#baris3
no7 = Button(root, text='7', command= lambda: click('7')).grid(column=0, row=2, sticky=NSEW)
no8 = Button(root, text='8', command= lambda: click('8')).grid(column=1, row=2, sticky=NSEW)
no9 = Button(root, text='9', command= lambda: click('9')).grid(column=2, row=2, sticky=NSEW)
kurang = Button(root, text='-', command= lambda: click('-')).grid(column=3, row=2, sticky=NSEW)
#baris4
no4 = Button(root, text='4', command= lambda: click('4')).grid(column=0, row=3, sticky=NSEW)
no5 = Button(root, text='5', command= lambda: click('5')).grid(column=1, row=3, sticky=NSEW)
no6 = Button(root, text='6', command= lambda: click('6')).grid(column=2, row=3, sticky=NSEW)
tambah = Button(root, text='+', command= lambda: click('+')).grid(column=3, row=3, sticky=NSEW)
#baris5
no1 = Button(root, text='1', command= lambda: click('1')).grid(column=0, row=4, sticky=NSEW)
no2 = Button(root, text='2', command= lambda: click('2')).grid(column=1, row=4, sticky=NSEW)
no3 = Button(root, text='3', command= lambda: click('3')).grid(column=2, row=4, sticky=NSEW)
samadengan = Button(root, text='=', command=calculate).grid(column=3, row=4, sticky=NSEW, rowspan=2)
#baris6
no0 = Button(root, text='0', command= lambda: click('0')).grid(column=0, row=5, sticky=NSEW, columnspan=2)
koma = Button(root, text=',', command= lambda: click('.')).grid(column=2, row=5, sticky=NSEW)
root.mainloop()