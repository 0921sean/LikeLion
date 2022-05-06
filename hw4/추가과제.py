# HW 1
num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
print("몫:  " + str(num1 // num2))
print("나머지:  " + str(num1 % num2))

# HW 2
x = int(input("Enter a value for x: "))
y = 3 * x**5 + 2 * x**4 - 5 * x**3 - x**2 + 7 * x - 6
print("Polynomial for x= " + str(x) + " :  " + str(y))

# HW 3
n = int(input("Enter the number of people : "))
prob = 100
for i in range(n):
    prob *= (1-i/365)
print("Probability: " + str(100-prob))