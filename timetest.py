import time
for i in range(30):
    oldtime = time.time()
    while True:
        newtime = time.time()
        if newtime-oldtime > 1:
            print(round(newtime - oldtime))
            break


