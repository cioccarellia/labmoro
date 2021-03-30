# Confrontiamo tempi di risposta

import requests as req
import matplotlib.pyplot as mpl
import numpy as np

# Flags
debug = 1

# Config
ping_count = 10
urls = [
    "https://www.toptechboy.com",
]

labels = [
    "amazon.com",
    "amazon.it",
    "amazon.co.uk",
]


# Functions
def httpms(url):
    response = req.get(url)
    elapsed = response.elapsed.microseconds / 1000

    if debug:
        print("[D] HTTP-ed ", url, "with", elapsed, "ms")

    return elapsed


global_https = {}
maxes = []

for url in urls:
    url_pings = []

    print("\nProbing", url)
    for _ in range(0, ping_count):
        ms = httpms(url)
        url_pings.append(ms)

    if debug:
        print("[D] Done", url)

    global_https[url] = url_pings

    max_time = np.max(url_pings)
    avg_time = np.average(url_pings)
    min_time = np.min(url_pings)

    print("\nStats for", url)
    print("Max:\t", max_time)
    print("Avg:\t", avg_time)
    print("Min:\t", min_time)

    maxes.append(np.max(url_pings))

#Plotting
mpl.figure()
mpl.xlabel("iteration")
mpl.ylabel("ms")
mpl.ylim([0, np.max(maxes)])

mpl.title("Response times")

for url in urls:
    mpl.plot(global_https[url], label=url)

mpl.legend(loc="lower left", fontsize=6)
mpl.show()
