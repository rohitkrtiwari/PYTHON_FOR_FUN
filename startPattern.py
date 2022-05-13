# Code 1
# num = int(input("Enter the number of rows: "))
# for i in range(1, num+1):
#     for j in range(1, i+1):
#         print("*",end="\t")
#     print()


# code 2
rows = int(input("Enter number of rows: "))
k = 0
for i in range(1, rows+1):
    for space in range(1, (rows-i)+1):
        print(end="  ")
    while k!=(2*i-1):
        print("* ", end="")
        k += 1
    k = 0
    print()
