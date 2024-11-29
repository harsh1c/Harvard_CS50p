import re
import sys


def main():
    print(count(input("Text: ")))


def count(text):

    my_list = re.findall(r"\b(um|UM|Um|uM)\b" , text)
    return len(my_list)

if __name__ == "__main__":
    main()