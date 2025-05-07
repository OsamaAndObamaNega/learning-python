import time as tmodi


print("ok")
time = 60000    

for i in range(time, 0, -1):
    seconds = i % 60
    minits = int(i / 60) % 60
    hour = int(i / 3600)
    print(f"{hour:02}:{minits:02}:{seconds:02}")

    tmodi.sleep(1)
print("Up")