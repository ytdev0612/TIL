## 주피터 노트북으로 진행
``python
'''
넘파이(배열)과 파이썬(리스트) 차이
배열 : 모든 자료형이 동일, 데이터의 개수를 변경할 수 없다
파이썬에서 배열을 기본적으로 제공하지 않으므로, 별도로 넘파이 패키지를 설치하여 배열을 사용

벡터 : 숫자를 원소로 갖는 리스트(배열), 행백터, 열벡터
행벡터 = x=[x1 x2 ... xn]
공간에서의 한 점
원점으로부터 떨어진 상대적위치

행렬 : 벡터를 원소로 갖는 2차원 배열
공간에서의 여러 점(데이터 모임)
행렬 곱셈을 통해 벡터를 다른 차원의 공간으로 이동할 수 있다
'''
```




    '\n넘파이(배열)과 파이썬(리스트) 차이\n배열 : 모든 자료형이 동일, 데이터의 개수를 변경할 수 없다\n파이썬에서 배열을 기본적으로 제공하지 않으므로, 별도로 넘파이 패키지를 설치하여 배열을 사용\n'



```python
plist
```

    Package                            Version
    ---------------------------------- --------------------
    alabaster                          0.7.12
    anaconda-client                    1.9.0
    anaconda-navigator                 2.1.1
    anaconda-project                   0.10.1
    anyio                              2.2.0
    appdirs                            1.4.4
    argh                               0.26.2
    argon2-cffi                        20.1.0
    arrow                              0.13.1
    asn1crypto                         1.4.0
    astroid                            2.6.6
    astropy                            4.3.1
    async-generator                    1.10
    atomicwrites                       1.4.0
    attrs                              23.2.0
    autopep8                           1.5.7
    Babel                              2.9.1
    backcall                           0.2.0
    backports.functools-lru-cache      1.6.4
    backports.shutil-get-terminal-size 1.0.0
    backports.tempfile                 1.0
    backports.weakref                  1.0.post1
    bcrypt                             3.2.0
    beautifulsoup4                     4.10.0
    binaryornot                        0.4.4
    bitarray                           2.3.0
    bkcharts                           0.2
    black                              19.10b0
    bleach                             4.0.0
    bokeh                              2.4.1
    boto                               2.49.0
    Bottleneck                         1.3.2
    brotlipy                           0.7.0
    cached-property                    1.5.2
    certifi                            2021.10.8
    cffi                               1.14.6
    chardet                            4.0.0
    charset-normalizer                 2.0.4
    click                              8.0.3
    cloudpickle                        2.0.0
    clyent                             1.2.2
    colorama                           0.4.4
    comtypes                           1.1.10
    conda                              4.10.3
    conda-build                        3.21.6
    conda-content-trust                0+unknown
    conda-pack                         0.6.0
    conda-package-handling             1.7.3
    conda-repo-cli                     1.0.4
    conda-token                        0.3.0
    conda-verify                       3.4.2
    contextlib2                        0.6.0.post1
    cookiecutter                       1.7.2
    cryptography                       3.4.8
    cycler                             0.10.0
    Cython                             0.29.24
    cytoolz                            0.11.0
    daal4py                            2021.3.0
    dask                               2021.10.0
    debugpy                            1.4.1
    decorator                          5.1.0
    defusedxml                         0.7.1
    diff-match-patch                   20200713
    distributed                        2021.10.0
    docutils                           0.17.1
    entrypoints                        0.3
    et-xmlfile                         1.1.0
    exceptiongroup                     1.2.0
    fastcache                          1.1.0
    filelock                           3.3.1
    flake8                             3.9.2
    Flask                              1.1.2
    fonttools                          4.25.0
    fsspec                             2021.10.1
    future                             0.18.2
    gevent                             21.8.0
    glob2                              0.7
    greenlet                           1.1.1
    h11                                0.14.0
    h5py                               3.2.1
    HeapDict                           1.0.1
    html5lib                           1.1
    idna                               3.2
    imagecodecs                        2021.8.26
    imageio                            2.9.0
    imagesize                          1.2.0
    importlib-metadata                 4.8.1
    inflection                         0.5.1
    iniconfig                          1.1.1
    intervaltree                       3.1.0
    ipykernel                          6.4.1
    ipython                            7.29.0
    ipython-genutils                   0.2.0
    ipywidgets                         7.6.5
    isort                              5.9.3
    itsdangerous                       2.0.1
    jdcal                              1.4.1
    jedi                               0.18.0
    Jinja2                             2.11.3
    jinja2-time                        0.2.0
    joblib                             1.1.0
    json5                              0.9.6
    jsonschema                         3.2.0
    jupyter                            1.0.0
    jupyter-client                     6.1.12
    jupyter-console                    6.4.0
    jupyter-core                       4.8.1
    jupyter-server                     1.4.1
    jupyterlab                         3.2.1
    jupyterlab-pygments                0.1.2
    jupyterlab-server                  2.8.2
    jupyterlab-widgets                 1.0.0
    keyring                            23.1.0
    kiwisolver                         1.3.1
    lazy-object-proxy                  1.6.0
    libarchive-c                       2.9
    llvmlite                           0.37.0
    locket                             0.2.1
    lxml                               4.6.3
    MarkupSafe                         1.1.1
    matplotlib                         3.4.3
    matplotlib-inline                  0.1.2
    mccabe                             0.6.1
    menuinst                           1.4.18
    mistune                            0.8.4
    mkl-fft                            1.3.1
    mkl-random                         1.2.2
    mkl-service                        2.4.0
    mock                               4.0.3
    more-itertools                     8.10.0
    mpmath                             1.2.1
    msgpack                            1.0.2
    multipledispatch                   0.6.0
    munkres                            1.1.4
    mypy-extensions                    0.4.3
    navigator-updater                  0.2.1
    nbclassic                          0.2.6
    nbclient                           0.5.3
    nbconvert                          6.1.0
    nbformat                           5.1.3
    nest-asyncio                       1.5.1
    networkx                           2.6.3
    nltk                               3.6.5
    nose                               1.3.7
    notebook                           6.4.5
    numba                              0.54.1
    numexpr                            2.7.3
    numpy                              1.20.3
    numpydoc                           1.1.0
    olefile                            0.46
    openpyxl                           3.0.9
    Note: you may need to restart the kernel to use updated packages.outcome                            1.3.0.post0
    
    packaging                          21.0
    pandas                             1.3.4
    pandocfilters                      1.4.3
    paramiko                           2.7.2
    parso                              0.8.2
    partd                              1.2.0
    path                               16.0.0
    pathlib2                           2.3.6
    pathspec                           0.7.0
    patsy                              0.5.2
    pep8                               1.7.1
    pexpect                            4.8.0
    pickleshare                        0.7.5
    Pillow                             8.4.0
    pip                                21.2.4
    pkginfo                            1.7.1
    pluggy                             0.13.1
    ply                                3.11
    poyo                               0.5.0
    prometheus-client                  0.11.0
    prompt-toolkit                     3.0.20
    psutil                             5.8.0
    ptyprocess                         0.7.0
    py                                 1.10.0
    pycodestyle                        2.7.0
    pycosat                            0.6.3
    pycparser                          2.20
    pycurl                             7.44.1
    pydocstyle                         6.1.1
    pyerfa                             2.0.0
    pyflakes                           2.3.1
    Pygments                           2.10.0
    PyJWT                              2.1.0
    pylint                             2.9.6
    pyls-spyder                        0.4.0
    PyNaCl                             1.4.0
    pyodbc                             4.0.0-unsupported
    pyOpenSSL                          21.0.0
    pyparsing                          3.0.4
    pyreadline                         2.1
    pyrsistent                         0.18.0
    PySocks                            1.7.1
    pytest                             6.2.4
    python-dateutil                    2.8.2
    python-lsp-black                   1.0.0
    python-lsp-jsonrpc                 1.0.0
    python-lsp-server                  1.2.4
    python-slugify                     5.0.2
    pytz                               2021.3
    PyWavelets                         1.1.1
    pywin32                            228
    pywin32-ctypes                     0.2.0
    pywinpty                           0.5.7
    PyYAML                             6.0
    pyzmq                              22.2.1
    QDarkStyle                         3.0.2
    qstylizer                          0.1.10
    QtAwesome                          1.0.2
    qtconsole                          5.1.1
    QtPy                               1.10.0
    regex                              2021.8.3
    requests                           2.26.0
    rope                               0.19.0
    Rtree                              0.9.7
    ruamel-yaml-conda                  0.15.100
    scikit-image                       0.18.3
    scikit-learn                       0.24.2
    scikit-learn-intelex               2021.20210714.120553
    scipy                              1.7.1
    seaborn                            0.11.2
    selenium                           4.18.1
    Send2Trash                         1.8.0
    setuptools                         58.0.4
    simplegeneric                      0.8.1
    singledispatch                     3.7.0
    sip                                4.19.13
    six                                1.16.0
    sniffio                            1.3.1
    snowballstemmer                    2.1.0
    sortedcollections                  2.1.0
    sortedcontainers                   2.4.0
    soupsieve                          2.2.1
    Sphinx                             4.2.0
    sphinxcontrib-applehelp            1.0.2
    sphinxcontrib-devhelp              1.0.2
    sphinxcontrib-htmlhelp             2.0.0
    sphinxcontrib-jsmath               1.0.1
    sphinxcontrib-qthelp               1.0.3
    sphinxcontrib-serializinghtml      1.1.5
    sphinxcontrib-websupport           1.2.4
    spyder                             5.1.5
    spyder-kernels                     2.1.3
    SQLAlchemy                         1.4.22
    statsmodels                        0.12.2
    sympy                              1.9
    tables                             3.6.1
    TBB                                0.2
    tblib                              1.7.0
    terminado                          0.9.4
    testpath                           0.5.0
    text-unidecode                     1.3
    textdistance                       4.2.1
    threadpoolctl                      2.2.0
    three-merge                        0.1.1
    tifffile                           2021.7.2
    tinycss                            0.4
    toml                               0.10.2
    toolz                              0.11.1
    tornado                            6.1
    tqdm                               4.62.3
    traitlets                          5.1.0
    trio                               0.25.0
    trio-websocket                     0.11.1
    typed-ast                          1.4.3
    typing_extensions                  4.10.0
    ujson                              4.0.2
    unicodecsv                         0.14.1
    Unidecode                          1.2.0
    urllib3                            1.26.7
    watchdog                           2.1.3
    wcwidth                            0.2.5
    webencodings                       0.5.1
    Werkzeug                           2.0.2
    wheel                              0.37.0
    whichcraft                         0.6.1
    widgetsnbextension                 3.5.1
    win-inet-pton                      1.1.0
    win-unicode-console                0.5
    wincertstore                       0.2
    wrapt                              1.12.1
    wsproto                            1.2.0
    xlrd                               2.0.1
    XlsxWriter                         3.0.1
    xlwings                            0.24.9
    xlwt                               1.3.0
    xmltodict                          0.12.0
    yapf                               0.31.0
    zict                               2.0.0
    zipp                               3.6.0
    zope.event                         4.5.0
    zope.interface                     5.4.0
    


```python
x = [10, 20, 30]
x
```




    [10, 20, 30]




```python
import numpy as np
```


```python
array_x = np.array(x)
array_x # 1차원 배열(벡터)
```




    array([10, 20, 30])




```python
type(array_x)
```




    numpy.ndarray




```python
사과:1000, 딸기:2000, 배:2000, 파인애플:5000, 바나나:3000
5/1 사과:5, 딸기:2, 배:0, 파인애플:0, 바나나:3
5/2 사과:1, 딸기:3, 배:2, 파인애플:3, 바나나:0

