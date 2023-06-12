#!/usr/bin/env python
# coding: utf-8

# In[3]:


import seaborn as sns


# In[4]:


var = ['a', 'a', 'b', 'b', 'b', 'c']
var


# In[5]:


sns.countplot(x = var)


# In[6]:


df = sns.load_dataset('titanic')
df


# In[7]:


sns.countplot(data = df, x = 'sex')


# In[8]:


sns.countplot(data = df, x = 'sex', hue = 'alive')


# In[9]:


sns.countplot(data = df, y = 'class', hue = 'sex')


# In[10]:


pip install pydataset


# In[11]:


import pydataset


# In[12]:


pydataset.data()


# In[13]:


df = pydataset.data('mtcars')
df


# In[14]:


score = [80, 60, 70, 50 , 90]
print(score)
sum_score = sum(score)
print(sum_score)


# In[15]:


pip install pandas


# In[16]:


import pandas as pd


# In[17]:


df = pd.DataFrame({"name" : ["김지훈", "이유진", "박동현", "김민지"],
                  "english": [90, 80, 60, 70],
                  "math" : [50, 60, 100, 20]})
df


# In[18]:


df['english']


# In[19]:


sum(df['english'])


# In[20]:


sum(df['english']) / 4


# In[21]:


df2 = pd.DataFrame({'product' : ['사과', '딸기', '수박'],
                   'price' : [1800, 1500, 3000],
                   'count' : [24, 38, 13]})
df2


# In[22]:


print(sum(df2['price']))
print(sum(df2['price']) / 3)


# In[23]:


df_exam = pd.read_excel('excel_exam.xlsx')
df_exam


# In[24]:


# 수학 점수 평균 구하기
print(sum(df_exam['math']) / 20)
print(sum(df_exam['math']) / len(df_exam))


# In[25]:


# 영어 점수 평균 구하기
print(sum(df_exam['english']) / 20)
print(sum(df_exam['english']) / len(df_exam))


# In[26]:


# 과학 점수 평균 구하기
print(sum(df_exam['science']) / 20)
print(sum(df_exam['science']) / len(df_exam))


# In[27]:


df_exam_novar = pd.read_excel('excel_exam_novar.xlsx')
df_exam_novar


# In[28]:


df_exam_novar = pd.read_excel('excel_exam_novar.xlsx', header = None)
df_exam_novar


# In[29]:


df_csv = pd.read_csv('exam.csv')
df_csv


# In[30]:


# 데이터프레임을 csv 파일로 저장하기
df_midterm = pd.DataFrame({'english' : [90, 80, 60, 70],
                          'math' : [50, 60, 100, 20],
                          'nclass' : [1, 1, 2, 2]})
df_midterm
df_midterm.to_csv("output_newdata.csv")


# In[31]:


import pandas as pd


# In[32]:


exam = pd.read_csv('exam.csv')


# In[33]:


exam.head()


# In[34]:


exam.head(8)


# In[35]:


exam.tail()


# In[36]:


exam.tail(10)


# In[37]:


exam.shape


# In[38]:


exam.info()
# <class 'pandas.core.frame.DataFrame'> : 해당 데이터가 pandas로 만든 데이터프레임이다.
# RangeIndex: 20 entries, 0 to 19 : 20개의 행으로 이루어져있으며, 행 번호는 0 ~ 19이다.
# Data columns (total 5 columns) : exam의 변수는 5개로 구성되어 있다.


# In[39]:


exam.describe(include = 'all')


# In[40]:


mpg = pd.read_csv('mpg.csv')
mpg


# In[41]:


mpg.head()


# In[42]:


mpg.tail()


# In[43]:


mpg.info()


# In[44]:


mpg.shape


# In[45]:


mpg.describe()


# In[46]:


mpg.describe(include = 'all')
# count = 빈도: 값의 개수
# unique = 고유값 빈도 : 중복을 제거한 범주의 개수
# top = 최빈값 : 개수가 가장 많은 값
# freq = 최빈값 빈도 : 개수가 가장 많은 값의 개수


# In[47]:


# 변수명 바꾸기
df_raw = pd.DataFrame({'var1' : [1, 2, 1],
                      'var2' : [2, 3, 2]})
df_raw


# In[48]:


# 데이터프레임 복사본 만들기
df_new = df_raw.copy()
df_new
# 복사본 만들기는 변수명.copy() 하면 된다


# In[49]:


df_new = df_new.rename(columns = {'var2' : 'v2'})
df_new


