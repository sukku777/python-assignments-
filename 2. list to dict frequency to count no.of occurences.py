original_list=[11,45,8,11,23,45,23,45,89]
dict1={}
for i in original_list:
    if i in dict1:
        dict1[i]=dict1[i]+1
    else:
        dict1[i]=1
print( dict1)
   
