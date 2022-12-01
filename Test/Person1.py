import os

#This will be the class of the first person to talk

class Person1:
    def __init__(self, name):
        self.name = name

    priv_key = 0
    pub_key = 0
    shared_key = 0


name1 = input("Please enter your name : ")
person1 = Person1(name1)
  
friend = input("Please enter the name of the person you want to talk to : ")

print('You are going to talk to : ' + friend)

file = 'Test/' + name1 + '_' + friend + '.txt'
revfile = 'Test/' + friend + '_' + name1 + '.txt'

#Verify if a text file between the two already exists
if not (os.path.isfile(file)) and not (os.path.isfile(revfile)):
    f = open(file, "w")
    f.write("start of the conversation between " + name1 + " and " + friend)
    f.close()

#Make sure that whatever the order of the name, we will still write in the same file
#if the two people that communicate have the right names
if (os.path.isfile(file)):
    file = file
else:
    file = revfile

talking = True

print('If you want to stop, type : STOP')

while talking == True:
    f = open(file, "a")
    new_input = input(person1.name + ' : ')
    if new_input.lower() == 'stop':
        talking = False
        f.close()
        break
    f.write('\n' + person1.name + ' : ' + new_input)
    f.close()


