import inflect
p = inflect.engine()

def main():
    names = []
    while True:
        try:
            name = input()
            names.append(name)
        except EOFError:
            joined_names = p.join(names )
            if len(names) == 1:
                print("Adieu, adieu, to", names[0])
                break
            else:
                print("Adieu, adieu, to", joined_names)
                break

main()