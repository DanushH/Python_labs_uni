##ALL ABOUT set
##set an UNORDERED, UNINDEXED, MUTABLE collection.
##It does not allows duplicate values.
##since set is unordered, data will appear in a random order
##use a set when,
##data need uniqueness for the elements


#create set l = []
set1 = {"A", "V", "F", "D", "W", "A"}
print(set1)

#insert values
set1.add("N")               #add an element to the set
print(set1)
set1.update("Q", "R", "J")  #add multiple elements to the set
print(set1)

#update values
#data cannot be changed

#delete values
set1.pop()                  #removes last element, can't predict the value since unordered
print(set1)
set1.remove("V")            #removes element V (VALUE)
print(set1)
set1.discard("J")           #removes element J (VALUE)
print(set1)
##del set1                  #removes the set
##print(set1)               #causes a name error since the set no longer exists
##set1.clear()              #empties the set
##print(set1)               #no error, outputs empty set

#copy the set
set2 = set1.copy()
print(set2)

#loop through a set
for r in set1:
    print(r)

#check a value exist in the set
if "A" in set1:
    print("value exists")

#set length
print("length of set 1 is ", len(set1))




##set methods
set3 = {"W", "D", "w", "t"}
set4 = {"a", "A", "N", "W"}
set5 = {1, 5, 66, "W"}
set6 = {5, 89, 66,}
set7 = {1, 5, 20}
set8 = {8, 20, 1, 65, 5}

#union
u = set3.union(set4, set5)                  #unite set3 with 4 & 5
print(u)

#intersection
i = set3.intersection(set4, set5)           #common elements for 1/ more sets
print(i)
#intersection_update
set3.intersection_update(set4, set5)        #removes uncommon elements from set3
print(set3)
##iu = set3.intersection_update(set4, set5) #results none //update method values can't be assigned
##print(iu)

#difference
d = set4.difference(set3)                   #results elements exist in only set4, not in set3
print(d)
##d = set3.difference(set4)                 #set3 is updated to {"W"}, hence results an empty set
##print(d)
#difference_update
set4.difference_update(set3)                #removes common elements from set4 //updates set4
print(set4)
#symmetric_difference
sd = set5.symmetric_difference(set6)        #results elements exist in both set5 & set6 except for common ones
print(sd)
#symmetric_difference_update
set5.symmetric_difference_update(set6)      #removes common elements from set5 //updates set5
print(set5)

#issubset
iss = set7.issubset(set8)                   #results true if set7 is a subset of set8
print(iss)
#issuperset
iss = set8.issuperset(set7)                 #results true if set8 is a superset of set7
print(iss)

#isdisjoint
isd = set3.isdisjoint(set8)                 #results true if set3 & set8 has no common elements
print(isd)







