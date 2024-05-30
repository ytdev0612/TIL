```python
# 시각화
import matplotlib.pyplot as plt
import numpy as np
```


```python
plt.title("Plot")
plt.plot([1, 4, 9, 16]) # y축
plt.show()
```


    
![png](output_1_0.png)
    



```python
plt.title("x ticks")
plt.plot([10, 20, 30, 40], [1, 4, 9, 16])
plt.show()
```


    
![png](output_2_0.png)
    



```python
# 한글깨짐 방지
import matplotlib
from matplotlib import font_manager, rc
import platform
if platform.system()=="Windows":
    font_name=font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
    rc('font', family=font_name)
matplotlib.rcParams['axes.unicode_minus']=False

import warnings
warnings.filterwarnings("ignore")
```


```python
plt.title('한글 제목')
plt.plot([10, 20, 30, 40], [1, 4, 9, 16])
plt.xlabel("엑스축 라벨")
plt.ylabel("와이축 라벨")
plt.show()
```


    
![png](output_4_0.png)
    



```python
plt.title("'rs--' 스타일의 plot ")
plt.plot([10, 20, 30, 40], [1, 4, 9, 16], 'rs--')
plt.show()
```


    
![png](output_5_0.png)
    



```python
plt.plot([10, 20, 30, 40], [1, 4, 9, 16], c="b",
         lw=5, ls="--", marker="o", ms=15, mec="g", mew=5, mfc="r")
# 선 색상 : c, : 선의 굵기 : lw, 선의 스타일 : ls, 
# 마커중심 : marker, 마커사이즈 : ms, 마커선의 색상 : mec, 마커 선의 굵기 : mew, 마커 내부 색상 : mfc
plt.title("스타일 적용 예")
plt.show()
```


    
![png](output_6_0.png)
    



```python
plt.title("x축, y축의 범위 설정")
plt.plot([10, 20, 30, 40], [1, 4, 9, 16],
         c="b", lw=5, ls="--", marker="o", ms=15, mec="g", mew=5, mfc="r")
plt.xlim(0, 50)
plt.ylim(-10, 30)
plt.show()
```


    
![png](output_7_0.png)
    



```python
X = np.linspace(-np.pi, np.pi, 256)
C = np.cos(X)
plt.title("x축과 y축의 tick label 설정")
plt.plot(X, C)
plt.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi])
plt.yticks([-1, 0, +1])
plt.show()
```


    
![png](output_8_0.png)
    



```python
t = np.arange(0., 5., 0.2)
plt.title("라인 플롯에서 여러개의 선 그리기")
plt.plot(t, t, 'r--', t, 0.5 * t**2, 'bs:', t, 0.2 * t**3, 'g^-')
plt.show()
```


    
![png](output_9_0.png)
    



```python
plt.title("복수의 plot 명령을 한 그림에서 표현")
plt.plot([1, 4, 9, 16],
         c="b", lw=5, ls="--", marker="o", ms=15, mec="g", mew=5, mfc="r")
# plt.hold(True)   # <- 1,5 버전에서는 이 코드가 필요하다.
plt.plot([9, 16, 4, 1],
         c="k", lw=3, ls=":", marker="s", ms=10, mec="m", mew=5, mfc="c")
# plt.hold(False)  # <- 1,5 버전에서는 이 코드가 필요하다.
plt.show()
```


    
![png](output_10_0.png)
    



```python
X = np.linspace(-np.pi, np.pi, 256)
C, S = np.cos(X), np.sin(X)
plt.title("legend를 표시한 플롯")
plt.plot(X, C, ls="--", label="cosine")
plt.plot(X, S, ls=":", label="sine")
plt.legend(loc=2)
plt.show()
```


    
![png](output_11_0.png)
    



```python
X = np.linspace(-np.pi, np.pi, 256)
C, S = np.cos(X), np.sin(X)
plt.plot(X, C, label="cosine")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.title("Cosine Plot")
plt.show()
```


    
![png](output_12_0.png)
    



```python
# figure 객체 : 1개 이상의 axes 객체로 구성
# axes 객체 : axis의 복수형, 축들
# axis 객체 : 축(x축, y축...)
```


```python
np.random.seed(0)
f1 = plt.figure(figsize=(10, 2))
plt.title("figure size : (10, 2)")
plt.plot(np.random.randn(100))
plt.show()
```


    
![png](output_14_0.png)
    



