m = int(input("Enter the number of rows: "))
n = int(input("Enter the number of columns: "))
matrix = []

print("Enter the elements row wise (space separated):")

for i in range(m):
    while True:  # Keep asking until a valid row is entered
        row_input = list(map(int, input(f"Row {i + 1}: ").split()))
        if len(row_input) != n:
            print(f"Error: Expected {n} elements, but got {len(row_input)}. Please re-enter.")
        else:
            matrix.append(row_input)
            break  # Valid row, move to next

# Print the matrix only after all rows are entered
print("\nThe entered matrix is:")
for row in matrix:
    print(" ".join(map(str, row)))
