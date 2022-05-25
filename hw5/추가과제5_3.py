string = ''

while True:
    name = input("Enter a name (q to quit): ")
    if (name == 'q'):
        break
    else:
        string += (" " + name)

print("Number of names and letter 'a': " + str(string.count(' ')) + " , " + str(string.count('a')))