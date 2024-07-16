while True:
    n = int(input("The number of Fibonacci series: "))
    a, b = 1, 1
    count = 0
    while True:
        if n <= 0:
            print("Not vaild number for Fibonacci series, please enter postive integer.")
        
        elif n >= 1:
            print("Fibonacci series upto", n)

        while count<n:
            print(a)
            temp = a + b
            a = b
            b = temp
            count += 1
        break