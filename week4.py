n = int(input("자연수를 입력해주세요: "))

# HW 1
for i in range(n):
    x = "*" * (i+1)
    print(x)
print("------------")
# HW 2
for i in range(n):
    x = " " * (n-(i+1)) + "*" * (i+1)
    print(x)
print("------------")
# HW 3
for i in range(n):
    x = " " * (n-(i+1)) + "*" * (2*i+1)
    print(x)
print("------------")
# HW 4
for i in range(n):
    x = " " * i + "*" * (2*(n-i)-1)
    print(x)