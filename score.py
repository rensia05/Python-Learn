scores = list(map(int,input("점수들을 입력하세요 (띄어쓰기로 값 구분) : ").split()))

for i in range(0,len(scores)):
    if scores[i] >= 95:
        print(f"{i+1}번 학생 : A+")
    elif scores[i] >= 90:
        print(f"{i+1}번 학생 : A0")
    elif scores[i] >= 85:
        print(f"{i+1}번 학생 : B+")
    elif scores[i] >= 80:
        print(f"{i+1}번 학생 : B")
    elif scores[i] >= 75:
        print(f"{i+1}번 학생 : C+")
    elif scores[i] >= 70:
        print(f"{i+1}번 학생 : C")
    elif scores[i] >= 60:
        print(f"{i+1}번 학생 : F")