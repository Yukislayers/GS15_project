import Person

name1 = input("Please enter the name of the 1st person to communicate : ")
person1 = Person.Person(name1)

name2 = input("Please enter the name of the 2nd person to communicate : ")
person2 = Person.Person(name2)

setattr(person1, 'priv_key', 100)

setattr(person2, 'priv_key', 150)

print(f"{name1} private key is : {getattr(person1, 'priv_key')}")  

print(f"{name2} private key is : {getattr(person2, 'priv_key')}")  