```python
# subplot(2, 1, 1) # 2행, 1열 위아래로 나눔 subplot(1,2,1) 1행, 2열 좌우로 나눔
# 여기에서 윗부분에 그릴 플롯 명령 실행
# subplot(2, 1, 2) # 
# 여기에서 아랫부분에 그릴 플롯 명령 실행
```


```python
x1 = np.linspace(0.0, 5.0)
x2 = np.linspace(0.0, 2.0)
y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
y2 = np.cos(2 * np.pi * x2)

ax1 = plt.subplot(1,2,1)
plt.plot(x1, y1, 'yo-')
plt.title('A tale of 2 subplots')
plt.ylabel('Damped oscillation')

ax2 = plt.subplot(1,2,2)
plt.plot(x2, y2, 'r.-')
plt.xlabel('time (s)')
plt.ylabel('Undamped')

plt.tight_layout()
plt.show()
```


    
![png](output_16_0.png)
    



```python
fig, axes = plt.subplots(2, 2)

np.random.seed(0)
axes[0, 0].plot(np.random.rand(5))
axes[0, 0].set_title("axes 1")
axes[0, 1].plot(np.random.rand(5))
axes[0, 1].set_title("axes 2")
axes[1, 0].plot(np.random.rand(5))
axes[1, 0].set_title("axes 3")
axes[1, 1].plot(np.random.rand(5))
axes[1, 1].set_title("axes 4")

plt.tight_layout()
plt.show()
```


    
![png](output_17_0.png)
    



```python
np.random.seed(0)

plt.subplot(221)
plt.plot(np.random.rand(5))
plt.title("axes 1")

plt.subplot(222)
plt.plot(np.random.rand(5))
plt.title("axes 2")

plt.subplot(223)
plt.plot(np.random.rand(5))
plt.title("axes 3")

plt.subplot(224)
plt.plot(np.random.rand(5))
plt.title("axes 4")

plt.tight_layout()
plt.show()
```


    
![png](output_18_0.png)
    



```python
import matplotlib as mpl
import matplotlib.pylab as plt

y = [2, 3, 1]
x = np.arange(len(y))
xlabel = ['가', '나', '다']
plt.title("Bar Chart")
plt.bar(x, y)
plt.xticks(x, xlabel)
plt.yticks(sorted(y))
plt.xlabel("가나다")
plt.ylabel("빈도 수")
plt.show()
```


    
![png](output_19_0.png)
    



```python
np.random.seed(0)

people = ['몽룡', '춘향', '방자', '향단']
y_pos = np.arange(len(people))
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))

plt.title("Barh Chart")
plt.barh(y_pos, performance, xerr=error, alpha=0.4) # alpha : 투명도
plt.yticks(y_pos, people)
plt.xlabel('x 라벨')
plt.show()
```


    
![png](output_20_0.png)
    



```python
x = np.linspace(0.1, 2 * np.pi, 10)
plt.title("Stem Plot")
plt.stem(x, np.cos(x), '-.')
plt.show()
```


    
![png](output_21_0.png)
    



```python
labels = ['개구리', '돼지', '개', '통나무']
sizes = [15, 30, 45, 10]
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
explode = (0, 0.1, 0, 0)
plt.title("Pie Chart")
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.show()
```


    
![png](output_22_0.png)
    



```python
np.random.seed(0)
x = np.random.randn(1000)
plt.title("Histogram")
arrays, bins, patches = plt.hist(x, bins=10)
plt.show()
```


    
![png](output_23_0.png)
    



```python
arrays
```




    array([  9.,  20.,  70., 146., 217., 239., 160.,  86.,  38.,  15.])




```python
bins
```




    array([-3.04614305, -2.46559324, -1.88504342, -1.3044936 , -0.72394379,
           -0.14339397,  0.43715585,  1.01770566,  1.59825548,  2.1788053 ,
            2.75935511])




```python
np.random.seed(0)
X = np.random.normal(0, 1, 100)
Y = np.random.normal(0, 1, 100)
plt.title("Scatter Plot")
plt.scatter(X, Y)
plt.show()
```


    
![png](output_26_0.png)
    



```python
N = 30
np.random.seed(0)
x = np.random.rand(N)
y1 = np.random.rand(N)
y2 = np.random.rand(N)
y3 = np.pi * (15 * np.random.rand(N))**2
plt.title("Bubble Chart")
plt.scatter(x, y1, c=y2, s=y3)
plt.show()
```


    
![png](output_27_0.png)
    



