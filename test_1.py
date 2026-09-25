import pandas as pd
from scipy.cluster.vq import kmeans
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
data=pd.read_csv("C:\\Users\\DELL\\Downloads\\customer_data.csv")
print(data,'\n')
print(data.info(),'\n')
print(data.isnull(),'\n')
x=data[["Age","AnnualIncome","SpendingScore"]]
x_train,x_test=train_test_split(x,test_size=0.3,random_state=13)
silhouette_scores=[]

scale=StandardScaler()
x_train_scaled=scale.fit_transform(x_train)
x_test_scaled=scale.transform(x_test)
# print(x_test_scaled)
for k in range(2,10):
    model1=KMeans(n_clusters=k,random_state=12)
    labels=model1.fit_predict(x_train_scaled)
    score=silhouette_score(x_train_scaled,labels)
    silhouette_scores.append(score)
    print("K=",k,"Silhouette Score =",score)

model2=KMeans(n_clusters=2,random_state=23)
model2.fit(x_train_scaled)
clusters=model2.predict(x_test_scaled)

# print(model2.cluster_centers_,'\n')
print(data,'\n')
print(clusters)
centroids=scale.inverse_transform(model2.cluster_centers_)
print(centroids)

plt.scatter(x_test_scaled[:,0],x_test_scaled[:,1],c=clusters)
plt.xlabel("Age(scaled,test_data)")
plt.ylabel("AnnualIncome(scaled,test_data)")
# plt.legend()
plt.show()