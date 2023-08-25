import os

#prints out all the current environment variables and their values in a dictionary
print(os.environ)

print("*_______________________________________________*")
#prints the value of the HOME environment variable. HOME usually points to the current user's home directory
print(os.environ['HOME'])
print("*_______________________________________________*")
#prints the value of the PATH environment variable. PATH is a list of directories that the operating system uses to look for executable files
print(os.environ['PATH'])