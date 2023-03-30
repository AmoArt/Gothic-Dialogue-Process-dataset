import os
import re

# Dictionary to map symbols to letters
symbol_map_swap = {
    ":": " ",
    "": ",",
    "¥": "Ą",
    "¹": "ą",
    "Âœ": "ś",
    "": "Ś",
    "Ãª": "ę",
    "Ã¦": "ć",
    "ñ": "ń",
    "£": "Ł",
    "³": "ł",
    "¯": "Ż",
    "Âæ": "ż",
    "Ê": "Ę",
    "¿": "ż",
    "ê": "ę",
    "æ": "źć",
    "": "ź",
    "": "ź",
    "": "ź",
    "": "Ś",
    "": "ś",
    "æ": "ć",
    "": "Ź",
    "æ": "ć"
} #lines are not empty, just has an invisible characters

def modify_line(line):
    """
    Replaces symbols with their corresponding letters
    """
    for symbol, letter in symbol_map_swap.items():
        line = line.replace(symbol, letter)
    return line

def process_files():
    # Get all files in the current directory with the ".txt" extension
    files = [file for file in os.listdir('.') if file.endswith('.txt')]

    # Process each file
    for filename in files:
        with open(filename, 'r', encoding='utf-8') as input_file:
            # Read all lines from the file
            lines = input_file.readlines()

        with open(filename, 'w', encoding='utf-8') as output_file:
            # Process each line
            for line in lines:
                # Skip empty lines
                if not line.strip():
                    continue
                # Modify the line
                modified_line = modify_line(line)
                # Write the modified line to the output file
                output_file.write(modified_line)

        print(f"Output saved to {filename}")

process_files()
print("\ndone")