# In[50]:


df_raw


# In[51]:


mpg_new = mpg.copy()
mpg_new


# In[52]:


mpg_new = mpg_new.rename(columns = {"cty" : "city",
                          "hwy" : "highway"})
mpg_new


# In[53]:


# 파생변수 만들기: 기존의 변수를 변형해 만든 변수
df = pd.DataFrame({'var1' : [4, 3, 8],
                  'var2' : [2, 6, 1]})
df


# In[54]:


df['var_sum'] = df['var1'] + df['var2']
df


# In[55]:


df['var_mean'] = df['var_sum'] / 2
df


# In[56]:


mpg_new['total'] = (mpg_new['city'] + mpg_new['highway']) / 2
mpg_new


# In[57]:


sum(mpg_new['total']) / len(mpg_new)


# In[58]:


mpg_new['total'].mean()


# In[59]:


# 조건문을 활용해 파생변수 만들기
# 전체 자동차 중에서 연비 기준을 충족해 '고연비 합격 판정'을 받은 자동차가 몇 대?
# 연비가 기준값을 넘으면 합격, 넘지 못하면 불합격
mpg_new['total'].describe()


# In[60]:


mpg_new['total'].plot.hist()


# In[61]:


import numpy as np


# In[62]:


mpg_new['test'] = np.where(mpg_new['total'] >= 20,'pass', 'fail')
mpg_new


# In[63]:


mpg_new['test'].value_counts()


# In[64]:


# 막대 그래프로 빈도 표현하기
count_test= mpg_new['test'].value_counts()


# In[65]:


count_test.plot.bar()


# In[66]:


# 축 이름 회전하기
count_test.plot.bar(rot = 30)


# In[67]:


# 중첩 조건문 활용하기
mpg_new['grade'] = np.where(mpg_new['total'] >= 30, 'A', np.where(mpg_new['total'] >= 20, 'B', 'C'))
mpg_new.head(20)


# In[68]:


count_grade = mpg_new['grade'].value_counts()
count_grade


# In[69]:


count_grade.plot.bar(rot = 0)


# In[70]:


# 등급 빈도표 알파벳순 정렬
count_grade = mpg_new['grade'].value_counts().sort_index()
count_grade


# In[71]:


count_grade.plot.bar(rot = 0)


# In[72]:


mpg_new['size'] = np.where((mpg_new['category'] == 'compact')|
                           (mpg_new['category'] == 'subcompact')|
                           (mpg_new['category'] == '2seater'), 'small', 'large')
mpg_new


# In[73]:


mpg_new['size'] = np.where(mpg_new['category'].isin(['compact', 'subcompact','2seater']), 'small', 'large')
mpg_new


# In[74]:


import pandas as pd
midwest = pd.read_csv('midwest.csv')
midwest


# In[75]:


midwest.head()


# In[76]:


midwest.tail()


# In[77]:


midwest.shape


# In[78]:


midwest.info()


# In[79]:


midwest.describe()


# In[80]:


midwest.describe(include = 'all')


# In[81]:


midwest_new = midwest.copy()
midwest_new


# In[82]:


midwest_new = midwest.rename(columns = {'poptotal' : 'total',
                                     'popasian' : 'asian'})
midwest_new


# In[83]:


midwest_new['asian_ratio'] = (midwest_new['asian'] / midwest_new['total']) * 100
midwest_new


# In[84]:


ratio_hist = midwest_new['asian_ratio']
ratio_hist.plot.hist()


# In[85]:


import numpy as np


# In[86]:


midwest_new['avg_asian'] = np.where(midwest_new['asian_ratio'] > midwest_new['asian_ratio'].mean(), 'large', 'small')
midwest_new.head(15)


# In[87]:


midwest_new['avg_asian'].value_counts()


# In[88]:


midwest_new['avg_asian'].value_counts().plot.bar(rot = 0)


# In[89]:


# 자유자재로 데이터 가공하기
# 1. 데이터 전처리 : 원하는 형태로 데이터 가공하기
# 2. 조건에 맞는 데이터만 추출하기
import pandas as pd
exam = pd.read_csv('exam.csv')
exam


# In[90]:


exam.query('nclass == 1')


# In[91]:


exam.query('nclass == 2')


# In[92]:


exam.query('nclass != 1')


# In[93]:


# 수학 점수가 50점을 초과한 경우
exam.query('math > 50')


# In[94]:


# 수학 점수가 50점 미만인 경우
exam.query('math < 50')


# In[95]:


