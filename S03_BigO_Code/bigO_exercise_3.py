
### What is the Big O of the function below? Hint: You may want to go line by line...

def print_firstitem_firsthalf_say100hi(items):

    print(items[0]) # O(1)

    middle_index = len(items) // 2 # O(1)
    index = 0 # O(1)
    while index < middle_index: # O(n)
        print(items[index]) # O(n)
        index += 1 # O(n)

    for counter in range(100): # O(100)
        print('hi') # O(100)

### Big O = 1 + 2*1+3n + 2*100 = 3n + 203 >>> O(n)
