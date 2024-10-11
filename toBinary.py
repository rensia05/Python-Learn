decimal = int(input('type a number : '))
result = ' '
while (decimal > 0):
    remainder = decimal % 2
    decimal = decimal // 2
    result = str(remainder) + result
print(f'binary : {result}')