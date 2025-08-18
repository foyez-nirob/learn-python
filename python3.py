#----------------------->>>>>>>>>LIST IN PYTHON<<<<<------------------............

list1 = ["hey","hi","hello","bye","ta ta"]
list2 = [1,3,4,5,6,7,8]
list3 = ["Foyez",20,"IIUC"]

print(list1)
print(len(list1))
print(list[1]," ",list[2])


# Slicing the list :===>

print(list1[0])
print(list1[:5])
print(list1[0:])
print(list1[2:5])

# Changing in the list ==>

list =[2,5,6,8,9]

list[0] = 1                                 #output: 1 5 6 8 9
list[1:3] =[0,0]                            #output: 1 0 0 8 9
list[1:3] =[10,11,12]                       #output: 1 10 11 12 8 9


# Some oparetion in List ===>

list =[3,4,5,6]

list.append(7)                             #output:3 4 5 6 7
list.sort()                                #output:sort
list.sort(reverse=True)                    #output:reverse sort
list.reverse()                             #output: reverse the whole list
list.insert(0,1)                           #output:1 4 5 6 


# removing in list -->

ll=[1,2,3,4,5,6,7]

ll.remove(2)
ll.remove(4)

ll.pop(1)
ll.pop()

del ll[0]

ll.clear

del ll 

