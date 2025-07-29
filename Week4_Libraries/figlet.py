import sys
import pyfiglet
import random

def main():
    font_list = pyfiglet.FigletFont.getFonts()

    if len(sys.argv) == 1:
        prompt = input("")
        rando_font =  random.choice(font_list)
        f = pyfiglet.figlet_format(prompt, font= rando_font)
        print(f)
    elif len(sys.argv) == 2:
        sys.exit("Invalid usage")
    elif len(sys.argv) == 3:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            if sys.argv[2] in font_list:
                prompt = input("")
                f = pyfiglet.figlet_format(prompt, font = sys.argv[2])
                print(f)
            else:
                sys.exit("Invalid usage")
        else:
            sys.exit("Invalid usage")

main()