import sys
from read_data import Data
import matplotlib.pyplot as plt
from matplotlib.widgets import Button


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

    fig, ax = plt.subplots(figsize=(10, 8))
    plt.subplots_adjust(bottom=0.2)

    plot_index = [0, 1]

    def update_plot():
        ax.clear()
        a, b = plot_index
        ax.scatter(
            [student[features[a]]
                for student in data if features[a] in student],
            [student[features[b]]
                for student in data if features[b] in student]
        )
        ax.set_xlabel(features[a])
        ax.set_ylabel(features[b])
        ax.set_title(f"Scatter plot: {features[a]} vs {features[b]}")
        fig.canvas.draw()

    def next_plot(event):
        if (plot_index[1] + 1 == len(features) and
                plot_index[0] + 2 != len(features)):
            plot_index[0] = (plot_index[0] + 1) % len(features)
            plot_index[1] = (plot_index[0] + 1) % len(features)
        elif (plot_index[0] + 2 == len(features) and
              plot_index[1] + 1 == len(features)):
            plot_index[0] = 0
            plot_index[1] = 1
        else:
            plot_index[1] = (plot_index[1] + 1) % len(features)
        update_plot()

    def prev_plot(event):
        if (plot_index[0] == 0 and plot_index[1] == 1):
            plot_index[0] = len(features) - 2
            plot_index[1] = len(features) - 1
            print("YES")
        elif (plot_index[0] != 0 and
              plot_index[1] == plot_index[0] + 1):
            plot_index[0] = (plot_index[0] - 1) % len(features)
            plot_index[1] = len(features) - 1
            print("NO")
        else:
            plot_index[1] = (plot_index[1] - 1) % len(features)
        update_plot()

    axprev = plt.axes([0.7, 0.05, 0.1, 0.075])
    axnext = plt.axes([0.81, 0.05, 0.1, 0.075])
    bnext = Button(axnext, 'Next')
    bnext.on_clicked(next_plot)
    bprev = Button(axprev, 'Previous')
    bprev.on_clicked(prev_plot)

    update_plot()
    plt.show()


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python3 scatter_plot.py <dataset>")
    filename = sys.argv[1]
    data = Data(filename)
    scatter_plot(data.data)


if __name__ == "__main__":
    main()
