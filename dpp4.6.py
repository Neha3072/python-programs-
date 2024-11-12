test_list=[1,7,5,6,3,8]
k=4
print("the list:"+ str(test_list))
count = 0
for i in test_list:
    if i>k:
        count = count +1
        
print("the numbers greater than 4 :" + str(count))