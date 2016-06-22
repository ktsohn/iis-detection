##Part 1
'''
Average 10 sample spikes that are hand picked
-alligning spikes?
-better input method?
'''

import os
os.chdir("/Volumes/KINGSTON/")

def convert_time(hour, min, sec):
    '''(int, int, float) -> float
    Return time converted into single float'''
    
    time = (3600*hour) + (60*min) + sec
    return time


def select_sample(filename, channel, start_time):
    '''(str, str, float) -> list of floats
    Return values for channel and time frame specified
    Include start_time and end 300ms (75 samples) later'''
    
    f = open(filename)
    first_line = f.readline()
    time_and_channels = first_line.split("-Ref,")
    time_and_channels[-1] = time_and_channels[-1].rstrip("-Ref\n")
    for i in range(len(time_and_channels)):
        if time_and_channels[i] == channel:
            index = i
    line = f.readline()
    currtime = float((line.split(","))[0])
    if currtime > start_time:
        start_time += 86400
    while currtime != start_time:
        line = f.readline()
        currtime = float((line.split(","))[0])
    window = []
    for n in 75: #modify this if size of window is changed from 300ms
        window.append = float((line.split(","))[index])
        line = f.readline()
    
    print(window)
    return avg

def average_windows(w0, w1, w2, w3, w4, w5, w6, w7, w8, w9):
    '''(list ... list) -> (list)
    Average 10 lists in a brute force way'''
    
    avg = []
    for i in 75: #N
        avg[i] = (w0[i] + w1[i] + w2[i] + w3[i] + w4[i] + w5[i] + w6[i] + w7[i] + w8[i] + w9[i])/10
    print(avg)
    return avg


def make_sample_spike(filename, channel, sample_number):
    '''(string, string) -> (list)
    Use convert_time and select_sample to make dictionary of 10 spikes
    sample_number is the number of handpicked samples to be used
    Return list containing an average of every 0.004s'''
    
    spikes = {}
    sample_spike = []
    for n in sample_number:
        print("Spike number %d\n", n)
        h = int(input("hour: "))
        m = int(input("minute: "))
        s = float(input("second: "))
        spikes[n] = select_sample(filename, channel, convert_time(h, m, s))
    for i in 75: #N
        avg = 0
        for keys in spikes:
            avg += spikes[keys][i]
        sample_spike[i] = avg/float(sample_number)
    return sample_spike