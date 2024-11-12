#count the number of vowels in astring using a for loop
str=input("enter the string:")
count=0
for i in str:
    if(i=='a')or(i=='e')or(i=='i')or(i=='o')or(i=='u'):
        count+=1
        if(count==0):
            print("no vowels found")
           
        else:
            print("total vowels are:")
            print(count)
