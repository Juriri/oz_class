def cal_grade(students):
    scores = [score for _, score in students]
    max_score = max(scores)
    min_score = min(scores)

    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def main():
    students = []

    print("학생 이름과 점수를 입력하세요. 종료하려면 빈 줄을 입력하세요.")
    while True:
        try:
            line = input("입력 (예: 김홍도 88): ").strip()
            if not line:
                break
            name, score_str = line.split()
            score = int(score_str)
            students.append((name, score))
        except ValueError:
            print("입력 형식이 올바르지 않습니다. 예: 김홍도 88")
        except Exception as e:
            print("오류 발생:", e)

    if students:
        cal_grade(students)
    else:
        print("입력된 학생이 없습니다.")

if __name__ == "__main__":
    main()
  # 등급 매기기 (A: 90~100, B: 89: 80)
  # 결과를 파일로 저장
