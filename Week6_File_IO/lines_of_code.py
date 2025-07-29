import sys
import os

def main():
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    else:
        file = sys.argv[1]

        if not(file.endswith(".py")):
            sys.exit("Not a Python file")
        elif not(os.path.exists(file)):
            sys.exit("File does not exist")
        else:
            line_counter(file)

def line_counter(file):
    with open(file) as fp:
        lines = fp.readlines()

        counter = 0

        for line in lines:
            line = line.strip()

            if line.startswith("#"):
                continue
            elif line.startswith("#") and (line-1).startswith("def"):
                counter=counter+1
            elif line == "":
                continue
            else:
                counter=counter+1
        print(counter)

main()