5차원 벡터 : 5차원 공간에 표현된 한 점                    
[5 2 0 0 3]
[1 3 2 3 0]
...
[...]

덧셈, 뺄셈
[5 2 0 0 3] + [1 3 2 3 0] = [6 5 2 3 3]

```


```python
import time
s = time.time()
data = list(range(1, 10000000))
ans = []
# data

for d in data:
    ans.append(d*2)
ans

e = time.time()
print(e-s)
```

    1.1464414596557617
    


```python
arr_data = np.array(data)
arr_data
```




    array([      1,       2,       3, ..., 9999997, 9999998, 9999999])




```python
s= time.time()
ans2 = 2*arr_data # 벡터화 연산
e= time.time()
print(e-s)
```

    0.007102489471435547
    


```python
ans2
```




    array([       2,        4,        6, ..., 19999994, 19999996, 19999998])




```python
x=[1,2]
y=[3,4]
```


```python
x+y # 파이썬 리스트
```




    [1, 2, 3, 4]




```python
np.array(x) + np.array(y) # 요소간 덧셈
```




    array([4, 6])




```python
# 1~100까지 수 중에서 짝수를 even, 홀수를 odd에 저장한 다음,
# 같은 위치의 요소끼리 비교하여 큰 값을 출력하시오
odd =[i for i in range(1, 101, 2)]
# odd
even = [i for i in range(2, 101, 2)]
# even
res = [even[i] if even[i] > odd[i] else odd[i] for i in range(len(even))]
# res
```


```python
odd =[i for i in range(1, 101, 2)]
even = [i for i in range(2, 101, 2)]
a_even = np.array(even)
a_odd = np.array(odd)
```


```python
a_even + a_odd
a_even>50
(a_even >30) & (a_even % 5 == 0)
a_even # 2,4,...100
a_odd # 1,3,...99
a_even[a_even>a_odd] # True에 해당하는 값 출력
```




    array([  2,   4,   6,   8,  10,  12,  14,  16,  18,  20,  22,  24,  26,
            28,  30,  32,  34,  36,  38,  40,  42,  44,  46,  48,  50,  52,
            54,  56,  58,  60,  62,  64,  66,  68,  70,  72,  74,  76,  78,
            80,  82,  84,  86,  88,  90,  92,  94,  96,  98, 100])




```python
np.__version__
```




    '1.20.3'




```python
np.array((10,20,30))
```




    array([10, 20, 30])




```python
# 0차원 배열 = 스칼라 = 배열의 각 요소 값
arr = np.array(10)
arr
```




    array(10)




```python
# 1차원 배열 = 0차원 배열을 요소로 갖는 배열
arr = np.array([10, 20, 30])
arr
```




    array([10, 20, 30])




```python
# 2차원 배열 = 1차원 배열을 요소로 갖는 배열 = 행렬
arr = np.array([[10, 20, 30], [40, 50, 60]])
arr # 2행 3열
# len(arr) # 행
# len(arr[0]) # 열
```




    array([[10, 20, 30],
           [40, 50, 60]])




```python
# 3차원 배열 = 2차원 배열을 요소로 갖는 배열, 다차원 배열
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
arr
arr.ndim
```




    3




```python
len(arr) # 깊이
len(arr[0]) # 행, [[1,2,3],[4,5,6]]
len(arr[0][0]) # 열, [1,2,3]
```




    3




```python
# 1~24 요소값으로 2*3*4 배열생성
arr=np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]],[[13,14,15,16], [17,18,19,20], [21,22,23,24]]])
arr
# arr = np.array([ [ [n for n in range(1, 5)], [n for n in range(5, 9)], [n for n in range(9, 13)] ], [ [n for n in range(13, 17)], [n for n in range(17, 21)], [n for n in range(21, 25)] ] ])
# arr
```




    array([[[ 1,  2,  3,  4],
            [ 5,  6,  7,  8],
            [ 9, 10, 11, 12]],
    
           [[13, 14, 15, 16],
            [17, 18, 19, 20],
            [21, 22, 23, 24]]])




```python
# np.array([     ,      ])
# np.array([ [    ], [    ]])
# np.array([ [[ ], [ ], [ ] ], [ [[ ], [ ], [ ] ]])
# np.array([[[ , , , ], [ , , , ], [ , , , ]], 
#          [[ , ,  , ], [ , , , ], [ , , , ]]])
```


```python
arr + 1
```




    array([[[ 2,  3,  4,  5],
            [ 6,  7,  8,  9],
            [10, 11, 12, 13]],
    
           [[14, 15, 16, 17],
            [18, 19, 20, 21],
            [22, 23, 24, 25]]])




```python
# 1~24 요소값으로 2*3*4 배열생성
arr = np.array(list(range(1, 25)))
arr
```




    array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17,
           18, 19, 20, 21, 22, 23, 24])




```python
arr_re = arr.reshape(2,3,4)
arr_re
```




    array([[[ 1,  2,  3,  4],
            [ 5,  6,  7,  8],
            [ 9, 10, 11, 12]],
    
           [[13, 14, 15, 16],
            [17, 18, 19, 20],
            [21, 22, 23, 24]]])




```python
arr_re.ndim # .ndim : 넘파이 배열에서 몇 차원인지 나타내는 속성
arr_re.shape 
```




    (2, 3, 4)




```python
arr = np.array([1,2,3,4])
arr
```




    array([1, 2, 3, 4])




```python
arr[0]
arr[2]+arr[3]
arr[-1]
```




    4




```python
# 2차원 배열 생성(2행 5열), 11~20 까지 요소값 저장
arr = np.array(list(range(11, 21))).reshape(2, 5)
arr
```




    array([[11, 12, 13, 14, 15],
           [16, 17, 18, 19, 20]])




```python
arr[1][3]
arr[1, 3]
```




    19




```python
arr[-1]
arr[-2]
arr[-1][-2]
arr[-1, -2]
```




    19




```python
# 1~12까지 요소로 초기화
# 3차원 배열(2,2,3)
arr = np.array(list(range(1, 13))).reshape(2,2,3)
arr
```




    array([[[ 1,  2,  3],
            [ 4,  5,  6]],
    
           [[ 7,  8,  9],
            [10, 11, 12]]])




```python
arr[0][1][-1]
arr[0,1,2]
```




    6




```python
# array indexing
# array slicing
# [시작:끝]
# [시작:끝:간격]
```


```python
arr = np.array(list(range(1,8)))
arr
```




    array([1, 2, 3, 4, 5, 6, 7])




```python
arr[1]
arr[1:5] # 시작위치 포함, 끝 위치 불포함
arr[3:]
arr[:3]
```




    array([1, 2, 3])




```python
arr[-3:]
arr[-5:-2]
arr[:-3]
arr[1:5:2]
```




    array([2, 4])




```python
arr
```




    array([1, 2, 3, 4, 5, 6, 7])




```python
arr[:]
arr[::]
arr[::1] # [시작:끝:스텝]
```




    array([1, 2, 3, 4, 5, 6, 7])




```python
arr[::2]
```




    array([1, 3, 5, 7])




```python
arr=np.array(list(range(1,11))).reshape(2,5)
arr
```




    array([[ 1,  2,  3,  4,  5],
           [ 6,  7,  8,  9, 10]])




```python
arr[1]
```




    array([ 6,  7,  8,  9, 10])




```python
arr[1,1]
```




    7




```python
arr[1][1:4]
arr[1,1:4]
```




    array([7, 8, 9])




```python
arr=np.array(list(range(11,41))).reshape(6,5)
arr
```




    array([[11, 12, 13, 14, 15],
           [16, 17, 18, 19, 20],
           [21, 22, 23, 24, 25],
           [26, 27, 28, 29, 30],
           [31, 32, 33, 34, 35],
           [36, 37, 38, 39, 40]])




```python
arr[4,3]
```




    34




```python
arr[2,:3]
```




    array([21, 22, 23])




```python
# 17, 18, 19
# 22, 23, 24 출력

