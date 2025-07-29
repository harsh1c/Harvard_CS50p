def main():
    greeting = input("Question : ").lower().strip()
    amount = value(greeting)

    if amount == 0:
        print("$0")
    elif amount == 20:
        print("$20")
    else:
        print("$100")


def value(greeting):
    greeting = greeting.lower().strip()
    if greeting.startswith("hello") :
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100




if __name__ == "__main__":
    main()