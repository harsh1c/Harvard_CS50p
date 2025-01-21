import sys
import requests
import dotenv
import os
from recommend import recommendation  # Importing recommendation function
from information import info  # Importing info function
from colorama import Fore, Style, init
import time

# Initialize colorama
init(autoreset=True)

def main():
    set_terminal_env()
    clear_screen()

    terminal_width = get_terminal_width()  # Get the width of the terminal

    # Print the header with centered text
    print(f"{Fore.LIGHTBLUE_EX}{Style.BRIGHT} ╔══════════════════════════════════════════════════════════════╗".center(
        terminal_width))
    print(f"     ║  🌍 {Fore.YELLOW}{Style.BRIGHT}GeoInsight - Explore the World at Your Fingertips!       {Style.RESET_ALL}║".center(
        terminal_width))
    print(f" ║{Fore.LIGHTWHITE_EX}{Style.BRIGHT}      Uncover the History that Shapes Every Place!            ║".center(
        terminal_width))
    print(f"{Fore.LIGHTBLUE_EX}{Style.BRIGHT} ╚══════════════════════════════════════════════════════════════╝".center(
        terminal_width))

    print(f"\n{'-' * 50}")

    location = get_location()  # Prompting user for location input (this is commented for now)
    place_type = ask_info()  # Asking for additional information about the location type

    key = "6e24e5c0d0414dabb576fca2fb247bd2"  # Your Geoapify API key (ensure it's secured in a .env file)

    # Check if API key is provided, exit if not
    if not key:
        sys.exit("API key not found. Please check your .env file.")

    print("Searching, please wait....")

    # Call the function to get location details based on the provided location and API key
    location_details = get_location_details(location, place_type, key)

    if location_details:
        print(f"\n{Fore.LIGHTGREEN_EX}✔️ Location found! Fetching details...{Style.RESET_ALL}")
        time.sleep(1)
        i = 1
        while True:
            if i > 1:
                print(f"{Fore.LIGHTBLUE_EX}🔍 Searching for the recommendations...{Style.RESET_ALL}")
            # Call recommendation function to get place recommendations based on location and place type
            place_id = recommendation(place_type, location_details)

            # Extract Wikidata code from the place id
            wiki_code = wikidata_code_extractor(place_id, key)

            if wiki_code == 'True':  # If 'True', continue searching for recommendations
                print(f"{Fore.YELLOW}🔄 Unable to fetch data. Trying another recommendation...{Style.RESET_ALL}")
                i+=1
                continue
            elif wiki_code == 'False':  # If 'False', exit the program
                print(f"\n{Fore.LIGHTBLUE_EX}🌟 Thanks for exploring with GeoInsight! Until next time! {Style.RESET_ALL}🌍")
                sys.exit()
            else:
               break


        # Call info function to display information based on Wikidata code
        info(wiki_code)
    else:
        print("Location not found. Please try again with a different location.")  # If no location details are returned, print an error message

def clear_screen():
    """Clears the terminal screen."""
    if sys.platform == "win32":
        os.system("cls")  # Command for Windows
    else:
        os.system("clear")

def get_terminal_width():
    """Attempts to get the terminal width, with a fallback if not available."""
    try:
        # Try to get terminal size using os.get_terminal_size()
        terminal_width = os.get_terminal_size().columns
    except OSError:
        # Fallback value in case terminal size can't be fetched
        terminal_width = 157  # Default width (80 characters)
    return terminal_width

def set_terminal_env():
    """Sets the TERM environment variable if not set."""
    if "TERM" not in os.environ:
        os.environ["TERM"] = "xterm-256color"  # Default TERM value for most terminals


def get_location():
    """Asks the user for a location and validates the input."""
    print(f"\n{Fore.LIGHTBLUE_EX}{Style.BRIGHT}🌟 GeoInsight Location Search 🌟")
    print(f"{Fore.LIGHTWHITE_EX}Examples: 'India', 'Eiffel Tower', or 'Tokyo'.")
    print(f"{Fore.YELLOW}Type 'exit' anytime to leave GeoInsight.\n")

    while True:
        location = input(
            f"{Fore.LIGHTCYAN_EX}🔍 Enter a location to search (e.g., a City, a Country): {Style.RESET_ALL}").strip()

        # Exit gracefully if the user types 'exit'
        if location.lower() == "exit":
            sys.exit(f"{Fore.LIGHTBLUE_EX}\n🌟 Thanks for exploring with GeoInsight! Until next time! {Style.RESET_ALL}🌍")

        if location:
            return location
        else:
            print(
                f"{Fore.LIGHTRED_EX}❌ Invalid input. Please enter a valid location (e.g., 'shajapur' or 'New York').{Style.RESET_ALL}")


