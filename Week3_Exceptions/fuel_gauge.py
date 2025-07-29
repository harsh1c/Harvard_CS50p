def main():
    prompt = input("Fraction: ").strip()
    split_verify(prompt)
    convertor(prompt)

def split_verify(prompt):
    if "/" in prompt:
        return True
    else:
        return False

def convertor(prompt):
    while True:

        try:
            if split_verify(prompt) != True:
                raise ValueError

            else:
                numerator,denominator = prompt.split("/")
                if int(numerator)>int(denominator):
                    raise ValueError
                else:
                    percent = int(numerator)/int(denominator)*100
                    if percent<=1:
                        print("E")
                    elif percent>=99:
                        print("F")
                    else:
                        print(f"{percent:.0f}%")
                    break
        except ValueError:

                prompt = input("Fraction: ").strip()

        except ZeroDivisionError:
            prompt = input("Fraction: ").strip()
main()