m=int(input("Enter the no of rows"))
n=int(input("Enter the no of columns"))
matrix=[]
print("Enter the elements row wise (space seperated): ")
for i in range(m):
    row_input=list(map(int, input().split()))
    if len(row_input) !=n:
        print(f"Error: Expected {n} elements for row {i + 1}, but got {len(row_input)}. Please re-enter.")
        i -= 1  # Decrement to re-enter the same row
        continue
    matrix.append(row_input)

    print("\nThe entered matrix is:")
    for row in matrix:
        print(row)