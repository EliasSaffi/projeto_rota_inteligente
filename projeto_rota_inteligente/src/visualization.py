
import matplotlib.pyplot as plt

def plot_clusters(df):
    plt.scatter(df["x"],df["y"])
    plt.savefig("outputs/clusters.png")
    plt.close()

def plot_mapa(df):
    plt.scatter(df["x"],df["y"])
    plt.title("Mapa de Entregas")
    plt.savefig("outputs/mapa_entregas.png")
    plt.close()
