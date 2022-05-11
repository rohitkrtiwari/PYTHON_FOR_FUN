def pyramid(rows):
    for i in range(rows):
        print(''*(rows-i-1)+"*"*(i+1))

def pyramid2(rows):
    for i in range(0, rows):
        for j in range(0, rows-i-1):
            print(end=" ")
        for j in range(0, i+1):
            print("*", end=" ")
            
        print()
pyramid2(int(input("Enter the number of rows: ")))
