sample_string='The quick Brown Fox'
count=0
count1=0
for i in sample_string:
    if i.isupper():
        count=count+1
    elif i.islower():
        count1=count1+1
print('No.of Uppercase charcters:',count)
print('No.of Lowerrcase charcters:',count1)


