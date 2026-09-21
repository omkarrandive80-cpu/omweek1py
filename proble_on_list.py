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
    