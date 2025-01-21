from datetime import date
from datetime import datetime
import sys
import inflect

def main():
    d_o_b = input("Date of Birth: ").strip()
    words_version = words_convert(d_o_b)
    print(words_version)

def minute_conversion(d_o_b):
     try:
        year, month, day = d_o_b.split('-')
        date1 = date(int(year), int(month), int(day))
        date2 = date.today()

        if date2 > date1:
            return (date2-date1).days * 24 * 60
        else:
            sys.exit("you are not born yet")
     except ValueError:
         sys.exit("Invalid Date")
def words_convert(d_o_b):
    minutes_lived = minute_conversion(d_o_b)

    p = inflect.engine()
    words = p.number_to_words(minutes_lived, andword="")
    return words.capitalize() + " minutes"

if __name__ == "__main__":
    main()