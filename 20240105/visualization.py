import matplotlib.pyplot as plt
#데이터 시각화

datax = ["kim", "park", "nam"]
math = [43, 57, 97]
eng = [100, 87, 92]
chemistry = [55, 28, 99]
physics = [83, 90, 15]

#라벨을 설정하는 함수: xlable, ylable, title
plt.xlabel("Student Name")
plt.ylabel("M&E Score")

plt.title("Score of Th S")

#선 그래프 : plot
#첫 번째 전달 데이터: x 축, 두 번째: y축, 세 번째: 범례 -> label = " "
#범례의 위치를 조정해주는 함수 .legend()
#upper center, upper left, upper right, center, center right, lower left, lower right, lower center
plt.plot(datax, math, label = "Math", color = "cyan", linestyle="-", marker = "o")
plt.plot(datax, eng, label = "Eng", color ="magenta", linestyle="--", marker="*")
plt.plot(datax, chemistry, label = "Chemisty", color ="Olive", linestyle="-.", marker="s")
plt.plot(datax, physics, label = "Physics", color ="royalblue", linestyle=":", marker="d")
plt.legend(loc = "lower center")
plt.show()

'''
선 색깔
cyan: 하늘색
magenta: 자주색?
'''

'''
선 스타일
- 실선
-- 파선
-. 일점쇄선
: 점선
'''

'''
marker
o 
x
s 네모
d 다이아몬드
*
'''
