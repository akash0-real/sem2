n = int(input("enter a value: "))
d = n-1
a = 1
for i in range(n):
        print("  "*d,end=" ")
        for k in range(a):
                print("*",end=" ")
        print("\n")
        d=d-1
        a=a+2
        
for i in range(n,0,-1):
            print(" "*d,end="")
            for k in range(a,0,-1):
                print("*",end=" ")
            print("\n")
            d=d+1
            a=a-2
