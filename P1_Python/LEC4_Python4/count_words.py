#-------------------------------------------------------------------
#Write a Python program to count the number of words in a text file.
#-------------------------------------------------------------------

reading = open("example.txt","r")
words = reading.read()
print(len(words.split())) 