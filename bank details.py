balance=1000
print('''
welcome to sukumar
1.check balance
2.withdraw
3.deposit
4.exit ''')
while True:
    choice=int(input('enter the choice:'))
    if choice==1:
        print('the balance is',balance)
        #another=input('do u want to make another transaction? YES/NO')
        #if another=="YES":
         #   continue
        #else:
         #   break
    elif choice==2:
        withdr=float(input('enter the withdraw amount:'))
        if balance>withdr:
            total=balance-withdr
            print('sucess')
            print("your remaining balance is",total)
        else:
            print('inuffiencent balance')
    elif choice==3:
        deposit=float(input('enter the deposit amount:'))
        totalbal=balance+deposit
        print('the new balnce',totalbal)
    elif choice==4:
        print('eixt the program')
        #exit()
    else:
        print('no selected transaction')
    another=input('do u want to make another transaction? yes/no')
    if another=='yes':
        continue
    else:
        break
                    
    
    
