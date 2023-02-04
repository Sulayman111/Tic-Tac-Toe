import tkinter
from tkinter import PhotoImage
from tkinter import ttk
from tkinter import messagebox
window = tkinter.Tk()
window.title('Tic-Tac-Toe')
window.geometry('565x455')
window.resizable(False, False)

but1 = ttk.Button(window, text=' ')
but1.config(command=lambda: buttonClick(1))
but1.grid(row=0, column=0, sticky='snew', ipadx=40, ipady=40)
but2 = ttk.Button(window, text=' ')
but2.config(command=lambda: buttonClick(2))
but2.grid(row=0, column=1, sticky='snew', ipadx=40, ipady=40)
but3 = ttk.Button(window, text=' ')
but3.config(command=lambda: buttonClick(3))
but3.grid(row=0, column=2, sticky='snew', ipadx=40, ipady=40)
but4 = ttk.Button(window, text=' ')
but4.config(command=lambda: buttonClick(4))
but4.grid(row=1, column=0, sticky='snew', ipadx=40, ipady=40)
but5 = ttk.Button(window, text=' ')
but5.config(command=lambda: buttonClick(5))
but5.grid(row=1, column=1, sticky='snew', ipadx=40, ipady=40)
but6 = ttk.Button(window, text=' ')
but6.config(command=lambda: buttonClick(6))
but6.grid(row=1, column=2, sticky='snew', ipadx=40, ipady=40)
but7 = ttk.Button(window, text=' ')
but7.config(command=lambda: buttonClick(7))
but7.grid(row=2, column=0, sticky='snew', ipadx=40, ipady=40)
but8 = ttk.Button(window, text=' ')
but8.config(command=lambda: buttonClick(8))
but8.grid(row=2, column=1, sticky='snew', ipadx=40, ipady=40)
but9 = ttk.Button(window, text=' ')
but9.config(command=lambda: buttonClick(9))
but9.grid(row=2, column=2, sticky='snew', ipadx=40, ipady=40)
playerturn1 = ttk.Label(text = 'playing №1')
playerturn1.place(x=500, y=300)
playerturn1.grid(row=3 , column=0, sticky='snew', ipadx=65, ipady=40)

playerDetails = ttk.Label(text = '\tPlayer №1 = X\n\n\tPlayer №2 = O')
playerDetails.grid(row=3, column=2, sticky='snew', ipadx=25, ipady=40)

restartButton = ttk.Button(window, text='Restart')
restartButton.grid(row=3, column=1, sticky='snew', ipadx=40, ipady=40)
restartButton.config(command=lambda: restartEvent())

#Queue -> Ochered
a = 1
b = 0
c = 0

def restartEvent():
    global a, b, c
    a = 1
    b = 0
    c = 0
    playerturn1['text'] = 'playing №1'
    but1['text'] = ' '
    but2['text'] = ' '
    but3['text'] = ' '
    but4['text'] = ' '
    but5['text'] = ' '
    but6['text'] = ' '
    but7['text'] = ' '
    but8['text'] = ' '
    but9['text'] = ' '

def disableButton():
    but1.state(['!disabled'])
    but2.state(['!disabled'])
    but3.state(['!disabled'])
    but4.state(['!disabled'])
    but5.state(['!disabled'])
    but6.state(['!disabled'])
    but7.state(['!disabled'])
    but8.state(['!disabled'])
    but9.state(['!disabled'])
    
