import time
import random
f = open("rockyou.txt", "r", encoding="utf-8")
lines = f.read().splitlines()
f.close()
password = input("Password... ")
for line in lines:
    print(line)
    if line == password:
        print(f"Your password is {line}")
        break