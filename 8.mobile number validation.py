import re
def validation(phone):
    pattern="^[6-9][0-9]{9}$|^[+][9][1][6-9][0-9]{9}$"
    return re.search(pattern,phone)
while True:
    phone=input('enter the number:')
#while True:
    if validation(phone):
        print(phone,"number is valid")
        break
    else:
        print(phone,"number is not valid")
    another=input('do u want enter valid number y/n:')
    if another=='y':
        continue
    else:
        break
    
    
    

