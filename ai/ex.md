#outliers 출력
# iqr*1.5+q3 초과, q1-iqr*1.5 미만

#이상치 : 367건
#data[(data['age'] > iqr*1.5+q3) | (data['age'] < q1-iqr*1.5)]

#정상치 : 29633 건
data[(data['age'] <= iqr*1.5+q3) & (data['age'] >= q1-iqr*1.5)]

df=data[(data['age'] <= iqr*1.5+q3) & (data['age'] >= q1-iqr*1.5)]