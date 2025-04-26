import matplotlib.pyplot as plt

# 사용자 입력 데이터 (예시로 고정)
weight, body_fat, muscle_mass = map(float, input("체중, 체지방률, 근육량 순으로 입력하세요: ").split(", "))

# 그래프 생성
fig, ax = plt.subplots()

# 인바디처럼 표현하기 위한 항목들
categories = ['body_fat (%)', 'muscle (kg)', 'weight (kg)']
values = [body_fat, muscle_mass, weight]

# 수평 그래프 그리기
bars = ax.barh(categories, values, color=['blue', 'green', 'red'])

# 그래프 제목과 레이블 설정
ax.set_title("인바디 데이터")
ax.set_xlabel("수치")

# 각 바 옆에 숫자 표시
for bar in bars:
    width = bar.get_width()  # 바의 너비 (즉, 값)
    ax.text(width + 0.5, bar.get_y() + bar.get_height() / 2, f'{width:.2f}', va='center', ha='left', color='black')

# 그래프 출력
plt.tight_layout()
plt.savefig('inbody_graph_horizontal_with_numbers.png')  # 그래프를 로컬에 저장

# 그래프 보여주기
plt.show()
