
### printing items of array and their sums

def pair_sums(numbers):

    print("These are the numbers:") # O(1)
    for number in numbers: # O(n)
        print(number)

    print("These are their sums:") # O(1)
    for first_number in numbers: # O(n^2)
        for second_number in numbers:
            print(first_number + second_number)

pair_sums([1, 2, 3, 4, 5])

### Big O = 1+n + 1+n^2 = n^2 + n + 2 = O(n^2)
