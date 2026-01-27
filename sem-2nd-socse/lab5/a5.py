def  pattren(n):
    for  i  in  range (1,n+1):
        row=""
        for  j  in  range(i):
            row += chr(64 +j)
        print(row)
    for i in range(n-1,0,-1):
        row=""
        for j in range(i):
            row+=chr(64+j)
        print(row)

n=int(input("enter the number"))
print(pattren(n))
