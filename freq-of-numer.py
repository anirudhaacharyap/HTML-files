n = input('Enter the number:')
digit = int(input("Num to find the occurrence:"))

def freq(n, digit):
    count = 0
    for i in n:
        if int(i) == digit:
            count += 1
    print(count)

freq(n, digit)
