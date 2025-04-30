#read first line of file
file = open('', 'r')
print("Reading first line")
print(file.readline())
file.close()

#reade first three lines of file
file = open('', 'r')
print("Reading multiple lines...")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

#looping through all the lines of the file
file = open('', 'r')
print("Looping through the lines...")
for line in file:
    print(line)
    file.close()
