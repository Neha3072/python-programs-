def is_positive(num):
    if(num>0):
        return "true"
    else:
        return "false"
num=int(input("enter the number:"))
result=is_positive(num)
print(result)
