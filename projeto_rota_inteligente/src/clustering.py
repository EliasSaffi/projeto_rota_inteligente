
import pandas as pd
from sklearn.cluster import KMeans

def cluster_entregas(path, k=3):
    df = pd.read_csv(path)
    model = KMeans(n_clusters=k, random_state=0)
    df["cluster"] = model.fit_predict(df[["x","y"]])
    return df
