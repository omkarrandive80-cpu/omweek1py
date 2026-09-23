#WAP to create lst of 10elements and print first ,last and middle elements of the list.
list1=[10,20,30,40,50,60,70,80,90,100]
print("First element of list:",list1[0])
print("Last element of list:",list1[9])
print("Middle element of list:",list1[4])
#WAP to create sum and average of list
list2=[5,10,15,20,25]
sum=0
for index in range(0,5,1):
  sum=sum+list2[index]
print("Sum of the all elemnts in list",sum)
print("Average element   of the list",sum/len(list2))
#
list3=[4,2,8,7,3,5,1,10,12]
lenght=len(list3)
count_even=0
count_odd=0
for index in range (0,lenght,1):
  if list3[index] % 2 == 0:
    count_even=count_even+1
  else:
    print(list3[index])
    count_odd=count_odd+1

print("NO. of even elements :",count_even) 
print("No. of odd elemnts :",count_odd)
    
  #
list4=[4,2,8,7,3,5,1,10,12,15]
lenght=len(list4)
count_even=0
count_odd=0
for index in range (0,lenght,1):
  if list4 [index] % 2 == 0:
    count_even=count_even+1
else:
    count_odd=count_odd+1
print("NO. of even elements :",count_even) 
print("No, of odd elemnts :",count_odd)
#5 wAr to find maximum and minimum element in a list 
l1=[10,15,1,105,2,100]
largest=l1[0]
for i in range(0,6,1):
  if largest<l1[i]:
    largest=l1[i]
print("largest element in the list is :",largest)

smallest=l1[0]
for i in range(0,6,1):
  if smallest>l1[i]:
     smallest=l1[i]
print("smallest element in the list is :",smallest)
#WAP to find the second largest element in a list
l2=[10,15,1,105,2,100]
largest=l2[0]
second_largest=l2[0]
for i in range(0,6,1):
  if largest<l2[i]:
    second_largest=largest
    largest=l2[i]
  elif second_largest<l2[i] and l2[i]!=largest:
    second_largest=l2[i]
print("Second largest element in the list is :",second_largest)
#7wap to find count of a no. 3 from the list
l2=[1,2,2,3,3,3,4,4,4,4]
count_of_3=0
for i in range(0,10,1):
  if l2[i]==3:
    count_of_3+=1
print("the count of 3 is :", count_of_3)
#8 wap to segrigate +ve and -ve no. from list to two different list
l3=[-1,2,-3,4,-5,6,-7,8,-9,10]
positive_list=[]  
negative_list=[]
for i in range(0,10,1):
  if l3[i]>0:
    positive_list.append(l3[i])
  else:
    negative_list.append(l3[i])
print("Positive elements in the list are :",positive_list)
print("Negative elements in the list are :",negative_list)
    
