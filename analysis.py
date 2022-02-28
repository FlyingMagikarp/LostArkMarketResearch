import csv
import matplotlib.pyplot as plt
import numpy


def format_timestamps_to_hour(timefull):
    return timefull.split(":")[0]

with open('data.csv') as f:
    reader = csv.reader(f)
    data = list(reader)

data.pop(0)

items, values, timesfull, days, dates = zip(*data)
times = []
for t in timesfull:
    # times.append(format_timestamps_to_hour(t))
    times.append(t)

plt.scatter(values, times)
plt.plot(values, times)
plt.show()

plt.scatter(times, values)
plt.plot(times, values)
plt.show()

print("done")