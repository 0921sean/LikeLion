list = []

while True:
    data = input("Enter anything: ")
    if (data == 'q'):
        break
    else:
        list.append(data)
print(list)