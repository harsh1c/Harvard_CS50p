import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    source_url = re.search(r"(src=\")(http:\/\/|https:\/\/|https:\/\/www\.)(youtube\.com\/embed\/)(\w+)\"", s)

    if source_url:
        return f"https://youtu.be/{source_url[4]}"
    else:
        return None

if __name__ == "__main__":
    main()