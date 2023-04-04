import os
import re

def modify_text(text):
    # Remove everything before the first "
    text = text.split('"', 1)[1]
    # Replace the ");   " at the end with ".wav|"
    text = text.replace('");\t//', '.wav|')
    # Add the preceding audio filename
    audio_filename = text.split('.wav|', 1)[0] + '.wav'
    text = audio_filename + '|' + text.split('.wav|', 1)[1]
    return text

def process_files():
    # Get all files in the current directory with the ".d" extension
    files = [file for file in os.listdir('.') if file.endswith('.d')]
    
    # Process each file
    for filename in files:
        #use World-1250 encoding
        with open(filename, 'r', encoding='cp1250') as input_file:
            text = input_file.read()
                
            for line in text.splitlines():
                if line.strip() == '"""': # skip empty lines
                    continue
                match = re.search(r'^\s*(AI_Output.*)$', line)
                if match:
                    if not re.search(r'//\s*$', line): # check if the line contains anything between '//' and the end of the line
                        output_filename = f"output_{os.path.splitext(filename)[0]}.txt"
                        with open(output_filename, 'a', encoding='utf-8') as output_file:
                            modified_text = modify_text(match.group(1))
                            output_file.write(modified_text + '\n')
                            print(f"Line saved to {output_filename}: {modified_text}")
                        print(f"Output saved to {output_filename}")
                    else:
                        print("No output found in line.")
                        
            print(f"All output saved for {filename}.")

process_files()

print("Done")

print("Done")
