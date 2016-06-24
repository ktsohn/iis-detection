##Part 1
'''
Average 10 sample spikes that are hand picked
-alligning spikes?
-better input method?
'''

import os
os.chdir("/Volumes/KINGSTON/Coding/")


#def convert_time(hour, min, sec):
#    '''(int, int, float) -> float
#    Return time converted into single float'''
#    
#    time = (3600*hour) + (60*min) + sec
#    return time

def select_channel(data_file, channel):
    '''(str, str) -> int
    data_file: name of the data file
    channel: name of channel
    Return index of channel
    '''
    
    f = open(data_file)
    first_line = f.readline()
    time_and_channels = first_line.split("-Ref,")
    time_and_channels[-1] = time_and_channels[-1].rstrip("-Ref\n")
    for i in range(len(time_and_channels)):
        if time_and_channels[i] == channel:
            return i

def select_sample(data_file, index, start_time, n):
    '''(str, str, float) -> list of floats
    data_file: name of the data file
    index: index of channel
    start_time: the value for the beginning of the window
    n: number of points per window (window * frequency)
    
    Return values for channel and time frame specified
    Include start_time and end 300ms (75 samples) later'''
    
    f = open(data_file)
    first_line = f.readline()
    line = f.readline()
    currtime = float((line.split(","))[0])
    if currtime > start_time:
        start_time += 86400
    while currtime != start_time:
        line = f.readline()
        currtime = float((line.split(","))[0])
    window = []
    for i in range(n):
        window.append = float((line.split(","))[index])
        line = f.readline()
    
    return window

#def average_windows(w0, w1, w2, w3, w4, w5, w6, w7, w8, w9):
#    '''(list ... list) -> (list)
#    Average 10 lists in a brute force way'''
#    
#    avg = []
#    for i in 75: #N
#        avg[i] = (w0[i] + w1[i] + w2[i] + w3[i] + w4[i] + w5[i] + w6[i] + w7[i] + w8[i] + w9[i])/10
#    print(avg)
#    return avg


def make_sample_spike_manual(data_file, index, sample_number, n):
    '''(string, string, int) -> (list)
    data_file: name of the data file
    index: index of channel
    sample_number: number of hand-picked samples to be averaged
    n: number of points per window (window * frequency)
    
    Use
    convert_time
    select_sample
    
    Input time
    Make dictionary of sample_number spikes
    Return list containing an average = sample_spike'''
    
    spikes = {}
    sample_spike = []
    for i in range(sample_number):
        print("Spike number %d\n", n)
        h = int(input("hour: "))
        m = int(input("minute: "))
        s = float(input("second: "))
        spikes[i] = select_sample(data_file, index, convert_time(h, m, s))
    for j in range(n):
        avg = 0
        for keys in spikes:
            avg += spikes[keys][j]
        sample_spike[j] = avg/float(sample_number)
    return sample_spike

def make_sample_spike(data_file, index, time_file, sample_number, n):
    '''(string, string, int) -> (list)
    data_file: name of the data file
    index: index of channel
    time_file: name of the file that contains the timestamps
    sample_number: number of hand-picked samples to be averaged
    n: number of points per window (window * frequency)
    
    Use
    select_sample
    
    Make dictionary of sample_number spikes
    Return list containing an average'''
    
    spikes = {}
    sample_spike = []
    time_list = get_times(time_file)
    for time in time_list:
        spikes[time] = select_sample(data_file, index, time)
    for j in range(n):
        avg = 0
        for keys in spikes:
            avg += spikes[keys][j]
        sample_spike[j] = avg/float(sample_number)
    return sample_spike