# 영어 점수가 50점 이상인 경우
exam.query('english >= 50')


# In[96]:


# 영어 점수가 80점 이하인 경우
exam.query('english <= 80')


# In[97]:


# 여러 조건을 충족하는 행 추출하기
exam.query('nclass == 1 & math >= 50')


# In[98]:


# 2반이면서 영어 점수가 80점 이상인 경우
exam.query('nclass == 2 & english >= 80')


# In[99]:


# 여러 조건 중 하나 이상을 충족하는 행 추출하기
# 수학 점수가 90점 이상이거나 영어 점수가 90점 이상인 경우
exam.query('math >= 90 | english >= 90')


# In[100]:


# 영어 점수가 90점 미만이거나 과학 점수가 50점 미만인 경우
exam.query('english < 90 | science < 50')


# In[101]:


# 목록에 해당하는 행 추출하기
# 1, 3, 5반에 해당하면 추출
exam.query('nclass == 1 | nclass == 3 | nclass == 5')


# In[102]:


# in을 사용하기
exam.query('nclass in [1, 3, 5]')


# In[103]:


# 추출한 행으로 데이터 만들기
# nclass가 1인 행을 추출해 nclass1에 할당
nclass1 = exam.query('nclass == 1')

# nclass가 2인 행을 추출해 nclass2에 할당
nclass2 = exam.query('nclass == 2')


# In[104]:


# 1반 수학 점수 평균 구하기
nclass1['math'].mean()


# In[105]:


# 2반 수학 점수 평균 구하기
nclass2['math'].mean()


# In[106]:


import pandas as pd
# 문자 변수를 이용해 조건에 맞는 행 추출하기
df= pd.DataFrame({'sex' : ['F', 'M', 'F', 'M'],
             'country' : ['Korea', 'China', 'Japan', 'USA']})
df


# In[107]:


# 전체 조건에 작은따옴표, 추출할 문자에 큰따옴표 사용
df.query('sex == "F" & country == "Korea"')


# In[108]:


# 전체 조건에 큰따옴표로 썼다면 추출 문자는 작은 따옴표를 사용
df.query("sex == 'M' & country == 'China'")


# In[109]:


# 외부 변수를 이용해 추출하기
var = 3
exam.query('nclass == @var')


# In[111]:


# 데이터프레임 출력 제한 설정하기
# 노트북은 데이터프레임이 60행을 넘기면 위아래 5행씩 10행만 출력하고 중간을 생략한다.
# 열은 20열을 넘기면 좌우 10열씩 20열만 출력하고 중간을 생략한다.
# 이때 set_option으로 출력 제한을 설정할 수 있다.
pd.set_option('display.max_rows', None)
# 이러한 옵션은 재실행 시 원상복귀되므로, 이를 방지하기 위해서는 reset_option을 설정하면 된다.
pd.rest_option('display.max_rows')


# In[112]:


import pandas as pd


# In[114]:


mpg = pd.read_csv('mpg.csv')
mpg.head()


# In[116]:


mpg.tail()


# In[117]:


mpg.info()


# In[118]:


mpg.shape


# In[119]:


mpg.describe(include = 'all')


# In[127]:


# 자동차 배기량에 따라 고속도로 연비가 얼마나 다른지 알아보려고 합니다.
# displ(배기량)이 4 이하인 자동차와 5이상인 자동차 중에서 어떤 자동차의 hwy(고속도로 연비) 평균이 더 높은지 알아보세요
displ_4 = mpg.query('displ <= 4')
displ_5 = mpg.query('displ >= 5')


# In[128]:


displ_4['hwy'].mean()


# In[129]:


displ_5['hwy'].mean()


# In[134]:


# 자동차 제조 회사에 따라 도시 연비가 어떻게 다른지 알아보려고 합니다.
# 'audi'와 'toyota' 중 어느 manufacturer(자동차 제조 회사)의 cty(도시 연비) 평균이 더 높은지 알아보세요.
audi = mpg.query('manufacturer == "audi"')
toyota = mpg.query('manufacturer == "toyota"')


# In[135]:


audi['cty'].mean()


# In[136]:


toyota['cty'].mean()


# In[139]:


#'chevrolet', 'ford', 'honda' 자동차의 고속도로 연비 평균을 알아보려고 합니다. 
# 세 회사의 데이터를 추출한 다음 hwy 전체 평균을 구해보세요
three = mpg.query('manufacturer in ["chevrolet", "ford", "honda"]')
three['hwy'].mean()

