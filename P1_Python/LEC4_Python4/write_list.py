#----------------------------------------------------
# Write a Python program to write a “list” to a file.
#----------------------------------------------------

names = ["ahmed","tawfik"]
with open('example.txt',"w") as myfile:
    myfile.write(" ".join(names))
    
show = open('example.txt')
print(show.read())