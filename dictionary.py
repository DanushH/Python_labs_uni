##ALL ABOUT dictionary
##dictionary is an ORDERED(V 3.7+), INDEXED and (therefore) MUTABLE collection.
##It does not allow duplicate values.
##use a dictionary when,
##need a logical association between a key-value pair
##need fast lookup for data based on a custom key
##data is being constantly modified


#create dictionary d = {}
diction1 = {
    "A": 54,
    "V": 89,
    "F": 24,
    "Y": 43,
    "D": 18,
    "H": 46,
    "W": 16
}
print(diction1)

#insert values
diction1["B"] = 77          #add a new value with key B
print(diction1)

#update values
diction1["A"] = 22          #change value of key A
print(diction1)
diction1.update({"H": 99})  #change value of key H

#delete values
diction1.popitem()          #remoevs last inserted value (B)
print(diction1)
diction1.pop("F")           #removes key F
print(diction1)
del diction1["V"]           #removes key V
print(diction1)
##del diction1              #removes the dictionary
##print(diction1)           #causes a name error since the dictionary no longer exists
##diction1.clear()          #empties the dictionary
##print(diction1)           #no error, outputs empty dictionary

#copy the dictionary
diction2 = diction1.copy()
diction3 = dict(diction1)
print(diction2)
print(diction3)


#print the keys and values list
print(diction1.keys())
#or
for x in diction1.keys():
    print(x)                #key list
    
print(diction2.values())    
#or
for x in diction2.values():
    print(x)                #value list

print(diction3.items())     
#or
for x, y in diction3.items():
    print(x, y)             #both keys and values


#sorted function to sort keys alphabetically
diction4 = sorted(diction1)
print(diction4)
for x in diction4:
    print(x)


#dictionary length
print("length of dictionary 1 is ", len(diction1))

#check a value exist in the dictionary
if "A" in diction1:
    print("key exists")
if 43 in diction1.values():
    print("value exists")


#does not work
##if "A" in diction1.items():
##    print("key/ value exists")        

##list1 = []
##list1 = diction1.values()
##print(list1.sort())
##for x in list:
##    print(x)

