list = ["hey","hi","hello","bye","ta ta"]

print(list)

print(len(list))

print(list[0])
print(list[:5])
print(list[0:])
print(list[2:5])

if "hi" in list:
    print("hiiii guys")

if "bu" not in list:
    print("NOOOO HIIIII")


list[1] = "hii"
print(list)

list[1:3] =["hiiiii","helloo"]
print(list)

list[1:3] =["hiiiii","hellooooo","byeeee"]
print(list)

#adding method --->
thslist = ["apple","banana","oragne","lemon","dragon"]
thslist.append("dragon")
print(thslist)
thslist.insert(1,"komola")
print(thslist)
thslist.extend(list)
print(thslist)

# removing in list -->

ll=[1,2,3,4,5,6,7]

ll.remove(2)
ll.remove(4)

ll.pop(1)
ll.pop()

del ll[0]

ll.clear

del ll 

