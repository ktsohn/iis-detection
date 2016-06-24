##Part 3
'''
Detecting spikes
-collate everything?
-use of existing .txt files for recording spike times?
'''

import os
os.chdir("/Volumes/KINGSTON/Coding/")


def detection_and_addition(data_file, index, time_file, sample_spike, n, threshold):
    '''(string, string, string, int, int, list) -> int
    data_file: name of the data file
    index: index of the channel
    time_file: name of the file with timestamps
    sample_spike: list of floats that represents the sample spike template
    n: number of samples per window
    threshold: threshold for detection
    
    Use
    get_times
    compute_relation
    
    Modify .txt file with all the spike times
    Return the total number of spikes, including hand-picked and first pass
    '''
    f = open(data_file)
    first_line = f.readline()
    line = f.readline()
    list_of_times = get_times(time_file)
    count = len(list_of_times)
    while line != None:
        currtime = float((line.split(","))[0])
        if currtime not in list_of_times:
            window = []
            for n in range(n):
                window.append = float((line.split(","))[index])
            if compute_relation(window, sample_spike) > threshold:
                for i in (n):
                    sample_spike[i] = ((sample_spike[i] * float(count))\
                    + window[i])/float(count + 1)
                list_of_times.append(currtime)
                append_times(time_file, currtime)
                count += 1
        line = f.readline()
    
    return count