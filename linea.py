
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from yellowbrick.cluster import KElbowVisualizer
from scipy.cluster.hierarchy import linkage
from scipy.cluster.hierarchy import dendrogram
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.decomposition import PCA

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 500)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.float_format', lambda x: '%.5f' % x)

df = pd.read_excel("C:/Users/Po/PycharmProjects/pythonProject/datasets/linea_2.xlsx")

#KExplatory Data Analysis

def check_df(dataframe, head=5):
    print("##################### Shape #####################")
    print(dataframe.shape)
    print("##################### Types #####################")
    print(dataframe.dtypes)
    print("##################### Nunique #####################")
    print(dataframe.nunique())
    print("##################### Head #####################")
    print(dataframe.head(head))
    print("##################### Tail #####################")
    print(dataframe.tail(head))
    print("##################### NA #####################")
    print(dataframe.isnull().sum())
    print("##################### Quantiles #####################")
    print(dataframe.describe([0.01, 0.05, 0.25, 0.50, 0.75, 0.95, 0.99, 1]).T)

check_df(df)

#Remove columns
df = df.drop (columns = ["Unnamed: 0"])

####### K-Means #######

scaled_columns = ["current_lxp", "dex_volume_usd","num_onchain_txns","days_old_onchain"]
scaler= MinMaxScaler()
df[scaled_columns].isna().sum()
df[scaled_columns] = df[scaled_columns].fillna(df[scaled_columns].mean())
df[scaled_columns] = scaler.fit_transform(df[scaled_columns])

kmeans = KMeans(n_clusters=4, random_state=17).fit(df[scaled_columns])
kmeans.get_params()
#{'algorithm': 'lloyd', 'copy_x': True, 'init': 'k-means++', 'max_iter': 300, 'n_clusters': 4,
# 'n_init': 'auto', 'random_state': None, 'tol': 0.0001, 'verbose': 0}

#####Optimum Cluster Count#####
kmeans = KMeans()

ssd = []
K = range(1,30)

for k in K:
    kmeans = KMeans(n_clusters=k).fit(df[scaled_columns])
    ssd.append(kmeans.inertia_)

#Elbow Visualisation Plots
plt.plot(K, ssd, "bx-")
plt.xlabel("SSE/SSR/SSD for Different K Values")
plt.title("Elbow Method for Optimum Clusters")
plt.show(block=True)

kmeans=KMeans()
elbow = KElbowVisualizer(kmeans, k=(2,20))
elbow.fit(df[scaled_columns])
elbow.show()
plt.savefig('elbow_plot.png')

#Recall data from excel file
df = pd.read_excel("C:/Users/Po/PycharmProjects/pythonProject/datasets/linea_2.xlsx")
df = df.drop (columns = ["Unnamed: 0"])
df.head()

#Remove inactive users who do not have any activity on the blockchain
df = df[(df["nft_volume_usd"] > 0) & (df["dex_volume_usd"] > 0) & (df["contracts_deployed"] > 0) & (df["times_contracts_called"] > 0)]

#Final Cluster Model
kmeans = KMeans(n_clusters=7).fit(df[scaled_columns])
clusters = kmeans.labels_

df["cluster"] = clusters
df["cluster"] = df["cluster"] + 1
df["cluster"].value_counts()

#Examining Clusters
selected_columns = ["current_lxp", "dex_volume_usd","num_onchain_txns","days_old_onchain"]
df.groupby("cluster")[selected_columns].agg(["count", "mean"])

#Redefining Cluster Count for the Model
kmeans = KMeans(n_clusters=5).fit(df[scaled_columns])
clusters = kmeans.labels_

df["cluster"] = clusters
df["cluster"] = df["cluster"] + 1
df["cluster"].value_counts()

#Examining Clusters
selected_columns = ["current_lxp", "dex_volume_usd","num_onchain_txns","days_old_onchain"]
agg_data = df.groupby("cluster")[selected_columns].agg(["count", "mean"])

#Examining Final Clusters
df["cluster"] = df["cluster"].replace({2: 4, 3: 4})
df["cluster"] = df["cluster"].replace({4: "Most Active Users", 5: "Active Users", 1: "Other Users"})
agg_data = df.groupby("cluster")[selected_columns].agg(["count", "mean"])

#Examining Final Clusters on Charts
for col in selected_columns:
    plt.figure(figsize=(10, 5))
    sns.barplot(x=agg_data.index, y=agg_data[(col, 'mean')], palette="viridis")
    plt.title(f"Cluster-wise Mean for {col}")
    plt.xlabel("Cluster")
    plt.ylabel("Mean")
    plt.show(block=True)

