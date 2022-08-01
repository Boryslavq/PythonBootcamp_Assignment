import csv


class Notes:

    def __init__(self, file: str):
        self.file = file
        self.notes = self.read()

    def read(self):
        with open(self.file, "r", encoding='utf-8') as file:
            notes = list(csv.reader(file))
            return notes

    def pretty_print(self):
        for new_note in self.notes:
            print(*new_note)

    def add(self, new_note: list):
        with open(self.file, "a", newline='') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow(new_note)

    def get_highest(self):
        return self._get_sorted_array(self.notes, reverse=True)

    def get_lowest(self):
        return self._get_sorted_array(self.notes, reverse=False)

    def get_average(self):
        summ = 0
        for newNote in self.notes:
            summ += int(newNote[2])

        return summ / len(self.notes)

    @staticmethod
    def _get_sorted_array(array: list, reverse=False):
        if reverse:
            return sorted([arr for arr in array if int(arr[2]) > 3], reverse=reverse)
        return sorted([arr for arr in array if int(arr[2]) <= 3], reverse=reverse)


if __name__ == '__main__':
    note = Notes("notes.csv")
    note.read()
    note.pretty_print()
    note.add(["Movie 43", "awful", 1])
    print(note.get_highest())
    print(note.get_lowest())
    print(note.get_average())
