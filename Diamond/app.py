row = int(input("Enter the number of rows you want in your first half of diamond : "))

for i in range(1, row + 1):
    for j in range(1, row - i + 1):
        print(end=" ")
    for star in range(0, i * 2 - 1):
        print(end="*")
    print()
for i in range(1, row):
    for j in range(1, i + 1):
        print(end=" ")
    for star in range(1,2 * (row - i)):    
        print(end="*")    
    print()
