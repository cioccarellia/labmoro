import numpy as np
import requests as rq

# Flags
debug = 1

# Config
urls = [
    "https://www.google.com",
    "https://www.youtube.com",
    "https://www.wikipedia.com",
]
probes = 5

# Probing
avg_snaps = {}

for url in urls:
    current_probes = []

    for _ in range(0, probes):
        current_probes.append(rq.get(url).elapsed.microseconds / 1000)

    avg_snaps[url] = {
        "name": url.replace("https://www.", "").upper(),
        "avg": np.average(current_probes)
    }

if debug:
    print(avg_snaps)

# Searching lowest ping
lowest = {
    "name": "",
    "avg": 0
}

for url in urls:
    if avg_snaps[url]["avg"] < lowest["avg"] or lowest["avg"] == 0:
        lowest = avg_snaps[url]

print("Lowest ping achieved by", lowest["name"], "with ping", lowest["avg"])
