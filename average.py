kor_score = list(map(int, input('학생들의 국어 점수 입력 : ').split(',')))
math_score = list(map(int, input('학생들의 수학 점수 입력 : ').split(',')))
eng_score = list(map(int, input('학생들의 영어 점수 입력 : ').split(',')))
midterm_score = [kor_score, math_score, eng_score]

students_score = [0] * len(kor_score)

for subject in midterm_score:
    for i in range(len(subject)):
        students_score[i] += subject[i]

students_average = [score / 3 for score in students_score]
print(students_average)