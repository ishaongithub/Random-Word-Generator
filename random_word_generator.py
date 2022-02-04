# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 18:13:21 2022

@author: ramak
"""

import random
from tkinter import *
root=Tk()
root.title("Random Word Generator")
root.geometry("400x400")
root.configure(bg="purple")

label= Label(root, bg="gold")


def random_word():
    
    alpha_list= ["a","b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    print(alpha_list)
    random1=random.randint(0,25)
    random_alpha1 =alpha_list[random1]
    
    random2=random.randint(0,25)
    random_alpha2 =alpha_list[random2]
    
    random3=random.randint(0,25)
    random_alpha3 =alpha_list[random3]
    
    random4=random.randint(0,25)
    random_alpha4 =alpha_list[random4]
    
    random5=random.randint(0,25)
    random_alpha5 =alpha_list[random5]
    
    label["text"]=random_alpha1 + random_alpha2 + random_alpha3 + random_alpha4 + random_alpha5
    
    


    
btn1= Button(root, text="You Random Word Is...  ", command=random_word, bg="gold")
btn1.place(relx=0.5, rely=0.5, anchor=CENTER)
label.place(relx=0.5, rely=0.6, anchor=CENTER)




root.mainloop()