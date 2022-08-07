from tkinter import *
import pyttsx3

my_app = Tk()
my_app.title("TechNess Text 2 Speech")
my_app.geometry("800x500")

def talk_action():
    #*This part is going to trigger the major action in the code base and can be called anywhere in the program
    voice_handler = pyttsx3.init()
    voice_handler.say(my_input.get())
    voice_handler.runAndWait()
    my_input.delete(0, END)

 
my_input = Entry(my_app, font=("Poppins", 20))
my_input.pack(pady=20)

my_button = Button(my_app, text="Talk", command=talk_action)
my_button.pack(pady=20)

my_app.mainloop()