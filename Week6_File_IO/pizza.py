from tabulate import tabulate
import csv
import sys
import os

def main():
    file = sys.argv[1]

    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    else:

        if not(file.endswith(".csv")):
            sys.exit("Not a CSV file")
        elif not(os.path.exists(file)):
            sys.exit("File does not exist")
        else:
            table(file)

def table(file):

    rows =[]

    with open(file) as f:
        reader = csv.reader(f)

        for row in reader:
            rows.append(row)
    headers = rows[0]
    print(tabulate(rows[1:], headers, tablefmt="grid"))

main()