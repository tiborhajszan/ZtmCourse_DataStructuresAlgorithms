
### 1 -- for loop in python

everyone = ["dory", "bruce", "marlin", "nemo", "gill", "bloat", "nigel", "squirt", "darla", "hank"]

def find_nemo_3(input):
    for item in input:
        print(item)
        if item == "nemo":
            print("\nFound NEMO!\n")
            break

find_nemo_3(everyone)
