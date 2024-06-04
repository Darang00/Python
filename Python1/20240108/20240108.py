import matplotlib.pyplot as plt
from matplotlib import rc

rc("font", family="Malgun Gothic") #맑은 고딕 한글 폰트 사용

datax=["김", "박", "남"]
korean=[100, 76, 89]
math=[56, 32, 76]
#서브 그래프

fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(9, 3), sharex=True, sharey=True)
#sharex=True: x축을 datax 애들이 공유하겠다.
#sharey=True: y축을 datax 애들이 공유하겠다.

ax=axs[0]
ax.scatter(datax, korean)
ax.set_title("Korean Score")

ax=axs[1]
ax.scatter(datax, math)
ax.set_title("Math Score")


fig.suptitle("Subject Score")
plt.show()


plt.title("국어 성적")
plt.scatter(datax, datay)   #산포그래프
#plt.bar(datax, datay)  #x, y 막대그래프, plot(선그래프)
plt.ylabel("성적")

plt.show()
