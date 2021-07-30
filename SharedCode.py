'''
Random Password Generator using Python
Author: Ayushi Rawat
'''

#import the necessary modules!
import random
import string

print('hello, Welcome to Password generator!')

try:
    newfile = open("passwordfile.txt","x")
except:
    newfile = open("passwordfile.txt", "w")



    
def makepassword(length):
    length = int(length)
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation
    all = lower + upper + num + symbols
    temp = random.sample(all,length)
    password = "".join(temp)
    return password
    
def addpassword(website, username, length):
     
    password = makepassword(length)
    newfile = open("passwordfile.txt", "a")
    newfile.write("\n")
    newfile.write("Website: " + website)
    newfile.write("\t")
    newfile.write("Username: " + username)
    newfile.write("\t") 
    newfile.write("Password: " + password)
    


import tkinter as tk

root = tk.Tk()
root.title("Password Generator")
canvas = tk.Canvas(root, height=500, width=500)
canvas.pack()

frame = tk.Frame(root, bg="#9196c0", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

frame1 = tk.Frame(root, bg="#9196c0", bd=5)
frame1.place(relx=0.5, rely=0.2, relwidth=0.75, relheight= 0.1, anchor='n')

frame2 = tk.Frame(root, bg="#9196c0", bd=5)
frame2.place(relx=0.5, rely=0.3, relwidth=0.75, relheight= 0.1, anchor='n')

frame3 = tk.Frame(root, bg="#9196c0", bd=5)
frame3.place(relx=0.5, rely=0.4, relwidth=0.75, relheight= 0.1, anchor='n')

website_label = tk.Label(text = "Website", bg="#9196c0", font=40).place(x = 300, y = 65)
username_label = tk.Label(text = "Username", bg="#9196c0",font=40).place(x = 300, y = 115)
length_label = tk.Label(text = "Length", bg="#9196c0",font=40).place(x = 300, y = 165)




entry = tk.Entry(frame, font=40)

entry.place(relwidth=0.5, relheight=1)

entry1 = tk.Entry(frame1, font=40)

entry1.place(relwidth=0.5, relheight=1)

entry2 = tk.Entry(frame2, font=40)

entry2.place(relwidth=0.5, relheight=1)

button = tk.Button(frame3, text="AddPassword", font=40, command=lambda: addpassword(entry.get(),entry1.get(),entry2.get()))
button.place(relx=0, relheight=1, relwidth=0.3)

root.mainloop()