##ALL ABOUT tuple
##tuple is an ORDERED, IMMUTABLE collection.
##It allows duplicate values.
##use a tuple when,
##data does not need modification


#create tuple 
tuple1 = ("A", "V", "F", "Y", "D", "H", "W", "A", "A")
print(tuple1)

#insert/ update values
#you cannot insert/ update values to a tuple, tuples are immutable

#delete values
##you cannot delete values from a tuple, tuples are immutable
##but you can delete the entire tuple
##del tuple1                #removes the tuple
##print(list1)              #causes a name error since the tuple no longer exists


#element count
x = tuple1.count("A")
print(x)

#prints the index of an element
y = tuple1.index("W")
print(y)

#loop through a tuple
for r in tuple1:
    print(r)

#check a value exist in the tuple
if "A" in tuple1:
    print("value exists")

#tuple length
print("length of tuple 1 is ", len(tuple1))

             