# arr[1,1:4]
# arr[2][1:4]
arr[1:3, 1:4] # [16,17,18,19,20], [21,22,23,24,25] -> 여기서 [1:4] 출력, arr[1:3][1:4] 는 논리적 오류
```




    array([[17, 18, 19],
           [22, 23, 24]])




```python
pip install -U finance-datareader
```

    Requirement already satisfied: finance-datareader in c:\anaconda3\lib\site-packages (0.9.90)
    Requirement already satisfied: requests>=2.3.0 in c:\anaconda3\lib\site-packages (from finance-datareader) (2.26.0)
    Requirement already satisfied: tqdm in c:\anaconda3\lib\site-packages (from finance-datareader) (4.62.3)
    Requirement already satisfied: pandas>=0.19.2 in c:\anaconda3\lib\site-packages (from finance-datareader) (1.3.4)
    Requirement already satisfied: lxml in c:\anaconda3\lib\site-packages (from finance-datareader) (4.6.3)
    Requirement already satisfied: requests-file in c:\anaconda3\lib\site-packages (from finance-datareader) (2.0.0)
    Requirement already satisfied: numpy>=1.17.3 in c:\anaconda3\lib\site-packages (from pandas>=0.19.2->finance-datareader) (1.20.3)
    Requirement already satisfied: python-dateutil>=2.7.3 in c:\anaconda3\lib\site-packages (from pandas>=0.19.2->finance-datareader) (2.8.2)
    Requirement already satisfied: pytz>=2017.3 in c:\anaconda3\lib\site-packages (from pandas>=0.19.2->finance-datareader) (2021.3)
    Requirement already satisfied: six>=1.5 in c:\anaconda3\lib\site-packages (from python-dateutil>=2.7.3->pandas>=0.19.2->finance-datareader) (1.16.0)
    Requirement already satisfied: certifi>=2017.4.17 in c:\anaconda3\lib\site-packages (from requests>=2.3.0->finance-datareader) (2021.10.8)
    Requirement already satisfied: idna<4,>=2.5 in c:\anaconda3\lib\site-packages (from requests>=2.3.0->finance-datareader) (3.2)
    Requirement already satisfied: charset-normalizer~=2.0.0 in c:\anaconda3\lib\site-packages (from requests>=2.3.0->finance-datareader) (2.0.4)
    Requirement already satisfied: urllib3<1.27,>=1.21.1 in c:\anaconda3\lib\site-packages (from requests>=2.3.0->finance-datareader) (1.26.7)
    Requirement already satisfied: colorama in c:\anaconda3\lib\site-packages (from tqdm->finance-datareader) (0.4.4)
    Note: you may need to restart the kernel to use updated packages.
    


```python
kakao_arr = np.loadtxt('kakao.csv', skiprows=1, dtype=np.float32, delimiter=',')
kakao_arr[:,2]
```




    array([57800., 56000., 57100., 57300., 56300., 56000., 55600., 56100.,
           56000., 55600., 56800., 57200., 57600., 57600., 56700., 56300.,
           56400., 56400., 56100., 56000., 56000., 57000., 57300., 56300.,
           56300., 56400., 56200., 55300., 53700., 53400., 52000., 51500.,
           50300., 50100., 49550., 48600., 49350., 48500., 48700., 48400.,
           49300., 49900., 48800., 48700., 49750., 49450., 50000., 50200.,
           51700., 51600., 52200., 51400., 50100., 50100., 49750., 49400.,
           48800., 46650., 47500., 49600., 50000., 51800., 52300., 52300.,
           51000., 51200., 51800., 52100., 51900., 50600., 50600., 49850.,
           49150., 48200., 48250., 48400., 48450., 48900., 47600., 47800.,
           48000., 48750., 48100., 47950., 48400., 48850., 48500., 48600.,
           48000., 47900., 48150., 47300., 47450., 48100., 48450., 47800.,
           47050., 45600., 44800., 44650., 43400., 43150., 41600., 40700.,
           40600., 41200., 41900., 42600., 43050., 42400., 42800., 41800.,
           40450., 38850., 37850., 37850., 38850., 37400., 37300., 37600.,
           37450., 37450., 37900., 38900., 42300., 42850., 43850., 43450.,
           45000., 44900., 45500., 46800., 46850., 47200., 47000., 48300.,
           48250., 49600., 50000., 49300., 49800., 50100., 50000., 49650.,
           49750., 50200., 50200., 50000., 50700., 51900., 51800., 50700.,
           52300., 54000., 53700., 53200., 53000., 52000., 52600., 52100.,
           52100., 53300., 54000., 56000., 55600., 55500., 55800., 58300.,
           58600., 59400., 59100., 59800., 59400., 56600., 55900., 57100.,
           55800., 56600., 56300., 54700., 55600., 55200., 53600., 52200.,
           51500., 53700., 54600., 53800., 53600., 53700., 54000., 53200.,
           56700., 58300., 58100., 57800., 58000., 57700., 56600., 57000.,
           56300., 55200., 53000., 52900., 51600., 51400., 52000., 53000.,
           52700., 54800., 54100., 54600., 53900., 52700., 51700., 52300.,
           52800., 53300., 53100., 53900., 53900., 54400., 53500., 53600.,
           51000., 51000., 49100., 48200., 48300., 48850., 47700., 47650.,
           46850., 46600., 46700., 46900., 47700., 48450., 47050., 47850.,
           47100., 47150., 47600., 48300., 48050., 49000.], dtype=float32)




```python
# 과제
```


```python
# 1. 넘파이를 사용하여 다음과 같은 행렬을 만든다.
# 10 20 30 40
# 50 60 70 80

