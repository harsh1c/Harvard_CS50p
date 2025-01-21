import sys
import requests
import wikipedia
from texttable import Texttable
from colorama import Fore, Style, init
import textwrap

init(autoreset=True)

def info(wiki_code):
    """
    Fetches and displays information about a place using its Wikipedia code.
    """
    # URL to fetch entity data from Wikidata API
    url = f"https://www.wikidata.org/w/api.php?action=wbgetentities&ids={wiki_code}&languages=en&sites=enwiki&format=json"

    response = requests.get(url)
    data = response.json()

    title = data["entities"][wiki_code]["sitelinks"]["enwiki"]["title"]

    # Fetch the introduction of the place from Wikipedia
    location_summary = get_wikipedia_intro(title)

    if len(location_summary) > 0:
        # Display each part of the summary if available
        i = 1
        while len(location_summary) > i:
            ask_for_more_info()
            print_in_box(location_summary[i])
            i += 1
        print("\n--- End of Information ---\n")
    else:
        # If no additional information is available
        print("No additional information available.")

    # Exit the program
    sys.exit("Thank you for using GeoPedia :)")


def get_wikipedia_intro(title):
    """
    Fetches the introductory summary of the given title from Wikipedia.
    """
    try:
        print(f"{Fore.GREEN}\n🌍 Exploring: {Style.BRIGHT}{title}{Style.RESET_ALL}")
        print("═════════════════════════════════════════════\n")
        print(f"{Fore.YELLOW}Introduction:{Style.RESET_ALL}")
        # Fetch the summary of the place from Wikipedia and split into lines
        location_summary = wikipedia.summary(title, auto_suggest=False).split("\n")

        # Print the first line as an introduction
        print_in_box(location_summary[0])
        return location_summary
    except wikipedia.exceptions.DisambiguationError as e:
        # Handle disambiguation errors (multiple possible matches for a title)
        print(f"Disambiguation error: {e}")
        return []
    except wikipedia.exceptions.HTTPTimeoutError:
        # Handle timeout errors if the request takes too long
        print("Request timed out. Please try again later.")
        return []


def print_in_box(paragraph, width=120):
    # Wrap the text to the specified width
    wrapped_text = textwrap.fill(paragraph, width=width)

    # Check if the wrapped_text is empty (i.e., only whitespace)
    if not wrapped_text.strip():
        print("No information available.")
        return

    # Create a Texttable object
    t = Texttable()

    # Set the alignment and other properties
    t.set_cols_align(["c"])  # Align text to the center

    # Set the column width based on the wrapped text's longest line
    max_length = max(len(line) for line in wrapped_text.splitlines())
    t.set_cols_width([max_length])  # Adjust width based on the longest line

    # Add the entire wrapped text as a single row
    t.add_row([wrapped_text])

    # Draw the table (box) without any internal line breaks
    print(t.draw())


def ask_for_more_info():
    """
    Asks the user if they want more information about the place.
    Exits the program if the user chooses 'No'.
    """
    while True:
        # Prompt user for input
        more_info = input("Do you want more information about this place?? (Yes or No)  ").lower().strip()

        # If the user wants more information, break out of the loop and continue
        if more_info == "yes":
            break
        # If the user doesn't want more information, exit the program
        elif more_info == "no":
            sys.exit("Thank you for using GeoPedia :)")
        else:
            # If the input is invalid, prompt again
            print("Invalid input. Please type 'Yes' or 'No'.")