def ask_info():
    """Prompts the user for more information about the location."""
    print(f"\n{Fore.LIGHTCYAN_EX}{Style.BRIGHT}🤔 Would you like to specify the type of location?{Style.RESET_ALL}")
    print(f"{Fore.LIGHTWHITE_EX}Choose one of the following options for better search results:")
    print(f"{Fore.YELLOW}• Country\n• State\n• City\n• District\n• None (If you're not sure!)\n")

    while True:
        # Ask the user to choose the location type directly
        choice = input(f"{Fore.LIGHTBLUE_EX}📍 Please specify the type of location ({Fore.YELLOW}Country, State, City, District, or None{Fore.LIGHTBLUE_EX}): {Style.RESET_ALL}").strip().lower()

        if choice in ["country", "state", "city", "district"]:
            print(f"{Fore.GREEN}✅ You selected: {choice.capitalize()}{Style.RESET_ALL}")
            return choice
        elif choice == "none":
            print(f"{Fore.GREEN}✅ No specific location type selected.{Style.RESET_ALL}")
            return "no"
        else:
            print(
                f"{Fore.RED}❌ Invalid choice. Please choose from 'Country', 'State', 'City', 'District', or 'None'.{Style.RESET_ALL}")


# Function to extract the API key from the .env file
def extract_api_key():
    dotenv.load_dotenv()
    api_key = os.getenv('KEY')
    return api_key


# Function to get location details from Geoapify API using the provided location and API key
def get_location_details(location, place_type, key):
    url = "https://api.geoapify.com/v1/geocode/search"
    params = {"text": location, "apiKey": key}  # Request parameters with location and API key

    try:
        # Send a request to the Geoapify API
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception if the response contains an error

        data = response.json()
        all_data = []

        # Check if any features are returned in the response
        if not data:
            return None
        if place_type == "no":
            for feature in data.get('features', []):
                all_data.append(feature["properties"])
        else:
            for feature in data.get('features', []):
                if place_type == feature["properties"]["result_type"]:
                    all_data.append(feature["properties"])
                else:
                    continue
        return all_data

    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}❌ Error: Unable to connect to the Geoapify API. Please check your connection or API key.{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Details: {e}{Style.RESET_ALL}")
        return None


# Function to extract the Wikidata code from the place ID using Geoapify API
def wikidata_code_extractor(place_id, key):
    url = f"https://api.geoapify.com/v2/place-details?id={place_id}&features=details,details.names&apiKey={key}"  # API endpoint for place details
    response = requests.get(url)  # Send GET request to the API

    try:
        if response.status_code == 200:
            data = response.json()
            wiki_code = data["features"][0]["properties"]["wiki_and_media"]["wikidata"]
            return wiki_code
        else:
            print(f"{Fore.RED}❌ Unable to connect to the server. Details: \nError: {response.status_code}{Style.RESET_ALL}")

            print(f'Error: {response.status_code}')  # Print error if the status code is not 200
    except KeyError:
        # If the expected data is not found, handle the error
        print(f"{Fore.LIGHTRED_EX}⚠️ Looks like we don't have data for that...Sorry for the inconvenience :(.{Style.RESET_ALL}")

        while True:

            re_input = input(f"{Fore.LIGHTYELLOW_EX}🔄 Would you like to search for another location? {Fore.LIGHTGREEN_EX}(yes){Fore.LIGHTYELLOW_EX}/{Fore.LIGHTRED_EX}(no){Style.RESET_ALL}: ").strip().lower()
            if re_input == "yes":
                return "True"
            elif re_input == "no":
                return "False"
            else:
                continue


if __name__ == '__main__':
    main()
