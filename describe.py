import sys
import csv
from prettytable import PrettyTable
from read_data import Data  
    
def count (data, feature):
    count = 0
    for row in data:
        if row[feature]:
            count += 1
    return count

def mean(data, feature):
    sum = 0
    count_value = count(data, feature)
    for row in data:
        if row[feature]:
            sum += row[feature]
    return sum / count_value

def std(data, feature):
    mean_value = mean(data, feature)
    deviation = [row[feature] - mean_value for row in data if row[feature]]
    squared_deviation = [d ** 2 for d in deviation]
    variance = sum(squared_deviation) / len(deviation)
    return variance ** 0.5

def minimum(data, feature):
    min_value = float('inf')
    for row in data:
        if row[feature] and row[feature] < min_value:
            min_value = row[feature]
    return min_value

def find_percentile(data, feature, percentile):
    values = [row[feature] for row in data if row[feature]]
    values.sort()
    index = int(len(values) * percentile)
    return values[index]
        
def maximum(data, feature):
    max_value = float('-inf')
    for row in data:
        if row[feature] and row[feature] > max_value:
            max_value = row[feature]
    return max_value

def display_data(data):
    features = [
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

    calculations = [
        "Count",
        "Mean",
        "Std",
        "Min",
        "25%",
        "50%",
        "75%",
        "Max"
    ]

    for i, feature_group in enumerate(features, 1):
        table = PrettyTable()
        table.field_names = [' '] + feature_group
        for calculation in calculations:
            row = [calculation]
            for feature in feature_group:
                if calculation == "Count":
                    row.append(count(data, feature))
                elif calculation == "Mean":
                    row.append(mean(data, feature))
                elif calculation == "Std":
                    row.append(std(data, feature))
                elif calculation == "Min":
                    row.append(minimum(data, feature))
                elif calculation == "25%":
                    row.append(find_percentile(data, feature, 0.25))
                elif calculation == "50%":
                    row.append(find_percentile(data, feature, 0.5))
                elif calculation == "75%":
                    row.append(find_percentile(data, feature, 0.75))
                elif calculation == "Max":
                    row.append(maximum(data, feature))
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