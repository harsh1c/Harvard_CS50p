# GeoInsight

GeoInsight is a terminal-based CLI (Command Line Interface) program designed to provide detailed information about any place using its Wikipedia code. It uses data fetched from Wikipedia and Wikidata APIs to deliver insightful and engaging details about locations worldwide.

## Features
- Fetches introductory summaries for locations from Wikipedia.
- Displays information in aesthetically pleasing boxes for easy readability.
- Prompts users to explore more information about the location interactively.
- Implements error handling for invalid inputs, disambiguation errors, and network issues.
- Incorporates colorful and user-friendly messages using `colorama`.

## How to Use
1. Clone this repository to your local machine.
2. Ensure you have Python installed (version 3.6 or later).
3. Install the required libraries using the following command:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the program:
   ```bash
   python main.py
   ```
5. Enter the Wikidata code for the location you want to explore when prompted.
6. Interact with the program by choosing to view more details or exit.

## Example Interaction
```
🌍 Welcome to GeoInsight!
═════════════════════════════════════════════

Enter the Wikidata code of the location you're curious about: Q30

🌍 Exploring: United States
═════════════════════════════════════════════

Introduction:
+-----------------------------------------------------------------------+
| The United States of America (USA), commonly known as the United ... |
+-----------------------------------------------------------------------+

Do you want more information about this place?? (Yes or No)  Yes
+-----------------------------------------------------------------------+
| The USA consists of 50 states, a federal district, five major un...  |
+-----------------------------------------------------------------------+

--- End of Information ---

Thank you for using GeoInsight :)
```

## Dependencies
GeoInsight uses the following libraries:
- `requests`: For making HTTP requests to Wikidata API.
- `wikipedia`: For fetching summaries from Wikipedia.
- `texttable`: For creating aesthetic boxes around text.
- `colorama`: For adding colorful and visually appealing messages.
- `textwrap`: For formatting long paragraphs into readable lines.

## Error Handling
GeoInsight handles the following errors:
- **DisambiguationError:** When multiple results match a query.
- **HTTPTimeoutError:** When a request to Wikipedia times out.
- **Invalid Input:** When users provide incorrect input (e.g., invalid Wikidata code).

## Project Structure
```
GeoInsight/
├── project.py
├── information.py
├── my_api.env
├── README.md
├── recommend.py
├── requirements.txt
└── README.md
```

## Author
GeoInsight is a CS50P final project by [Harsh Chandrawal].

## Acknowledgements
- [CS50's Introduction to Programming with Python](https://cs50.harvard.edu/python/2022/)
- [Wikidata API](https://www.wikidata.org/wiki/Wikidata:Data_access)
- [Wikipedia Python Library](https://pypi.org/project/wikipedia/)

