score = int(input("점수를 입력하세요 : "))

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
elif score < 60:
    grade = 'F'

print(grade)
