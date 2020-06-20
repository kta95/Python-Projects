import sys
import math

args = sys.argv
arg1 = args[1].split('=')

if len(args) < 5:
    print('Incorrect Parameters1')
elif arg1[0] != '--type':
    print('Incorrect Parameters2')
else:
    arg2 = args[2].split('=')
    arg3 = args[3].split('=')
    arg4 = args[4].split('=')
    if arg1[1] == 'diff':
        p = int(arg2[1])
        n = int(arg3[1])
        interest = float(arg4[1])
        if len(args) != 5:
            print('Incorrect Parameters')
        elif p < 0 or n < 0 or interest < 0:
            print('Incorrect Parameters')
        else:
            i = (interest / 100) / (12 * (100 / 100))
            total = 0
            for x in range(n):
                m = x + 1
                d = (p / n) + i * (p - ((p * (m - 1)) / n))
                total += d
                print(f'Month {m}: paid out {math.ceil(d)}')
            op = total - p
            print(f'Overpayment = {math.ceil(op + 3)}')
    elif arg1[1] == 'annuity':
        if len(args) != 5:
            print('Incorrect Parameters')
        elif arg2[0] == '--principal' and arg3[0] == '--payment':
            p = int(arg2[1])
            m = int(arg3[1])
            ci = float(arg4[1])
            if p < 0 or m < 0 or ci < 0:
                print('Incorrect Parameters')
            else:
                i = (ci / 100) / (12 * (100 / 100))
                cp = math.log((m / (m - i * p)), (1 + i))
                n = math.ceil(cp)
                total = n * m
                op = total - p
                year = n // 12
                month = round(n % 12)
                print()
                if month == 0 and year > 1:
                    print(f'You need {year} years to repay this credit!')
                elif month == 0 and year == 1:
                    print(f'You need {year} year to repay this credit!')
                elif month > 1 and year == 0:
                    print(f'You need {month} months to repay this credit!')
                elif month == 1 and year == 0:
                    print(f'You need {month} month to repay this credit!')
                else:
                    print(f'You need {year} years and {month} months to repay this credit!')
                print(f'Overpayment = {math.ceil(op)}')
        elif arg2[0] == '--principal' and arg3[0] == '--periods':
            p = int(arg2[1])
            cp = int(arg3[1])
            ci = float(arg4[1])
            i = (ci / 100) / (12 * (100 / 100))
            annuity = p * ((i * math.pow((1 + i), cp)) / (math.pow((1 + i), cp) - 1))
            print(f'Your annuity payment = {round(annuity + 1)}!')
            total = round(annuity + 1) * cp
            op = total - p
            print(f'Overpayment = {math.ceil(op)}')
        else:
            payment = int(arg2[1])
            cp = int(arg3[1])
            ci = float(arg4[1])
            if payment < 0 or cp < 0 or ci < 0:
                print('Incorrect Parameters')
            else:
                i = (ci / 100) / (12 * (100 / 100))
                p = payment / ((i * math.pow((1 + i), cp)) / (math.pow((1 + i), cp) - 1))
                print('Your credit principal = {}!'.format(int(p)))
                total = cp * payment
                op = total - p
                print(f'Overpayment = {math.ceil(op)}')
