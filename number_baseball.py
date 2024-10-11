from random import randint

number = randint(1,100)

count = int(input('정답 입력을 몇번으로 제한하시겠습니까? : '))

print('난수가 생성되었습니다.')
print('숫자를 맞혀보세요. (0 ~ 100)\n범위를 벗어난 답을 입력시 정답 횟수가 2배로 소진됩니다.')
while 1:
    p_input = int(input())
    if count > 0:
        if p_input < number:
            count -= 1
            print(f'숫자가 너무 작습니다. 남은 정답 횟수 : {count}')
        elif p_input > number:
            count -= 1
            print(f'숫자가 너무 큽니다. 남은 정답 횟수 : {count}')
        elif p_input > 100:
            count -= 2
            print(f'플레이어가 입력한 답이 난수생성 범위를 벗어났습니다. 남은 정답 횟수 : {count}')
        elif p_input == number:
            print(f'정답입니다! 게임을 종료합니다. 남은 정답 횟수 : {count}')
            break
    if count == 0:
        print(f'정답 횟수를 모두 소진하였습니다. 정답은 {number} 입니다.')
        break

