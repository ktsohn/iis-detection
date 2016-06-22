##Practice using .txt files

import os
os.chdir("/Volumes/KINGSTON/")

def get_times(filename, size):
    list_of_times = []
    f=open(filename)
    first = f.readline()
    for i in range(size):
        line = f.readline()
        components = line.split(":")
        time = float((int(components[0]) * 86400) + (int(components[1]) * 3600) + \
        (int(components[2]) * 60) + float(components[3]))
        list_of_times.append(time)
    print(list_of_times)
    return list_of_times

def append_times(filename, time):
    day = int(time//86400)
    time -= (day * 86400)
    hour = int(time//3600)
    time -= (hour * 3600)
    min = int(time//60)
    time -= (min * 60)
    sec = float(time)
    with open(filename, "a") as f:
        f.write(str(day) + ":" + str(hour) + ":" + str(min) + ":" + str(sec) + "\n")
    print(str(day) + ":" + str(hour) + ":" + str(min) + ":" + str(sec) + "\n")


get_times("test_times.txt", 3)
append_times("test_times.txt", 90061.1)