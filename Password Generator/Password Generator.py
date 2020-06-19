import random
#Importin tkinter function
from tkinter import*
#Creating tkinter window
Generator_Window=Tk()
Generator_Window.geometry("300x200")
Welcome_lbl=Label(text='Welcome to the password generator!',font = "Arial 12 bold").place(x='10',y='10')
#Password Generator function
def PasswordGenerator():
     #Used password list to store password generator
     UsedPasswords = []
     #List storing different categories of characyters
     Category = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ','!@#$%^&*()+=:<>','1234567890']
     #Declaring counter
     i=0
     #Declaring password variables
     password=''
     #While loop
     while i<12:
         #Choosing a random category
         x=random.randint(0,2)
         RandomCategory=Category[x]
         #Choosing a random chartacter from the randomly chosen category
         RandomCategoryCount=len(RandomCategory)
         y=random.randint(1,RandomCategoryCount)
         password=password+RandomCategory[y-1]
         #Increasing counter
         i=i+1
     #Checking if password has been used before 
     UsedPasswords=['']    
     for i in range(len(UsedPasswords)):
         #Displaying password on label
         if UsedPasswords[i]==password:
             print('Password is already taken!')
             Password_lbl = Message(text = "Password is already taken!", width=25).place(x=130,y=60)
         else:
             UsedPasswords.append(password)
             Password_lbl = Message(text = ("Password:  "+password), width=200).place(x=60,y=60)
#Declaring generator button
Generator_btn=Button(text='Generator', activebackground="blue", activeforeground="yellow", command=PasswordGenerator).place(x='20',y='150')
#Function exiting Generator window
def close_window (): 
     Generator_Window.destroy()
#Declaring Exit button
Exit_btn = Button(text = "Exit",activebackground = "red", activeforeground = "black", command=close_window).place(x = 260, y = 150)  
Generator_Window.mainloop()
