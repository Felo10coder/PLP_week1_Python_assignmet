## Week-2 assignment

# Create an empty list
my_list = []
print(my_list)

# Append elements 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print(my_list)

# Inserting 15 at the second position 
my_list.insert(1, 15)

print (my_list)

# Extending my_list with the list [50,60,70]
my_list.extend([50, 60, 70])

print (my_list)

# Removing the last element
my_list.pop()
print (my_list)

# Sorting  in ascending order
my_list.sort()
print (my_list)

# Find and print the index of value 30
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)


