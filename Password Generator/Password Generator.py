import random
from tkinter import*
Generator=Tk()
Generator.geometry("250x200")
Welcome_lbl=Label(text='Welcome to the password generator!').place(x='20',y='10')
def PasswordGenerator():
     UsedPasswords = []
     Category = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ','!@#$%^&*()+=:<>','1234567890']
     i=0
     password=''
     while i<12:
         x=random.randint(0,2)
         RandomCategory=Category[x]
         RandomCategoryCount=len(RandomCategory)
         y=random.randint(1,RandomCategoryCount)
         password=password+RandomCategory[y-1]
         i=i+1
     UsedPasswords=['']    
     for i in range(len(UsedPasswords)):
         if UsedPasswords[i]==password:
             print('Password is already taken!')
             Password_lbl = Message(text = "Password is already taken!").place(x=130,y=60)
         else:
             UsedPasswords.append(password)
             Password_lbl = Message(text = password).place(x=30,y=60)
Generator_btn=Button(text='Generator',command=PasswordGenerator).place(x='20',y='150')
Generator.mainloop()