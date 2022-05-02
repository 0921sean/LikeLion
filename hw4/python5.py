import random
import time

print("5개의 메뉴를 추가해주세요! 5개가 입력되면 오늘의 메뉴를 추천해드려요.")
print("동일한 메뉴는 안돼요!")

menu = []
count = 0

while (count != 5):
    item = input("메뉴 추가: ")
    if (len(menu) == 0):
        pass
    else:
        for x in range(len(menu)):
            if (item == menu[x]):
                print("이미 있는 메뉴예요! 다른 메뉴를 입력해주세요.")
                del(menu[x])
                count -= 1
                break
            else:
                pass
    menu.append(item)
    count += 1
    print("현재 메뉴 수 = " + str(count))

print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)

print(menu)
print("과연 오늘의 메뉴는?")

print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)

index = random.randrange(5)
print("오늘의 메뉴는 " + str(index+1) + " 번째 메뉴," + menu[index] + " 입니다.")