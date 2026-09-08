n = int(input("Enter a number:"))
k = int(input("Enter a k:"))

if n&(1<<k):
    print("kth bit is set")
else: 
    print("kth bit is not set")