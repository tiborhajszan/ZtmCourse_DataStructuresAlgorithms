
### print all pairs of array

boxes = ['a', 'b', 'c', 'd', 'e']

def pairs_of_array(array):
  for item in array:
    for jtem in array:
      print(item, jtem)

pairs_of_array(boxes)
