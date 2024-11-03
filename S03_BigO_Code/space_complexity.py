
### -5- space complexity O(1)
def boooo(n):
    for _ in range(n):
        print("booooo")

### -6- space complexity O(n)
def hi_ntimes(n):
    hi_array = []
    for _ in range(n):
        hi_array.append("hi")
    return hi_array

boooo(5)
print(hi_ntimes(6))
