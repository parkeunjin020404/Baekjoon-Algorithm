inputs = []
inputs2 = []
total_points = 0.0  # 총 점수 초기화
total_credits = 0.0  # 총 학점 초기화

for i in range(20):
    user_input = input()
    inputs.append(user_input)

for a in range(20):
    inputs2.append(inputs[a].split(" "))

for b in range(20):
    grade = inputs2[b][2]
    credits = float(inputs2[b][1])

    if grade != 'P':  # P 등급은 제외
        if grade == 'A+':
            total_points += 4.5 * credits
        elif grade == 'A0':
            total_points += 4.0 * credits
        elif grade == 'B+':
            total_points += 3.5 * credits
        elif grade == 'B0':
            total_points += 3.0 * credits
        elif grade == 'C+':
            total_points += 2.5 * credits
        elif grade == 'C0':
            total_points += 2.0 * credits
        elif grade == 'D+':
            total_points += 1.5 * credits
        elif grade == 'D0':
            total_points += 1.0 * credits
        elif grade == 'F':
            total_points += 0.0 * credits
        
        total_credits += credits  # 학점 합산

# 전공평점 계산
if total_credits > 0:  # 0으로 나누는 것을 방지
    a = total_points / total_credits
else:
    a = 0.0  # 경우에 따라 처리

print(a)
