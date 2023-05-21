list1=[12,-7,5,64,-14]
list2=[12,14,-95,3]
print("unchanged list")
num1=list(filter(lambda x:x>0,list1))
num2=list(filter(lambda x:x>0,list2))
print( num1)
print(num2)
