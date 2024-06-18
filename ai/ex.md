#outliers 출력
# iqr*1.5+q3 초과, q1-iqr*1.5 미만

#이상치 : 367건
#data[(data['age'] > iqr*1.5+q3) | (data['age'] < q1-iqr*1.5)]

#정상치 : 29633 건
data[(data['age'] <= iqr*1.5+q3) & (data['age'] >= q1-iqr*1.5)]

df=data[(data['age'] <= iqr*1.5+q3) & (data['age'] >= q1-iqr*1.5)]

def gender_to_numeric(x):
    if x=="M":
scaled_feature['gender'] = scaled_feature['gender'].apply(gender_to_numeric)
scaled_feature['gender'].head()

scaled_feature['gender'] = scaled_feature['gender'].apply(gender_to_numeric)
scaled_feature['gender'].head()