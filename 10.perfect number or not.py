num=int(input('enter the number:'))
sum=0
for i in range(1,num):
    if num%i==0:
        sum=sum+i
if sum==num:
    print(num,'is a perfect number')
else:
    print(num ,'is not a perfect number')
        
    
    
