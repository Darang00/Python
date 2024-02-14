# %%
# 필요한 모듈 import
import requests as req
from bs4 import BeautifulSoup as bs

# %%
# url 만들기
base_url = 'https://www.jobkorea.co.kr/Search/?stext=%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EB%B6%84%EC%84%9D&focusTab=&focusGno=43641436&tabType=recruit&Page_No='

page_no = 1

url = f'{base_url}{page_no}'

url

# %%
resp = req.get(url)

# print(resp.text)
bs(resp.content, 'html.parser')

# %%
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}

resp=req.get(url, headers=headers)

resp.text

soup = bs(resp.text, 'html.parser')

soup


# %%
# 요구 경력 조회
exp_tags = soup.select('span.exp')

exp_list = []

for tag in exp_tags :
  exp_list.append(tag.text)

exp_list

# 요구 학력 조회
edu_tags = soup.select('span.edu')

edu_tags

edu_list = []

for tag in edu_tags :
  edu_list.append(tag.text)

edu_list


# %%

# 함수화 시키기
def getExp(soup) :
  exp_tags = soup.select('span.exp')
  exp_list = []

  for tag in exp_tags :
    exp_list.append(tag.text)

  return exp_list

getExp(soup)

def getEdu(soup) :
  edu_tags = soup.select('span.edu')
  edu_list = []

  for tag in edu_tags :
    edu_list.append(tag.text)

  return edu_list

getEdu(soup)

# %%
import math

83/20
math.ceil(83/20)

total_string = soup.select('.dev_tot')[0].text

total_string

# replace() : 특정 문자를 내가 원하는 문자로 변경해준다.
total_string = total_string.replace(',', '')

total_page = math.ceil( int(total_string) / 20 )

total_page

# %%
# 함수화 시키기
def getTotalPage(soup):
  total_string = soup.select('.dev_tot')[0].text
  total_string = total_string.replace(',', '')
  total_page = math.ceil( int(total_string) / 20 )

  return total_page

getTotalPage(soup)

# %%
# 필요한 모듈 import
import requests as req
from bs4 import BeautifulSoup as bs
import math

# 경력 조회 함수
def getExp(soup) :
  exp_tags = soup.select('span.exp')
  exp_list = []

  for tag in exp_tags :
    exp_list.append(tag.text)

  return exp_list

# 학력 조회 함수
def getEdu(soup) :
  edu_tags = soup.select('span.edu')
  edu_list = []

  for tag in edu_tags :
    edu_list.append(tag.text)

  return edu_list

# 전체 페이지 조회 함수
def getTotalPage(soup):
  total_string = soup.select('.dev_tot')[0].text
  total_string = total_string.replace(',', '')
  total_page = math.ceil( int(total_string) / 20 )

  return total_page

# 기타 준비물
base_url = 'https://www.jobkorea.co.kr/Search/?stext=%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EB%B6%84%EC%84%9D&focusTab=&focusGno=43641436&tabType=recruit&Page_No='

page_no = 1

url = f'{base_url}{page_no}'
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}


# %%

# 요청 보내기
resp = req.get(url, headers=headers)
html = resp.text

soup = bs(html, 'html.parser')

# 전체 페이지 수 가져오기
total_page = getTotalPage(soup)
# total_page

# 전체 페이지 크롤링

# 전체 페이지 데이터를 담을 리스트 생성
edu_results = []
exp_results = []

# for page in range(total_page): 
for page in range(10) :
  url = f'{base_url}{page_no}'

  resp = req.get(url, headers=headers)
  html = resp.text

  soup = bs(html, 'html.parser')
  edu_list = getEdu(soup)
  exp_list = getExp(soup)

  edu_results += edu_list
  exp_results += exp_list
  page_no += 1


# %%
edu_results
len(edu_results)

len(exp_results)

# %%
import pandas as pd

# 요구 학력을 시리즈 객체로 변환
s_edu = pd.Series(edu_results)

# 요구 경력을 시리즈 객체로 변환
s_exp = pd.Series(exp_results)

# 시리즈 객체가 지원하는 value_counts() 를 사용하여
# 각 항목이 몇 번 등장했는지 구한다.
count_edu = s_edu.value_counts()

count_exp = s_exp.value_counts()

type(count_exp) # ** 결과는 시리즈 객체이다.

# %%
# 요구 학력 시리즈 객체를 데이터 프레임으로 변경
# reset_index()는 기존의 인덱스를 하나의 칼럼으로 변경하여 df으로 반환한다.
df_edu = count_edu.reset_index()

