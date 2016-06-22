import os
os.chdir("/Volumes/KINGSTON/")

def convert_time(hour, min, sec, milisec):
    '''(int, int, int, int) -> float
    Return time converted into single float'''
    
    time = (3600*hour) + (60*min) + sec + (0.001*milisec)
    return time

##Work on getting rid of \n - did it with .rstrip
def get_values_time(filename, time):
    '''(str, float) -> dict{str:float}
    Return values for time specified'''

    f = open(filename)
    first_line = f.readline()
    channels = first_line.split("-Ref,")
    channels[-1] = channels[-1].rstrip("-Ref\n")
    del channels[0]
    dict = {}
    
    line = f.readline()
    currtime = float((line.split(","))[0])
    
    while currtime != time:
        line = f.readline()
        currtime = float((line.split(","))[0])
    
    for i in range(len(channels)):
        dict[channels[i]] = float((line.split(","))[i+1])

    print(dict)

get_values_time("file01.csv", 28649.046)

def get_values_channel(filename, channel, start_time, end_time):
    '''(str, str, float, float) -> dict{float:float}
    Return values for channel and time frame specified
    Include both start_time and end_time
    Works for a single time (enter same time for start_time and end_time'''
    
    f = open(filename)
    first_line = f.readline()
    time_and_channels = first_line.split("-Ref,")
    dict = {}
    for i in range(len(time_and_channels)):
        if time_and_channels[i] == channel:
            index = i
    line = f.readline()
    currtime = float((line.split(","))[0])
    while currtime != start_time:
        line = f.readline()
        currtime = float((line.split(","))[0])
    while currtime != end_time:
        dict[currtime] = float((line.split(","))[index])
        line = f.readline()
        currtime = float((line.split(","))[0])
    dict[currtime] = float((line.split(","))[index])
    
    print(dict)

get_values_channel("file01.csv", "LMT3", 28649.046, 28649.046)