def gender_to_numeric(x):
    if x=="M":
        return 1
    if x=="F":
        return 2
    if x== 'not disclosed':
        return 3

scaled_feature['gender'] = scaled_feature['gender'].apply(gender_to_numeric)
scaled_feature['gender'].head()

scaled_feature.head()

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=5, random_state=0)

model = kmeans.fit(scaled_feature)