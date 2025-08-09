myFile = open('myFile.txt', 'w')

print('Name of file: ', myFile.name)
# properties include .closed and .mode

myFile.write('I love python')
myFile.write(' and Javascript')
myFile.close()

myFile = open('myFile.txt', 'a')
myFile.write(' I also like php')
myFile.close()

# Read from a file

myFile = open('myFile.txt', 'r+')
text = myFile.read(100)
print(text)