def buttonClick(id):
    global a, b, c
    print(f'ID {id}')
    #Dlya igroka pod Nomeram 1
    if id == 1 and but1['text'] == ' ' and a == 1:
        but1['text'] = 'X'
        a = 0
        b += 1
    if id == 2 and but2['text'] == ' ' and a == 1:
        but2['text'] = 'X'
        a = 0
        b += 1
    if id == 3 and but3['text'] == ' ' and a == 1:
        but3['text'] = 'X'
        a = 0
        b += 1
    if id == 4 and but4['text'] == ' ' and a == 1:
        but4['text'] = 'X'
        a = 0
        b += 1
    if id == 5 and but5['text'] == ' ' and a == 1:
        but5['text'] = 'X'
        a = 0
        b += 1
    if id == 6 and but6['text'] == ' ' and a == 1:
        but6['text'] = 'X'
        a = 0
        b += 1
    if id == 7 and but7['text'] == ' ' and a == 1:
        but7['text'] = 'X'
        a = 0
        b += 1
    if id == 8 and but8['text'] == ' ' and a == 1:
        but8['text'] = 'X'
        a = 0
        b += 1
    if id == 9 and but9['text'] == ' ' and a == 1:
        but9['text'] = 'X'
        a = 0
        b += 1

    # Igrok-2

    if id == 1 and but1['text'] == ' ' and a == 0:
        but1['text'] = 'O'
        a = 1
        b += 1
    if id == 2 and but2['text'] == ' ' and a == 0:
        but2['text'] = 'O'
        a = 1
        b += 1
    if id == 3 and but3['text'] == ' ' and a == 0:
        but3['text'] = 'O'
        a = 1
        b += 1
    if id == 4 and but4['text'] == ' ' and a == 0:
        but4['text'] = 'O'
        a = 1
        b += 1
    if id == 5 and but5['text'] == ' ' and a == 0:
        but5['text'] = 'O'
        a = 1
        b += 1
    if id == 6 and but6['text'] == ' ' and a == 0:
        but6['text'] = 'O'
        a = 1
        b += 1
    if id == 7 and but7['text'] == ' ' and a == 0:
        but7['text'] = 'O'
        a = 1
        b += 1
    if id == 8 and but8['text'] == ' ' and a == 0:
        but8['text'] = 'O'
        a = 1
        b += 1
    if id == 9 and but9['text'] == ' ' and a == 0:
        but9['text'] = 'O'
        a = 1
        b += 1
    
    # Naxodim pobeditelya
    if (but1['text'] == 'X' and but2['text'] == 'X' and but3['text'] == 'X' or
        but4['text'] == 'X' and but5['text'] == 'X' and but6['text'] == 'X' or
        but7['text'] == 'X' and but8['text'] == 'X' and but9['text'] == 'X' or
        but1['text'] == 'X' and but4['text'] == 'X' and but7['text'] == 'X' or
        but2['text'] == 'X' and but5['text'] == 'X' and but8['text'] == 'X' or
        but3['text'] == 'X' and but6['text'] == 'X' and but9['text'] == 'X' or
        but1['text'] == 'X' and but5['text'] == 'X' and but9['text'] == 'X' or
        but3['text'] == 'X' and but5['text'] == 'X' and but7['text'] == 'X'):
        disableButton()
        c=1
        messagebox.showinfo('Tic-Tac-Toe', 'Player №1 Victory!')

    elif (but1['text'] == 'O' and but2['text'] == 'O' and but3['text'] == 'O' or
        but4['text'] == 'O' and but5['text'] == 'O' and but6['text'] == 'O' or
        but7['text'] == 'O' and but8['text'] == 'O' and but9['text'] == 'O' or
        but1['text'] == 'O' and but4['text'] == 'O' and but7['text'] == 'O' or
        but2['text'] == 'O' and but5['text'] == 'O' and but8['text'] == 'O' or
        but3['text'] == 'O' and but6['text'] == 'O' and but9['text'] == 'O' or
        but1['text'] == 'O' and but5['text'] == 'O' and but9['text'] == 'O' or
        but3['text'] == 'O' and but5['text'] == 'O' and but7['text'] == 'O'):
        disableButton()
        c=1
        messagebox.showinfo('Tic-Tac-Toe', 'Player №2 Victory!')

    elif b == 9:
        disableButton()
        c = 1
        messagebox.showinfo('Tic-Tac-Toe', 'Tie!')
    
    if a == 1 and c == 0:
        playerturn1['text'] ='playing №1'
    elif a == 0 and c == 0:
        playerturn1['text'] ='playing №2'
if __name__=='__main__':
    window.mainloop()
















