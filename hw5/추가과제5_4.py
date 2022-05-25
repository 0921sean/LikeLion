list = []

while True:
    num = int(input("Enter a number: "))
    if (num <= 0):
        break
    else:
        list.append(num)

print("The largest number entered was " + format(max(list), ".2f"))