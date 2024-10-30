### 1 -- for loop in python

import time

nemo = ["nemo"]
fish = ["dory", "bruce", "marlin", "nemo"]
everyone = ["dory", "bruce", "marlin", "nemo", "gill", "bloat", "nigel", "squirt", "darla", "hank"]
large = ["nemo"] * 100000

def find_nemo_2(input):
    t0 = time.time()
    for item in input:
        if item == "nemo":
            print("Found NEMO!")
    t1 = time.time()
    print("Function call took " + str(t1 - t0) + " seconds.")

find_nemo_2(large)
