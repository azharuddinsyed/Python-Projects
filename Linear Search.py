# Linear search
element_list=[7, 5, 2, 8, 5, 2, 8, 0, 6, 1]
isFound = False
input1 = int(input("Enter the element to be searched:"))
for j in element_list:
  if j == input1:
      isFound = True
      print("{} found at position {} in the list".format(input1,element_list.index(input1)))

if isFound != True:
  print("{} not found in list".format(input1))