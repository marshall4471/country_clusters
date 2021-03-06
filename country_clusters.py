# -*- coding: utf-8 -*-
"""mail_clusters.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JaCbyxtokgdu3JwQgd_jKwcLIMJY3hHD
"""

import zipfile
from google.colab import drive

drive.mount('/content/drive/')

zip_ref = zipfile.ZipFile('/content/country.zip', 'r')
zip_ref.extractall()
zip_ref.close()

from sklearn.cluster import KMeans
import seaborn as sns
import matplotlib.pyplot as plt

import pandas as pd

df = pd.read_csv('/content/Country-data.csv')

df.head()



from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder

le =  LabelEncoder()
for i in df:
    if df[i].dtype=='object':
        df[i] = le.fit_transform(df[i])
    else:
        continue

S=StandardScaler()

S.fit_transform(df)

model = KMeans

model=KMeans(n_clusters=8,random_state=10)
cluster=model.fit_predict(df)

sns.scatterplot(x=df['income'],y=df['child_mort'],hue=cluster)
plt.title("Clusters from country information data as you can see income impacts early childhood survival")
plt.show()