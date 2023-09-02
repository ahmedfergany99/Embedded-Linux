#-------------------------------------------------------------------
#Write a Python program to count the number of lines in a text file.
#-------------------------------------------------------------------

reading = open("example.txt","r")
lines = reading.readlines()
print(len(lines))