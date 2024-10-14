import sys
from read_data import Data
import matplotlib.pyplot as plt

def scatter_plot(data):
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
        "Flying"
    ]

    fig, ax = plt.subplots()

    fig.subplots_adjust(bottom=0.2)

    for a in range(len(features)):
        for b in range(a + 1, len(features)):
            if len(features[a]) != len(features[b]):
                if len(features[a]) > len(features[b]):
                    for _ in range(len(features[a]) - len(features[b])):
                        features[b] += ""
                elif len(features[a]) < len(features[b]):
                    for _ in range(len(features[b]) - len(features[a])):
                        features[a] += ""
            plt.scatter(
                [student[features[a]] for student in data if features[a] in student],
                [student[features[b]] for student in data if features[b] in student]
            )
                
            plt.xlabel(features[a])
            plt.ylabel(features[b])
            plt.title(f"What are the two features that are similar ?")
            plt.show()

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python3 histogram.py <dataset>")
        sys.exit(1)
    filename = sys.argv[1] 
    data = Data(filename)
    scatter_plot(data.data)

if __name__ == "__main__":
    main()