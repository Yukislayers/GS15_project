import Person

#We will create the 2 people that will communicate
#Then we will have to create their own private and public key
#Send them to a server so they can retrieve it if they want to talk

name1 = input("Please enter the name of the 1st person to communicate : ")
person1 = Person.Person(name1)

priv_key1 = input(f"Please enter the number to generate {person1.name} private key : ")
person1.priv_key = priv_key1

print(f"{person1.name} private key is : {person1.priv_key}")  

name2 = input("Please enter the name of the 2nd person to communicate : ")
person2 = Person.Person(name2)

priv_key2 = input(f"Please enter the number to generate {person2.name} private key : ")
person2.priv_key = priv_key2

print(f"{person2.name} private key is : {person2.priv_key}") 