##MERGE SORT ALGORITHM
##divide and conquer algorithm
##divides the array in half repeatedly until each piece is one element long
##then they are merged back in order
##useful to sort linked lists without extra space for links
##for arrays it needs extra space for each half during each iteration

def mergeSort(sortList):
    
    if len(sortList) > 1:
        mid = len(sortList)//2
        lefthalf = sortList[:mid]
        righthalf = sortList[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i = j = k = 0       

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                sortList[k] = lefthalf[i]
                i = i+1
            else:
                sortList[k] = righthalf[j]
                j = j+1
            k = k+1

        while i < len(lefthalf):
            sortList[k] = lefthalf[i]
            i = i+1
            k = k+1

        while j < len(righthalf):
            sortList[k]=righthalf[j]
            j = j+1
            k = k+1

    return sortList

list1 = []
size = int(input("Enter array size: "))     ##casted to type int

for i in range(size):
    print("Enter element", i+1) 
    list1.append(int(input()))              ##can also be casted to strings     
    ##or
    ##list1.append(input("Enter element: "))

print(list1)
print("Sorted array: ", mergeSort(list1))  ##function call  
