import requests
import numpy

import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")

# Flags
debug = 1

# Parameters
url = "http://www.toptechboy.com"
ping_count = 50

# Current Data
total_ping_elapsed_sum = 0
elapsed_time_list = []


def ping(i):
    global total_ping_elapsed_sum, elapsed_time_list

    current_ping_elapsed = requests.get(url).elapsed.microseconds / 1000

    if debug:
        print("[D] Hit", i, "\t", current_ping_elapsed, "ms")

    total_ping_elapsed_sum += current_ping_elapsed
    elapsed_time_list.append(current_ping_elapsed)


# Processing pings
print("Sending out", ping_count, "requests to", url)
for pingIndex in range(1, ping_count):
    ping(pingIndex)


# Report
print("\n\nDone")
print("Maximum: ", numpy.max(elapsed_time_list), "ms")
print("Average: ", numpy.average(elapsed_time_list), "ms")
print("Minimum: ", numpy.min(elapsed_time_list), "ms")


# Plotting
print("Generating plot")
plt.figure()

plt.xlabel("t")
plt.ylabel("ms")
plt.title("Response times")

plt.plot(numpy.average(elapsed_time_list))

plt.show()