```python
from sklearn.datasets import load_digits
digits = load_digits()
X = digits.images[3]
X
```




    array([[ 0.,  0.,  7., 15., 13.,  1.,  0.,  0.],
           [ 0.,  8., 13.,  6., 15.,  4.,  0.,  0.],
           [ 0.,  2.,  1., 13., 13.,  0.,  0.,  0.],
           [ 0.,  0.,  2., 15., 11.,  1.,  0.,  0.],
           [ 0.,  0.,  0.,  1., 12., 12.,  1.,  0.],
           [ 0.,  0.,  0.,  0.,  1., 10.,  8.,  0.],
           [ 0.,  0.,  8.,  4.,  5., 14.,  9.,  0.],
           [ 0.,  0.,  7., 13., 13.,  9.,  0.,  0.]])




```python
plt.title("mnist digits; 0")
plt.imshow(X, interpolation='nearest', cmap=plt.cm.bone_r)
plt.xticks([])
plt.yticks([])
plt.grid(False)
plt.subplots_adjust(left=0.35, right=0.65, bottom=0.35, top=0.65)
plt.show()
```


    
![png](output_29_0.png)
    



```python
import seaborn as sns
```


```python
iris = sns.load_dataset("iris")    # 붓꽃 데이터
titanic = sns.load_dataset("titanic")    # 타이타닉호 데이터
tips = sns.load_dataset("tips")    # 팁 데이터
flights = sns.load_dataset("flights")    # 여객운송 데이터
```


```python
x = iris.petal_length.values

sns.rugplot(x)
plt.title("Iris 데이터 중, 꽃잎의 길이에 대한 Rug Plot ")
plt.show()
```


    
![png](output_32_0.png)
    



```python
sns.kdeplot(x)
plt.title("Iris 데이터 중, 꽃잎의 길이에 대한 Kernel Density Plot")
plt.show()
```


    
![png](output_33_0.png)
    



```python
sns.distplot(x, kde=True, rug=True)
plt.title("Iris 데이터 중, 꽃잎의 길이에 대한 Dist Plot")
plt.show()
```


    
![png](output_34_0.png)
    



```python
sns.countplot(x="class", data=titanic)
plt.title("타이타닉호의 각 클래스별, 승객 수")
plt.show()
```


    
![png](output_35_0.png)
    



```python
sns.countplot(x="day", data=tips)
plt.title("요일별 팁을 준 횟수")
plt.show()
```


    
![png](output_36_0.png)
    



```python
sns.jointplot(x="sepal_length", y="sepal_width", data=iris)
plt.suptitle("꽃받침의 길이와 넓이의 Joint Plot", y=1.02)
plt.show()
```


    
![png](output_37_0.png)
    



```python
sns.jointplot(x="sepal_length", y="sepal_width", data=iris, kind="kde")
plt.suptitle("꽃받침의 길이와 넓이의 Joint Plot 과 Kernel Density Plot", y=1.02)
plt.show()
```


    
![png](output_38_0.png)
    



```python
sns.pairplot(iris)
plt.title("Iris Data의 Pair Plot")
plt.show()
```


    
![png](output_39_0.png)
    



```python
sns.pairplot(iris, hue="species", markers=["o", "s", "D"])
plt.title("Iris Pair Plot, Hue로 꽃의 종을 시각화")
plt.show()
```


    
![png](output_40_0.png)
    



```python
titanic_size = titanic.pivot_table(
    index="class", columns="sex", aggfunc="size")
titanic_size
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>sex</th>
      <th>female</th>
      <th>male</th>
    </tr>
    <tr>
      <th>class</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>First</th>
      <td>94</td>
      <td>122</td>
    </tr>
    <tr>
      <th>Second</th>
      <td>76</td>
      <td>108</td>
    </tr>
    <tr>
      <th>Third</th>
      <td>144</td>
      <td>347</td>
    </tr>
  </tbody>
</table>
</div>




```python
sns.heatmap(titanic_size, cmap=sns.light_palette(
    "gray", as_cmap=True), annot=True, fmt="d")
plt.title("Heatmap")
plt.show()
```


    
![png](output_42_0.png)
    



```python
flights_passengers = flights.pivot(index="month", columns="year", values="passengers")
plt.title("연도, 월 별 승객수에 대한 Heatmap")
sns.heatmap(flights_passengers, annot=True, fmt="d", linewidths=1)
plt.show()
```


    
![png](output_43_0.png)
    



```python

```
