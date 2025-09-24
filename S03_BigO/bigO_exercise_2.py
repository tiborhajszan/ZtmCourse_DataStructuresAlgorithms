
### What is the Big O of the function below? Hint: You may want to go line by line...

def another_fun_challenge(input):

    a = 5  # O(1)
    b = 10  # O(1)
    c = 50  # O(1)

    for item in input:  # O(n)
        x = item + 1  # O(n)
        y = item + 2  # O(n)
        z = item + 3  # O(n)   

    for element in input:  # O(n)
        p = element * 2  # O(n)
        q = element * 2  # O(n)
    
    whoAmI = "I don't know"  # O(1)

### Big O = 3*1 + 4n + 3n + 1 = 7n + 4 >>> O(n)
