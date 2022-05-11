list1 = [12, 23, 34]
# methods of a list
list1.append(76) # adds an element at the end of the list
# list1.clear() # remove all the elements of the list
list2 = list1.copy() # returns a copy of the list
list1.count(12) # returns the number of elements with the specified value
list1.extend(list2) # Add the elements of a list (or any iterable), to the end of the current list
list1.index(12) # Returns the index of the first element with the specified value
list1.insert(0, 6) # adds an element at the specified position of the list
list1.pop() # Removes the element at the specified position
list1.remove(12) # Removes the first item with the specified value
list1.reverse() # Reverses the order of the list
list1.sort() # Sort the list
print(list1)