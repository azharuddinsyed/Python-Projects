#       BINARY SEARCH

element_list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
isFound=False
middle = int((len(element_list)-1)/2)

input1 = int(input("Enter number to be searched:"))

# checking whether the middle element = searching element
if input1 == element_list[middle]:
  isFound=True
  print("{} found at index pos {}".format(input1, middle))
# check if input element < middle
elif input1 < element_list[middle]:
    for i in element_list[:middle]:
      if i == input1:
        isFound=True
        print("{} found at index pos {}".format(input1,element_list.index(i)))
# check if input element > middle
elif input1 > element_list[middle]:
    for i in element_list[middle:]:
      if i == input1:
        isFound=True
        print("{} found at index pos {}".format(input1,element_list.index(i)))

if isFound != True:
  print('{} not found in the list'.format(input1))