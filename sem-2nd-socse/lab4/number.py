rows = int(input("enter a number: "))
for i in range(1,rows+1):
        print(""*(rows-i)+"".join(str(num) for num in range(1,i+1)))
