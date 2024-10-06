import sys
import csv
from prettytable import PrettyTable
from read_data import Data  
    
def count (data, subject):
    count = 0
    for row in data:
        if row[subject]:
            count += 1
    return count

def mean(data, subject):
    sum = 0
    count_value = count(data, subject)
    for row in data:
        if row[subject]:
            sum += row[subject]
    return sum / count_value

def std(data, subject):
    mean_value = mean(data, subject)
    deviation = [row[subject] - mean_value for row in data if row[subject]]
    squared_deviation = [d ** 2 for d in deviation]
    variance = sum(squared_deviation) / len(deviation)
    return variance ** 0.5

def minimum(data, subject):
    min_value = float('inf')
    for row in data:
        if row[subject] and row[subject] < min_value:
            min_value = row[subject]
    return min_value

def find_percentile(data, subject, percentile):
    values = [row[subject] for row in data if row[subject]]
    values.sort()
    index = int(len(values) * percentile)
    return values[index]
        
def maximum(data, subject):
    max_value = float('-inf')
    for row in data:
        if row[subject] and row[subject] > max_value:
            max_value = row[subject]
    return max_value

def display_data(data):
    subjects = [
        "Arithmancy",
        "Astronomy",
        "Herbology",
        "Defense Against the Dark Arts",
        "Divination",
        "Muggle Studies"
    ], [
        "Ancient Runes",
        "History of Magic",
        "Transfiguration",
        "Potions",
        "Care of Magical Creatures",
        "Charms",
        "Flying"
    ]

    features = [
        "Count",
        "Mean",
        "Std",
        "Min",
        "25%",
        "50%",
        "75%",
        "Max"
    ]

    for i, subject_group in enumerate(subjects, 1):
        table = PrettyTable()
        table.field_names = [' '] + subject_group
        for feature in features:
            row = [feature]
            for subject in subject_group:
                if feature == "Count":
                    row.append(count(data, subject))
                elif feature == "Mean":
                    row.append(mean(data, subject))
                elif feature == "Std":
                    row.append(std(data, subject))
                elif feature == "Min":
                    row.append(minimum(data, subject))
                elif feature == "25%":
                    row.append(find_percentile(data, subject, 0.25))
                elif feature == "50%":
                    row.append(find_percentile(data, subject, 0.5))
                elif feature == "75%":
                    row.append(find_percentile(data, subject, 0.75))
                elif feature == "Max":
                    row.append(maximum(data, subject))
            table.add_row(row)
        print(table)

def main():
    if len(sys.argv) != 2:
        print("Usage: python describe.py <dataset>")
        sys.exit(1)
    filename = sys.argv[1]
    describe = Data(filename)
    display_data(describe.data)

if __name__ == "__main__":
    main()