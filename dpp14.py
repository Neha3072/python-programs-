# python program to check if a given number is armstrong number
num=int(input("check arm strong"))
f=num
sum=0
while(f>0):
    a%f=10
    f=int(f/10)
    sum=sum +(a**3)
    if(sum==num):
        print(num,"arm strong")