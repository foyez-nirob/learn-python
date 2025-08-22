#----------------------->>>>>>>>>Dictionary IN PYTHON<<<<<------------------............

info = {
    "name" : "Foyez",
    "age" : 22,
    "subject" : ["c++","python","java"]
}
print(info)
print(type(info))


print(info["name"])
print(info["age"])
print(info["subject"])

print(info.get("name"))
print(info.get("age"))
print(info.get("subject"))

info["surename"] = "Nirob"
print(info["surename"])

null_dict = {}
null_dict["name"] = "new dictionary"
print(null_dict)


# nested dictionary ==>

student = {
    "name" : "Foyez",
    "subject":{
        "stat" : "A-",
        "ds" : "A-",
        "dld": "A+"
    }
}

print(student)
print(student["subject"])
print(student["subject"]["dld"])


# Dictionary Method ==>

student = {
    "name" : "Foyez",
    "subject":{
        "stat" : "A-",
        "ds" : "A-",
        "dld": "A+"
    }
}

print(len(student.keys()))
print(student.keys())                   # returns all the keys of dictionary
print(list(student.keys()))

print(student.values())                     # returns all the values
print(list(student.values()))

print(student.items())                      # returns all the keys and values 
print(list(student.items()))                                            # as tuple (key,values)

new_dict={}
new_dict.update({"name":"Nirob"})
print(new_dict.get("name"))

student.update(new_dict)
print(student.get("name"))

#----------------------->>>>>>>>>Set IN PYTHON<<<<<------------------............

set1 = {1,2,3,4}
set2 = {1,2,"hello","world",4}

print(set2)
print(type(set1))
print(len(set1))


#Set methods ===>

set3 = set()                  #empty set

set3.add(1)
set3.add(2)
set3.add("foyez")
set3.add("nirob")

set3.remove("nirob")
set3.pop()                           # delete a random value
print(set3.pop())                    
set3.clear()                         #clear all the values

set1 ={1,2,3,4}
set2 = {4,5,6}
print(set1.union(set2))               #{1,2,3,4,5,6}
print(set1.intersection(set2))        #{4}