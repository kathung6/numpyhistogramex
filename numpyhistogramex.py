import numpy as np

# reads data file
data = np.genfromtxt('data1.txt', delimiter=',')

# finds the minimum and maximum value of the file
min_value = np.min(data)
max_value = np.max(data)

# creates a histogram
hist_data, bins = np.histogram(data, bins=[-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7])

# prints the left edge of the bins and their counts
for i in range(len(hist_data)):
    print(f'{bins[i]} {hist_data[i]}')