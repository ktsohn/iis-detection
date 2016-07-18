##Practice with .txt
'''
Reading .txt, getting data, and modifying file
-use .txt as a collection of all the iis times
-formatting needed?
'''

import os
os.chdir("/Volumes/KINGSTON/Coding/")

def get_times(time_file): #PRACTICE2
    '''string -> list
    time_file: name of file that contains the timestamps
    Return list of time listed in "time_file", but as one float each'''
    
    list_of_times = []
    f=open(time_file)
    line = f.readline() #careful with titles in files
    while line != "":
        components = line.split(":")
        time = float(int(components[0]) * 86400) + (int(components[1]) * 3600) + \
        (int(components[2]) * 60) + float(components[3]) #careful with day number
        list_of_times.append(time)
        line = f.readline()
    return list_of_times

def append_times(time_file, time):
    '''(string, float) -> 
    time_file: name of the file that contains the timestamps
    time: the time in float that will be appended to "time_file"
    Modify "time_file" and do not return anything'''
    
    day = int(time//86400)
    time -= (day * 86400)
    hour = int(time//3600)
    time -= (hour * 3600)
    min = int(time//60)
    time -= (min * 60)
    sec = format(time, ".3f")
    newline = str(day) + ":" + str(hour) + ":" + str(min) + ":" + sec + "\n"
    with open(time_file, "a") as f:
        f.write(newline)
    print(newline)


get_times("test_times.txt", 3)
append_times("test_times.txt", 90061.1)
append_times("test_times.txt", 0.005)