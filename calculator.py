## ???????

# ??????????????? int
income = int(input('请输入工资:'))

# ????
salary = 0  

# ??????
shouldPay = 0

# ????
tax = 0 

def calculator(num):
    """计算税后薪资的函数，参数为原始收入"""

    # ??????????5000
    shouldPay = num - 5000

    # ????????????????????????
    if shouldPay <= 0:
        tax = 0
    elif 0 < shouldPay <= 3000:
        tax = shouldPay * 0.03
    elif 3000 < shouldPay <=12000:
        tax = shouldPay * 0.10 -210
    elif 12000 < shouldPay <=25000:
        tax = shouldPay *0.20 -1410
    elif 25000 < shouldPay <=35000:
        tax = shouldPay *0.25-2660
    elif 35000 < shouldPay <=55000:
        tax = shouldPay *0.30 - 4410
    elif 55000 < shouldPay <=8000:
        tax = shouldPay*0.35 -7160
    else:
        tax = shouldPay*0.4 - 15160
    salary = income - tax
    return '{:.2f}'.format(salary)


    # ?????????????????????

    # ??????

# ??
print('你的税后收入是：{}'.format(calculator(income)))
