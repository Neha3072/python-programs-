# find the average of numbers in alist using a for loop
#n=int(input("enter the number of element to be insert:"))
#sum=0
#for i in range (0,n):
    #e=int(input("enter the element:"))
    #sum=sum+e
   # average=sum/n
    #print("average element in the list:")

a=[3,5,7,9,6]
for i in a:
    avg=sum(a)/len(a)
    print(avg)