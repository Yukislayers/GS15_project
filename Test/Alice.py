import os

#This will be the class of the first person to talk

class Alice:
    name = 'Alice'
    priv_key = 0
    pub_key = 0
    shared_key = 0

print('You are : ' + Alice.name)

friend = input("Please enter the name of the person you want to talk to : ")

print('You are going to talk to : ' + friend)

file = 'Test/' + Alice.name + '_' + friend + '.txt'
revfile = 'Test/' + friend + '_' + Alice.name + '.txt'

#Verify if a text file between the two already exists
if not (os.path.isfile(file)) and not (os.path.isfile(revfile)):
    f = open(file, "w")
    print('File between ' + Alice.name + ' and ' + friend + ' is created !')
    f.write("start of the conversation between " + Alice.name + " and " + friend)
    f.close()
else:
    print('File between ' + Alice.name + ' and ' + friend + ' already exists !')

mydir = 'Test/' + Alice.name + '_dir'
friend_dir = 'Test/' + friend + '_dir'

#Create folder to share files 
if not (os.path.isdir(mydir)):
    os.mkdir(mydir)
    print(mydir + ' folder is created')
else:
    print(friend_dir + ' folder is already created')

if not (os.path.isdir(friend_dir)):
    os.mkdir(friend_dir)
    print(friend_dir + ' folder is created')
else:
    print(friend_dir + ' folder is already created')

#Make sure that whatever the order of the name, we will still write in the same file
#if the two people that communicate have the right names
if (os.path.isfile(file)):
    file = file
else:
    file = revfile

print('\n-------------------------------------------')
print('Start of the communication \n')

talking = True

print('If you want to stop, type : STOP')

#We need to create something to share the files
while talking == True:
    f = open(file, "a")
    new_input = input(Alice.name + ' : ')
    if new_input.lower() == 'stop':
        talking = False
        f.close()
        break
    f.write('\n' + Alice.name + ' : ' + new_input)
    f.close()


