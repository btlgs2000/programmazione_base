import time

i = 1
try:
    while True:
        print(i)
        i +=1
        time.sleep(1)
except:
    print("Termino il programma")
    exit()