# 변환된 데이터 프레임의 칼럼명을 수정한다.
df_edu.columns = ['요구 학력', '집계']

df_edu

# 요구 경력
df_exp = count_exp.reset_index()

df_exp.columns = ['요구 경력', '집계']

df_exp

# df 객체를 csv로 저장한다.
df_exp.to_csv('exp.csv', index=False)
df_edu.to_csv('edu.csv', index=False)

# %%
import matplotlib.pyplot as plt

df_edu = pd.read_csv('edu.csv')
df_edu

df_exp = pd.read_csv('exp.csv')
df_exp

# 정렬하기
# ignore_index=True : 기존 인덱스를 무시하고 새로운 인덱스 부여
# inplace=True : 원본 데이터를 수정
df_exp.sort_values(by='요구 경력', ignore_index=True, inplace=True)


df_edu = pd.read_csv('edu.csv')
df_edu.sort_values(by='요구 학력', ignore_index=True, inplace=True)



# %%
# matplotlib 은 기본적으로 한글을 못 읽는다.
# df_exp.plot(kind='bar', x='요구 경력', y='집계')


# 한글 폰트 적용하기
from matplotlib import font_manager, rc
font_path = 'C:/Windows/Fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name)

df_exp.plot(kind='bar', x='요구 경력', y='집계')

plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# %%
# figure() : figure를 생성한다.(큰 도화지를 만든다.)
# figsize=(30,7) : 도화지의 크기를 설정
figure =plt.figure(figsize=(30,7))

# add_subplot(행, 열, 순서) : 서브 플롯을 추가한다.(큰 도화지에 그래프가 들어갈 작은 공간을 추가한다.)
# (1,2,1) : 1행 2열 중에 1번째 공간
ax1 = figure.add_subplot(1,2,1)
ax2 = figure.add_subplot(1,2,2)

df_exp.plot(kind='bar', x='요구 경력', y='집계', ax=ax1)
df_edu.plot(kind='bar', x='요구 학력', y='집계', ax=ax2)

ax1.tick_params(axis='x', rotation=0)
ax2.tick_params(axis='x', rotation=0)

# 타이틀 설정
ax1.set_title('데이터 분석가 요구 경력')

plt.savefig('my_graph.png')

plt.show()


# %%
# 원형 그래프로 시각화

fig = plt.figure(figsize=(20,20))

ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

# y : y축 설정
# lables : 각 파이에 들어갈 데이터 라벨을 지정
# autopct : 원형 차트의 조각에 백분율을 어떻게 표시할지 결정
# %.1f%% : %.1f (소수점 한 자리로 표시), %% (%문자열을 끝에 붙임)
df_exp.plot(kind='pie', y='집계', labels=df_exp['요구 경력'], autopct='%.1f%%' , ax=ax1)

df_edu.plot(kind='pie', y='집계', labels=df_edu['요구 학력'], autopct='%.1f%%' , ax=ax2, 
            explode=[0,0.1,0,0,0,0])

# df_exp
plt.savefig('pie_graph.png')

plt.show()


from wordcloud import WordCloud

# 한글 폰트 적용하기
from matplotlib import font_manager, rc
font_path = 'C:/Windows/Fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name)

test='가 나 다 라 가 가 나 가 다'

wordcloud_test = WordCloud(font_path = font_path,
          background_color='white').generate(test)

plt.figure(figsize=(8,8))

plt.imshow(wordcloud_test)

# x축, y축을 표시하지 않는다.
plt.axis('off')

plt.show()

# %%
# 워드 클라우드는 분석대상이 문자열 1개이다.
# 문자열은 데이터들을 띄어쓰기로 구분하여 저장되어 있어야한다.
# 중복되는 단어가 많을수록 해당 단어가 크게 표시된다.

# 리스트
exp_results
edu_results

# ' '.join(리스트) : 리스트의 각 요소들을 하나의 문자열로 만들어준다.
#                   이때 각 요소는 ' ' 을 구분자로 사용한다.
exp_str = ' '.join(exp_results)
edu_str = ' '.join(edu_results)

exp_str

wordcloud = WordCloud(font_path=font_path, background_color='white').generate(exp_str)

plt.figure(figsize=(8,8))
plt.imshow(wordcloud)
plt.axis('off')
plt.savefig('wordcloud.png')
plt.show()





# %%
