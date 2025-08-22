#--------------->>>>>>>>>FILE INPUT AND OUTPUT IN PYTHON<<<<<------------------............

# f = open("file name","mood")  * r = read,w = write

# if any file not in the same folder as python file then we have to give the file path

# => 'r' = for read only
# => 'w' = for write only,overwrite the file
# => 'x' = create a new file and for writing
# => 'a' = open for writing and appending end of the previous content
# => 'b' = binary mood
# => '+' = open a disk file for updating(reading and writing)

f = open("/Users/foyezahmmednirob/Desktop/git/learn-python/README.md","r")
data = f.read()
print(data)
print(type(data))
f.close()

F = open("file.txt","r")
# print(F.read())
print(F.read(10))                    # for first 10 character
F.close()

# data = f.readline()  ** read a line at a time

f = open("file.txt","r")
print(f.readline())
print(f.readline())
f.close()


## writing in file ==>>

f = open("/Users/foyezahmmednirob/Desktop/git/learn-python/README.md","w")
f.write("we are learning python for fun")
f.close()

f = open("file.txt","a")
f.write("\n5. This line is written by python code")
f.close()

f =open("/Users/foyezahmmednirob/Desktop/git/learn-python/README.md","r+")
data = f.read()
f.write(" and fun")
f.close()

### with syntax 

with open("file.txt","r") as f :
    data = f.read()
    print(data)

f = open("sample.txt","w")              # create a file if it's doesn't exist
f.write("hell")
f.close()

import os                               # this is procedure for delete a file
os.remove("sample.txt")