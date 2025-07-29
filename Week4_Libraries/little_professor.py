import random

def main():
    i = 0
    score = 0
    level = get_level()

    while i < 10:
        try:

            digits = generate_integer(level)
            print(f"{digits[0]} + {digits[1]} = ", end ="" )

            user_answer = int(input(""))
            answer = digits[0] + digits[1]

            j = 0
            while j<=3:
                if j  == 3:
                    score = score + j - 1
                    print(f"{digits[0]} + {digits[1]} = {answer}")
                    break
                elif answer != user_answer:
                    score = score - 1
                    if j < 2:
                        print("EEE")
                        print(f"{digits[0]} + {digits[1]} = ", end ="" )
                        user_answer = int(input(""))
                        j = j + 1
                        continue
                    else:
                        print("EEE")
                        j = j + 1
                        continue
                else:
                    print("", end ="")
                    break
            i = i + 1
            score = score + 1
        except (ValueError, TypeError):
           continue
    print(f"Score: {score}")




def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level == 1 or level == 2 or level == 3:
                return level
            else:
                continue

        except (ValueError, TypeError):
           continue



def generate_integer(level):

    digits = level

    match digits:
        case 1:
            first_number = random.randint(0, 9)
            second_number = random.randint(0, 9)
            return first_number , second_number

        case 2:
            first_number = random.randint(10, 99)
            second_number = random.randint(10, 99)
            return first_number , second_number

        case 3:
            first_number = random.randint(100, 999)
            second_number = random.randint(100, 999)
            return first_number , second_number



if __name__ == "__main__":
    main()