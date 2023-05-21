list1=[12,-7,5,64,-14]
list2=[12,14,-95,3]
print("original list that we have to do changes"+ str(list1))
num1=list(filter(lambda x:x>0,list1))
num2=list(filter(lambda x:x>0,list2))
print( num1)
print(num2)
