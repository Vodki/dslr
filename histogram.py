import sys
from read_data import Data
import matplotlib.pyplot as plt
from matplotlib.widgets import Button


def sort_by_house(data):
    houses = {}
    for student in data:
        house = student["Hogwarts House"]
        if house not in houses:
            houses[house] = []
        houses[house].append(student)
    return houses


def histogram(houses, subject, fig, ax):
    ax.clear()

    colors = {
        'Ravenclaw': 'blue',
        'Slytherin': 'green',
        'Gryffindor': 'red',
        'Hufflepuff': 'yellow'
    }

    for house, students in houses.items():
        scores = [student[subject] for student in students if student[subject]]
        ax.hist(scores, bins=50, alpha=0.6, label=house, color=colors[house])

    ax.legend(loc='upper right')
    ax.set_title(f'{subject} Scores by Houses')
    ax.set_xlabel('Score')
    ax.set_ylabel('Frequency')
    fig.canvas.draw()


def show_histogram(houses):
    subjects = [
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

    ind = 0

    def next(event):
        nonlocal ind
        ind += 1
        i = ind % len(subjects)
        histogram(houses, subjects[i], fig, ax)

    def prev(event):
        nonlocal ind
        ind -= 1
        i = ind % len(subjects)
        histogram(houses, subjects[i], fig, ax)

    axprev = fig.add_axes([0.7, 0.05, 0.1, 0.075])
    axnext = fig.add_axes([0.81, 0.05, 0.1, 0.075])
    bnext = Button(axnext, 'Next')
    bnext.on_clicked(next)
    bprev = Button(axprev, 'Previous')
    bprev.on_clicked(prev)

    histogram(houses, subjects[0], fig, ax)
    plt.show()


def main():
    if len(sys.argv) != 2:
        print("Usage: python histogram.py <dataset>")
        sys.exit(1)
    filename = sys.argv[1]
    data = Data(filename)
    houses = sort_by_house(data.data)
    show_histogram(houses)


if __name__ == "__main__":
    main()
