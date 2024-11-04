import csv
from guitar import Guitar  # Importing Guitar class from guitar.py

def main():
    filename = 'guitars.csv'
    guitars = load_guitars_from_file(filename)

    print("These are the current guitars:")
    for guitar in guitars:
        print(guitar)

    add_guitars(guitars)
    guitars.sort()
    write_guitars_to_file(filename, guitars)

    print("These are the updated guitars:")
    updated_guitars = load_guitars_from_file(filename)
    for guitar in updated_guitars:
        print(guitar)

def load_guitars_from_file(filename):
    """Load guitars from a CSV file."""
    guitars = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            name, year, cost = row
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars

def add_guitars(guitars):
    """Function to add new guitars via user input."""
    while True:
        name = input("Enter the name of the guitar: ")
        if name == "":
            break
        year = int(input("Enter the year of the guitar: "))
        cost = float(input("Enter the cost of the guitar: "))
        guitars.append(Guitar(name, year, cost))

def write_guitars_to_file(filename, guitars):
    """Write guitars to a CSV file."""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])

if __name__ == '__main__':
    main()
