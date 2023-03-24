import os
import codecs

#use script to force files into 'utf-8' encodings

folder_path = os.path.dirname(os.path.abspath(__file__))
encodings = ['utf-8', 'iso-8859-1', 'cp1252', 'utf-16', 'utf-32'] # add more encodings to try as needed

for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        for encoding in encodings:
            try:
                with codecs.open(os.path.join(folder_path, filename), 'r', encoding=encoding) as file:
                    file.read()
                    #print(f"{filename} decoded using {encoding}")
                    break
            except UnicodeDecodeError:
                continue
        else:
            print(f"Unable to decode {filename} with any of the specified encodings.")
            continue

        if encoding != 'utf-8':
            # Convert the file to UTF-8
            with codecs.open(os.path.join(folder_path, filename), 'r', encoding=encoding) as source_file:
                content = source_file.read()
            with codecs.open(os.path.join(folder_path, filename), 'w', encoding='utf-8') as target_file:
                target_file.write(content)
            print(f"{filename} converted to UTF-8.")
        else:
            #print(f"{filename} is already encoded in UTF-8.")
            one = 1

print("finish converting")
