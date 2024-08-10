import os
import time
import random

def clear_screen():
    if (os.name == 'posix'):s
        os.system('clear')
    else:
        os.system('cls')

SCORE_FINAL = 0

print("Retenez la sequence")
time.sleep(1)
a = random.randint(999, 10000)
print(a)
time.sleep(3)
b = ""
compact = str(a) + str(b)
while True:
    clear_screen()
    reponse_str = input("Votre reponse : ")
    if reponse_str == compact:
        SCORE_FINAL += 1
        print("La sequence est correcte")
    else:
        print(f"La sequence etait {compact} ")
        print(f"Votre Score Final est : {SCORE_FINAL}")
        time.sleep(2)
        break
    b = random.randint(0, 9)
    compact += str(b)
    print("Retenez la sequence")
    time.sleep(1)
    print(compact)
    time.sleep(3)



