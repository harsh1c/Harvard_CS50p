def main():
    while True:
        try:
            prompt = input("Fraction: ").strip()

            percentage = convert(prompt)
            print(gauge(percentage))

        except (ValueError, ZeroDivisionError):
            prompt = input("Fraction: ").strip()


def convert(fraction):

    while True:

        if "/" not in fraction:
            raise ValueError

        else:
            numerator, denominator = fraction.split("/")

            if int(denominator) == 0:
                raise ZeroDivisionError
            elif int(numerator) > int(denominator):
                raise ValueError
            elif denominator.isalpha() or numerator.isalpha():
                raise ValueError

            else:
                percent = int(numerator) / int(denominator) * 100
                return int(f"{percent:.0f}")


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage:}%"


if __name__ == "__main__":
    main()