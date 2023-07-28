##ALL ABOUT list
##list is an ORDERED, MUTABLE collection.
##It allows duplicate values.
##use a list when,
##data does not need random access
##need a simple, iterable collection
##data is being modified frequently


#create list l = []
list1 = ["A", "V", "F", "Y", "D", "H", "W", "A", "A"]
print(list1)

#insert values
list1.append("N")           #add an element to the end of the list
print(list1)
list1.insert(1, "R")        #add element to specific position
print(list1)

#update values
list1[0] = 22               #change existing values
print(list1)

#delete values
list1.pop(0)                #removes first position element (last element if not the INDEX is specified)
print(list1)
list1.remove("Y")           #removes element Y (VALUE)
print(list1)
del list1[2]                #removes second element
print(list1)
##del list1                 #removes the list
##print(list1)              #causes a name error since the list no longer exists
##list1.clear()             #empties the list
##print(list1)              #no error, outputs emplty list

#copy the list
list2 = list1.copy()
list3 = list(list1)
print(list2)
print(list3)


#element count
x = list1.count("A")
print(x)

#add two elements
list1.extend(list2)
print(list1)

#prints the index of an element
y = list1.index("W")
print(y)

#reverse a list
list1.reverse()
print(list1)

#sort a list alphabetically
list1.sort()

print(list1)

#loop through a list
for r in list1:
    print(r)

#check a value exist in the list
if "A" in list1:
    print("value exists")


#list length
print("length of list 1 is ", len(list1))



#swapping 2 positions
##def swapList(li, p1, p2):
##    li[p1], li[p2] = li[p2], li[p1]
##    return li
##
##list1 = [1,2,3,5,8,9]
##print(list1)
##position1, position2 = 2, 4
##print(swapList(list1, position1, position2))


#swapping 1st and last elements
##def swapList(li, p1, p2):
##    li[p1], li[p2-1] = li[p2-1], li[p1]
##    return li
##
##list1 = [1,2,3,5,8,9]
##print(list1)
##position1, position2 = 0, len(list1)
##print(swapList(list1, position1, position2))


#finding the 2nd largest number of a list from user input
##def secMax(li):
##    li.sort() #sort function sorts a list in ascending order
##    return li[-2]
##
##list1 = []
##
##num = int(input("Enter number of elements: "))
##
##for i in range(0, num):
##    elements = int(input("Enter element: "))
##    list1.append(elements)
##
##print(secMax(list1), " is the second largest number of the list")

                   


