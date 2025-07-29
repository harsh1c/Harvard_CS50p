def main():
    prompt = input("Write something in camelCase...")
    to_snakecase(prompt)

def to_snakecase(convert):

    for i in convert:
        if i.islower():
            print(i , end="")
        elif i.isupper():
          i = i.lower()
          print(f"_{i}" , end ="")

main()