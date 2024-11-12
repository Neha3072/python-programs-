# print a pattern of stsr using nestsed for loop
n=int(input("enetr the number of rows:"))
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end=" ")
    print()