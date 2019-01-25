def prime_numbers(a):
    l = []
    for i in range(1, a+1):
        count = 0
        for b in range(1, i+1):
            if i%b == 0:
                count +=1
        if count == 2:
            l.append(i)
    str1 = ", ".join(str(e) for e in l)
    print("Prime numbers are " + str1)


enter = int(input("Enter your number "))

prime_numbers(enter)


