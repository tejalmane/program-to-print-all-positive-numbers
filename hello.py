list1=[12,-7,5,64,-14]
list2=[12,14,-95,3]
print("original list"+ str(list1))
num1=list(filter(lambda x:x>0,list1))
print("original list"+ str(list2))
num2=list(filter(lambda x:x>0,list2))
print("output of list1" + str(num1))
print("output of list2" + str(num2))
