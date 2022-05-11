def fib(n):
    a = 0
    b = 1
    if n == 0:
        print(a)
    elif n == 1:
        print(b)
    elif n < 0:
        print("Enter a Positive Integer")
    else:    
        print(a)
        print(b)
        for i in range(2, n):
            c = a + b
            a = b
            b = c
            if c>=n:
                break
            print(c)
fib(int(input("Enter a Number: ")))
