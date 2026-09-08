n = int(input("Enter a number:"))

count = 0
while n:
    count++n&1
    n=n>>1
    print("Number if set bits+",count)
    