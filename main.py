

from tkinter import *
from tkinter import messagebox #* import messagebox library

def click():
    # messagebox.showinfo(title='This is an info message box', message='You are a person')
    # # while(True):
    # messagebox.showwarning(title='Warning', message='You have a virus')

    # messagebox.showerror(title='Error', message='error')


    # if messagebox.askokcancel(title="ask ok cancel", message="do you want to do the thing"):
    #     print('you did a thing')
    # else:
    #     print('you canceled a thing')
    
    
    # if messagebox.askretrycancel(title="ask ok cancel", message="do you want to do the thing"):
    #     print('you retried a thing')
    # else:
    #     print('you canceled a thing')

        
    # if messagebox.askyesno(title="ask yes or no", message="do you like papar?"):
    #     print('you like paper')
    # else:
    #     print('you dont like paper')


    answer = messagebox.askquestion(title='ask question', message='Do you like pie?', icon='error')
    if(answer == 'yes'):
        print('I like pie to')
    else:
        print('you dont like pie')
    
    print(messagebox.askyesnocancel(title='Yes no cancel', message='Do you like to code?'))





window = Tk()

button = Button(window, command=click, text="click")
button.pack()

window.mainloop()