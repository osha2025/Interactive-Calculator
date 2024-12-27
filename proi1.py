
import threading
from tkinter import Tk, Entry, Button, StringVar
import pygame

class Calculator:
    def __init__(self, master):
        pygame.mixer.init() 
        self.sound = pygame.mixer.Sound("bubble_sound.mp3.mp3")  
        self.result_sound = pygame.mixer.Sound("result_sound.wav")

        master.title("Numinexus")
        master.geometry('357x420+0+0')
        master.config(bg='gray')
        master.resizable(False, False)

        self.equation = StringVar()
        self.entry_value = ''
        Entry(width=17, bg='#fff', font=('Arial Bold', 28), textvariable=self.equation).place(x=0, y=0)

        Button(width=11, height=4, text='(', relief='flat', bg='orange', command=lambda: self.button_click('(')).place(x=0, y=50)
        Button(width=11, height=4, text=')', relief='flat', bg='orange', command=lambda: self.button_click(')')).place(x=90, y=50)
        Button(width=11, height=4, text='%', relief='flat', bg='orange', command=lambda: self.button_click('%')).place(x=180, y=50)
        Button(width=11, height=4, text='1', relief='flat', bg='orange', command=lambda: self.button_click(1)).place(x=0, y=125)
        Button(width=11, height=4, text='2', relief='flat', bg='orange', command=lambda: self.button_click(2)).place(x=90, y=125)
        Button(width=11, height=4, text='3', relief='flat', bg='orange', command=lambda: self.button_click(3)).place(x=180, y=125)
        Button(width=11, height=4, text='4', relief='flat', bg='orange', command=lambda: self.button_click(4)).place(x=0, y=200)
        Button(width=11, height=4, text='5', relief='flat', bg='orange', command=lambda: self.button_click(5)).place(x=90, y=200)
        Button(width=11, height=4, text='6', relief='flat', bg='orange', command=lambda: self.button_click(6)).place(x=180, y=200)
        Button(width=11, height=4, text='7', relief='flat', bg='orange', command=lambda: self.button_click(7)).place(x=0, y=275)
        Button(width=11, height=4, text='8', relief='flat', bg='orange', command=lambda: self.button_click(8)).place(x=180, y=275)
        Button(width=11, height=4, text='9', relief='flat', bg='orange', command=lambda: self.button_click(9)).place(x=90, y=275)
        Button(width=11, height=4, text='0', relief='flat', bg='orange', command=lambda: self.button_click(0)).place(x=90, y=350)
        Button(width=11, height=4, text='.', relief='flat', bg='orange', command=lambda: self.button_click('.')).place(x=180, y=350)
        Button(width=11, height=4, text='+', relief='flat', bg='orange', command=lambda: self.button_click('+')).place(x=270, y=275)
        Button(width=11, height=4, text='-', relief='flat', bg='orange', command=lambda: self.button_click('-')).place(x=270, y=200)
        Button(width=11, height=4, text='/', relief='flat', bg='orange', command=lambda: self.button_click('/')).place(x=270, y=50)
        Button(width=11, height=4, text='x', relief='flat', bg='orange', command=lambda: self.button_click('*')).place(x=270, y=125)
        Button(width=11, height=4, text='=', relief='flat', bg='lightblue', command=self.solve).place(x=270, y=350)
        Button(width=11, height=4, text='C', relief='flat', command=self.clear).place(x=0, y=350)

    def button_click(self, value):
        self.sound.play()
        self.show(value)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        try:
            result = eval(self.entry_value)
            self.equation.set(result)
            self.entry_value = str(result)

            threading.Timer(0.50, self.play_result_sound).start()
            
        except Exception as e:
            self.equation.set("math erorrrr brooo")
            self.entry_value = ''

    def play_result_sound(self):
        self.result_sound.play()

root = Tk()
Numinexus = Calculator(root)
root.mainloop()
