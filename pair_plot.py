import sys
from read_data import Data
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


def pair_plot(data):
    features = {
        "Arithmancy": "Arith",
        "Astronomy": "Astro",
        "Herbology": "Herbo",
        "Defense Against the Dark Arts": "DADA",
        "Divination": "Divin",
        "Muggle Studies": "Muggle",
        "Ancient Runes": "Runes",
        "History of Magic": "History",
        "Transfiguration": "Transf",
        "Potions": "Potions",
        "Care of Magical Creatures": "CMC",
        "Charms": "Charms",
        "Flying": "Flying",
        "Hogwarts House": "Houses"
    }

    df = pd.DataFrame(data, columns=features.keys())
    df = df.rename(columns=features)

    sns.pairplot(df, hue="Houses", kind="scatter", diag_kind="hist", height=1.5)

    plt.gcf().set_size_inches(15, 20)

    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

    plt.show()


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python3 pair_plot.py <dataset>")
    filename = sys.argv[1]
    data = Data(filename)
    pair_plot(data.data)


if __name__ == "__main__":
    main()
