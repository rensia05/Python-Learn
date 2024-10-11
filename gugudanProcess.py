while True:

    dan = int(input("구구단 몇 단을 계산할까?\n"))

    if (dan == 0):
        print('End of Process')
        break

    print(f"구구단 {dan}단을 계산한다.")

    for i in range(10):
        print(f"{dan} x {i+1} = {dan * (i+1)}")