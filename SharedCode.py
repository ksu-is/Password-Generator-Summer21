'''
Random Password Generator using Python
Author: Ayushi Rawat
'''

#import the necessary modules!
import random
import string

print('hello, Welcome to Password generator!')

#input the length of password
length = int(input('\nEnter the length of password: '))                      

#define data
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
#string.ascii_letters

#combine the data
all = lower + upper + num + symbols

#use random 
temp = random.sample(all,length)

#create the password 
password = "".join(temp)

#print the password
print(password)

def makepassword(length):
  lower = string.ascii_lowercase
  upper = string.ascii_uppercase
  num = string.digits
  symbols = string.punctuation
  all = lower + upper + num + symbols
  temp = random.sample(all,length)
  password = "".join(temp)
  return password

try:
    newfile = open("passwordfile.txt","x")
except:
    newfile = open("passwordfile.txt", "w")


def addpassword():
    websitename = input("Please enter the website that this password is for: ")
    username = input("Please enter the username this password will be associated with: ")
    length = int(input("How long should this password be? "))
    password = makepassword(length)
    newfile = open("passwordfile.txt", "w")
    newfile.write("Website: " + websitename)
    newfile.write("\t")
    newfile.write("Username: " + username)
    newfile.write("\t") 
    newfile.write("Password: " + password)
    newfile.close()


addpassword()

