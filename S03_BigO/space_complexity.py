
### -5- space complexity O(1)
def boooo(n):
    for _ in range(n):
        print("booooo")

boooo(5)
### Big sO = 0 = O(0) >>> O(1)

### -6- space complexity O(n)
def hi_ntimes(n):
    hi_array = [] # sO(1)
    for _ in range(n):
        hi_array.append("hi") # sO(n)
    return hi_array

print(hi_ntimes(6))
### Big sO = 1 + n = O(n+1) >>> O(n)
