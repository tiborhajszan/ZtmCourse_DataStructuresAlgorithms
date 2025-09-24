
### What is the time complexity of the function below? Hint: You may want to go line by line...

def fun_challenge(input):
  
    a = 10 # O(1)
    a = 50 + 3 # O(1)

    for item in input: # O(n)
        anotherFunction() # O(n)
        stranger = True # O(n)
        a += 1 # O(n)
    
    return a # O(1)

### Big O = 2*1 + 4n + 1 = 4n + 3 >>> O(n)
