import os
#This will be the class of the second person to talk

class Person2:
    def __init__(self, name):
        self.name = name

    priv_key = 0
    pub_key = 0
    shared_key = 0

name2 = input("Please enter your name : ")
person2 = Person2(name2)

priv_key2 = input(f"Please enter the number to generate {person2.name} private key : ")
person2.priv_key = priv_key2

print(f"{person2.name} private key is : {person2.priv_key}") 

friend = input("Please enter the name of the person you want to talk to : ")

file = 'Test/' + name2 + '_' + friend + '.txt'
revfile = 'Test/' + friend + '_' + name2 + '.txt'

#Verify if a text file between the two already exists
if not (os.path.isfile(file)) and not (os.path.isfile(revfile)):
    file = open(file, "w")
    file.write("start of the conversation between " + name2 + " and " + friend)
    file.close()

#Make sure that whatever the order of the name, we will still write in the same file
#if the two people that communicate have the right names
if (os.path.isfile(file)):
    file = file
else:
    file = revfile

