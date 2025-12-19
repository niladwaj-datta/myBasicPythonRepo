# Creating a tuple
my_tuple = (1, 2, 3, "apple", "banana")

# Accessing elements
print(my_tuple[0])  # Output: 1
print(my_tuple[-1])  # Output: banana

# Tuples are immutable
try:
    my_tuple[1] = 10  # This will raise an error
except TypeError as e:
    print("Error:", e)

# Tuples can contain duplicates
duplicate_tuple = (1, 2, 2, 3, 3, 3)
print(duplicate_tuple)  # Output: (1, 2, 2, 3, 3, 3)