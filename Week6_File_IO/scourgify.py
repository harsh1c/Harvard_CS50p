import sys
import os
import csv

def main():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    else:
        file_1 = sys.argv[1]
        file_2 = sys.argv[2]

        if not(file_1.endswith(".csv")):
            sys.exit("Not a CSV file")
        elif not(os.path.exists(file_1)):
            sys.exit("File does not exist")
        else:
            edit(file_1 , file_2)

def edit(file_1 , file_2):
    rows = []
    names = []
    houses = []
    first = []
    last = []

    with open(file_1) as f1:
        reader = csv.reader(f1)
        next(reader)  # Skip the header row
        for row in reader:
            rows.append(row)

    for row in rows:
        names.append(row[0])
        houses.append(row[1])

    for name in names:
        name = name.strip('"')
        last_name,first_name = name.split(", ")
        first.append(first_name)
        last.append(last_name)

    new_rows = list(zip(first,last,houses))

    with open(file_2, 'w', newline="") as f2:
        col_writer = csv.DictWriter(f2, fieldnames=["first", "last", "house"])
        col_writer.writeheader()

        for row in range(len(new_rows)):
            col_writer.writerow({"first": first[row], "last": last[row], "house": houses[row]})


main()