arr = np.array(list(range(10,81,10))).reshape(2,4)
arr
```




    array([[10, 20, 30, 40],
           [50, 60, 70, 80]])




```python
# 2.다음 행렬과 같은 행렬이 있다.
m = np.array([[ 0,  1,  2,  3,  4],
            [ 5,  6,  7,  8,  9],
            [10, 11, 12, 13, 14]])
```


```python
# 이 행렬에서 값 7 을 인덱싱한다.
m[1,2]
# 이 행렬에서 값 14 을 인덱싱한다.
m[2][4]
# 이 행렬에서 배열 [6, 7] 을 슬라이싱한다.
m[1,1:3]
# 이 행렬에서 배열 [7, 12] 을 슬라이싱한다.
m[1:, 2]
# 이 행렬에서 배열 [[3, 4], [8, 9]] 을 슬라이싱한다.
m[:2, 3:5]

```




    array([[3, 4],
           [8, 9]])




```python
# 3. 값이 10에서 49를 원소로 가지고 있는 벡터 만들기
arr = np.array(list(range(10,50)))
arr
```




    array([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
           27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43,
           44, 45, 46, 47, 48, 49])




```python
# 4. 3번 배열의 원소를 뒤집어 출력
arr[::-1]
```




    array([49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33,
           32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16,
           15, 14, 13, 12, 11, 10])




```python
# 5 삼성전자 주가 데이터 다운로드
# -날짜 열 제거
# -시가, 종가, 고가, 저가, 거래량을 각각 추출
# -2024년 5월 1일~ 5월 3일까지 데이터만 추출
sam_arr = np.loadtxt('samsung.csv', skiprows=1, dtype=np.float32, delimiter=',')
sam_arr
```




    array([[   65100.   ,    65600.   ,    64900.   ,    65400.   ,
               64431.652,  8876749.   ],
           [   65600.   ,    65700.   ,    64700.   ,    65100.   ,
               64136.094,  9791064.   ],
           [   66300.   ,    66300.   ,    65400.   ,    65900.   ,
               64924.246,  9405365.   ],
           ...,
           [   77000.   ,    78500.   ,    76600.   ,    77500.   ,
               77500.   , 19007008.   ],
           [   77600.   ,    78600.   ,    77300.   ,    78000.   ,
               78000.   , 18900640.   ],
           [   79000.   ,    79000.   ,    77500.   ,    77600.   ,
               77600.   , 13070459.   ]], dtype=float32)




```python
sam_arr[:,0]
sam_arr[:,1]
sam_arr[:,2]
sam_arr[:,3]
sam_arr[:, 4]
sam_arr[:, 5]
```




    array([ 8876749.,  9791064.,  9405365.,  9366861., 13057727., 11648905.,
            8693913.,  8172021., 12334657., 10745504., 14431704., 20349344.,
           14470308.,  8561643.,  8192896., 14231160., 19549512., 27476896.,
           25666088., 14669296., 12161798., 12686829., 14796613., 19165568.,
           15050209., 12064287., 13227285., 12541046., 13614994., 15373696.,
           11100887., 11557883., 10626603., 11411007., 12329484., 10541901.,
            9442997.,  8783093., 12229967., 11694765., 10722181., 10214350.,
           12310610., 14777667., 17308876., 11713926., 12177392., 10375581.,
           14417279., 15882519., 10060049., 11697900., 10896412.,  9732730.,
           16528926., 13418597., 14314945., 30016220., 24261180., 19420684.,
           13035420., 12299254., 13835020., 20087090., 12360193., 10968505.,
           14664709., 17259672., 10227311.,  9781038.,  9352343., 13174578.,
           10778652., 11745006.,  9720067., 10500242.,  9549352., 15044463.,
            7032462.,  5824628.,  9114352.,  9181223., 15964630., 29738236.,
           26286496., 12330239., 11414620., 13741241., 10688118., 11785462.,
           11688599., 15955797., 21041408., 17823512., 16040727., 11820188.,
           10873015., 10796336.,  9897840., 13582516., 13143470., 14886491.,
           23361148., 16108313., 14386527., 19889202., 25209348., 19311380.,
            9724086., 12599299., 17299252., 16493184., 13985012., 15204495.,
           11625959., 12791710., 10610703., 15517624., 11334726., 10139270.,
           14488892., 13775256., 16350031., 10322234., 22228488., 17228732.,
           12901310., 12301373.,  9684347.,  9246919.,  9567984., 20148676.,
           15860451., 11494644., 10610157.,  9712881., 11105143.,  6775614.,
            6676685.,  9113857., 13283081.,  9283933., 15783714.,  9871284.,
           10229267., 12129682.,  8123087.,  8862017., 10859463.,  9861960.,
           13758646., 13116766., 27567592., 15419815.,  9690551.,  8907632.,
           16870156., 13478766., 14515608., 13164909., 20651042., 17797536.,
           17142848., 21753644., 15324439., 11304316., 11088724., 26019248.,
           20259528., 57691264., 13038939.,  2957915., 14760415., 22683660.,
           17853396., 23363428., 19673376., 14786224., 12860661., 11737747.,
           11160062., 13976521., 12244418., 15703560., 19881032., 14955881.,
           19026020., 14559254., 16566445., 20810708., 21966744., 12434945.,
           14120600., 13444781., 12726404., 14681477., 11503495., 15208934.,
           16225166., 14669352., 13201981., 11795859., 21176404., 23210474.,
           19505124., 21547904., 14516963., 19271348.,  9740504., 13011654.,
           15243134., 22545540., 22580556., 11520348., 15376066., 50106296.,
           44569800., 26724760., 18703996., 30551494., 17424596., 25084812.,
           27126366., 20116512., 37077944., 30493348., 25248934., 18883752.,
           18953232., 23725956., 25538008., 17061770., 26663772., 31949844.,
           22611632., 21370190., 31317564., 30469476., 18717700., 22166150.,
           15549134., 12755629., 14664474., 19007008., 18900640., 13070459.],
          dtype=float32)




```python
sam_arr[-1:-3:-1]
```




    array([[   79000.,    79000.,    77500.,    77600.,    77600., 13070459.],
           [   77600.,    78600.,    77300.,    78000.,    78000., 18900640.]],
          dtype=float32)




```python

```


```python

```
