import time
import datetime

def getTime():
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%M-%D %H:%M:%S')
    return st

print('choose the number')
print('1. deposit    2.withdrawal')
selctitem = int(input())

# 입금
if selctitem == 1:
    print('deposit how much?')
    MoneyInput = int(input())
    print('any memo?')
    whyDeposit = input()

    # 읽기
    with open(r'C:\Users\lnfsg\Desktop\VsPython\source\repos\PythonChapter07\money.txt', 'r') as f01:
        MoneyBefore = int(f01.read())

    # 계산하기
    MoneyAfter = str(MoneyBefore + MoneyInput)
    
    # memo.txt에 남기기
    with open(r'C:\Users\lnfsg\Desktop\VsPython\source\repos\PythonChapter07\money.txt', 'w') as f02:
        f02.write(MoneyAfter)

    # pocketMoneyRegister.txt에 남기기
    with open(r'C:\Users\lnfsg\Desktop\VsPython\source\repos\PythonChapter07\pocketMoneyRegister.txt', 'a') as f03:
        f03.write('------------deposit-------------\n')
        f03.write(getTime() + '\n')
        f03.write(whyDeposit + '\n')
        f03.write(str(MoneyInput) + ' -> into your account' + '\n')
        f03.write('My bank blance: ' + str(MoneyAfter) + '\n')
    
    # 유저한테 보여주기
    print('complete!')
    with open(r'C:\Users\lnfsg\Desktop\VsPython\source\repos\PythonChapter07\pocketMoneyRegister.txt', 'r') as f04:
        a = f04.readlines()
        
        for i in range(-5, 0, 1) :
            b = a[i]
            print(b)

# 출금
elif selctitem == 2:
    print('withdrawal how much?')
    MoneyInputW = int(input())
    print('any memo?')
    whyWithdrawal = input()
    
    # 읽기
    with open(r'C:\Users\lnfsg\Desktop\VsPython\source\repos\PythonChapter07\money.txt', 'r') as g01:
        MoneyBeforeW = int(g01.read())

    # 계산하기
    MoneyAfterW = str(MoneyBeforeW - MoneyInputW)

    # memo.txt에 남기기
    with open(r'C:\Users\lnfsg\Desktop\VsPython\source\repos\PythonChapter07\money.txt', 'w') as g02:
        g02.write(MoneyAfterW)

    # pocketMoneyRegister.txt에 남기기
    with open(r'C:\Users\lnfsg\Desktop\VsPython\source\repos\PythonChapter07\pocketMoneyRegister.txt', 'a') as g03:
        g03.write('-------------withdrawal------------\n')
        g03.write(getTime() + '\n')
        g03.write(whyWithdrawal + '\n')
        g03.write(str(MoneyInputW) + ' -> out of your account' + '\n')
        g03.write('My bank blance: ' + str(MoneyAfterW) + '\n')

    # 유저한테 보여주기
    print('complete!')
    with open(r'C:\Users\lnfsg\Desktop\VsPython\source\repos\PythonChapter07\pocketMoneyRegister.txt', 'r') as g04:
        a = g04.readlines()

        for i in range(-5, 0, 1) :
            b = a[i]
            print(b)


else: 
    print('WRONG INPUT')
