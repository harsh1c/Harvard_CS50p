question = input('What is the answer to the Great Question of Life, the Universe and Everything ? ').lower().strip()

match question:
    case '42' | "forty two"  |  "forty-two":
        print('yes')
    case _:
        print('no')