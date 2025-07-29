def main():

    order_calculator()

def order_calculator():
    menu ={
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }
    while True:
        try:
            dish = input("Item: ").title()
            if dish not in menu:
                raise KeyError
            else:
                total = menu[dish]
                print(f"Total: ${total:.2f}")

                while True:
                    try:
                        dish = input("Item: ").title()
                        total = total + menu[dish]
                        print(f"Total: ${total:.2f}")
                    except KeyError:
                        continue


        except EOFError:
            print("")
            break
        except KeyError:
            continue


main()