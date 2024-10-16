import sys
from read_data import Data
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


def pair_plot(data):
    features = [
        "Arithmancy",
        "Astronomy",
        "Herbology",
        "Defense Against the Dark Arts",
        "Divination",
        "Muggle Studies",
        "Ancient Runes",
        "History of Magic",
        "Transfiguration",
        "Potions",
        "Care of Magical Creatures",
        "Charms",
        "Flying",
        "Hogwarts House"
    ]

    df = pd.DataFrame(data, columns=features)

    sns.pairplot(df, hue="Hogwarts House", kind="scatter", diag_kind="hist")

    plt.show()


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python3 pair_plot.py <dataset>")
    filename = sys.argv[1]
    data = Data(filename)
    pair_plot(data.data)


if __name__ == "__main__":
    main()
