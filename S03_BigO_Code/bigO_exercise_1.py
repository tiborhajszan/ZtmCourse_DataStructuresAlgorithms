
### What is the Big O of the function below? Hint: You may want to go line by line...

def funChallenge(input):
  
    a = 10 # O(1)
    a = 50 + 3 # O(1)

    for item in input: # O(n)
        anotherFunction() # O(n)
        stranger = True # O(n)
        a += 1 # O(n)
    
    return a # O(1)

### Big O = 1 + 1 + n + n + n + n + 1 = 3 + 4n = O(4n+3) >>> O(n)
