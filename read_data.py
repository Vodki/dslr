import sys
import csv


class Data:
    def __init__(self, filename) -> None:
        self.data = self.read_data_set(filename)
        if not self.data:
            sys.exit(1)

    def read_data_set(self, filename):
        file_path = f"datasets/{filename}"
        try:
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                return [{k: self.parse_value(k, v) for k, v in row.items()} for row in reader]
        except FileNotFoundError:
            print(f"File {filename} not found.")
        except Exception as e:
            print(f"An error occured: {e}")
        return []

    def parse_value(self, key, value):
        if not value:
            return None
        if key == "Index":
            return int(value)
        if key in [
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
        ]:
            return float(value)
        return value
