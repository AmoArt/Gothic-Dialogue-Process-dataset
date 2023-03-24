import os

#use script to merge text files

folder_path = os.path.dirname(os.path.abspath(__file__))
output_file = os.path.join(folder_path, '_merged.txt')

# Get all txt files in folder
input_files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]

with open(output_file, 'w', encoding='utf-8') as outfile:
    for i, fname in enumerate(input_files):
        try:
            with open(os.path.join(folder_path, fname), 'r', encoding='utf-8') as infile:
                if i != 0:
                    outfile.write('\n')  # add newline between files
                outfile.write(infile.read())
        except UnicodeDecodeError:
            print(f"Unable to decode file {fname}. Skipping...")

# Remove extra empty newlines
with open(output_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

with open(output_file, 'w', encoding='utf-8') as f:
    for line in lines:
        if line.strip() != "":
            f.write(line)

with open(output_file, 'rb+') as output:
    if os.stat(output_file).st_size > 0:  # Check if file is not empty
        output.seek(-1, os.SEEK_END)
        if output.read(1) == b'\n':
            output.seek(-1, os.SEEK_END)
            output.truncate()
        else:
            pass  # Do nothing if there isn't an empty newline at the end

print(f"All files merged and saved to {output_file}, with extra empty newlines removed.")
