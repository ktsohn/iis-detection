##Practice with graphing
'''
creating sample spikes
plotting
'''

import os
os.chdir("/Volumes/KINGSTON/Coding/")

import matplotlib.pyplot as pt

def graph_spike(spike, frequency, window):
    '''(list of float, int, float) -> int
    
    spike: list of floats containing values for spike at every 0.004
    return 0
    frequency: frequency of recording
    window: length of spike window'''
    
    x = []
    j = 0.0
    while j < window:
        x.append(j)
        j += 1/frequency
    
    pt.plot(x, spike)
    figure_name = input("Figure title: ")
    pt.savefig(figure_name + ".png")
    return 0



def select_sample(data_file, index, start_time, n): #PART 1
    '''(str, str, float) -> list of floats
    data_file: name of the data file
    index: index of channel
    start_time: the value for the beginning of the window
    n: number of points per window (window * frequency)
    
    Return values for channel and time frame specified
    Include start_time and end 300ms (n samples) later'''
    
    f = open(data_file)
    first_line = f.readline()
    line = f.readline()
    currtime = float(line.split(",")[0])
    if currtime > start_time:
        start_time += 86400
    while currtime != start_time:
        line = f.readline()
        currtime = float(line.split(",")[0])
    window = []
    for i in range(n):
        window.append(float(line.split(",")[index]))
        line = f.readline()
    return window

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

def make_sample_spike(data_file, index, time_file, sample_number, n): #PART 1
    '''(string, string, int) -> (list)
    data_file: name of the data file
    index: index of channel
    time_file: name of the file that contains the timestamps
    sample_number: number of hand-picked samples to be averaged
    n: number of points per window (window * frequency)
    
    Use
    select_sample
    get_times
    
    Make dictionary of sample_number spikes
    Return list containing an average'''
    
    spikes = {}
    sample_spike = []
    time_list = get_times(time_file)
    print(time_list)
    for time in time_list:
        spikes[time] = select_sample(data_file, index, time, n)
    for j in range(n):
        avg = 0
        for keys in spikes:
            avg += spikes[keys][j]
        sample_spike.append(avg/float(sample_number))
    return sample_spike


graph_spike(make_sample_spike("SaKh10_spiketrain.csv", 4, "spiketrainRFP.txt", 5, 75), 250, 0.3)