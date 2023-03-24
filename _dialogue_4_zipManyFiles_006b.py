import os
import zipfile

#tip: in cmd run 'copy *.txt _newfile.txt' to merge all txt files into one

#place wav files in the "SPEECH" subfolder while the text files are in the same folder as this code

def create_zip_files():
    # Create a new directory called "zipWavs" if it doesn't exist
    if not os.path.exists("zipWavs"):
        os.mkdir("zipWavs")

    # Get all audio files in the "audio_folder" directory
#    audio_files = [os.path.join("audio_folder", file) for file in os.listdir("audio_folder") if file.endswith('.wav')]
#    if not audio_files:
#        print("No audio files found in the audio_folder directory.")
#        return

    # Get all text files in the current directory that start with "audiofiles_"
    files = os.listdir('.')
    txt_files = [file for file in files if file.startswith('audiofiles_') and file.endswith('.txt')]

    # Process each text file
    for txt_file in txt_files:
        # Generate the name of the output zip file
        zip_file_name = txt_file.replace("audiofiles_", "").replace(".txt", "") + ".zip"
        zip_file_name = zip_file_name.replace("_div_", "_")
        
        # Create a new zip file inside the "zipWavs" directory
        zip_path = os.path.join("zipWavs", zip_file_name)
        with zipfile.ZipFile(zip_path, 'w') as zip:
            # Open the text file and add each audio file listed in it to the zip file
            with open(txt_file, 'r') as input_file:
                for line in input_file:
                    line = line.strip()
                    audio_file_path = os.path.join("SPEECH", line)
                    if os.path.isfile(audio_file_path):
                        zip.write(audio_file_path, line)
                    else:
                        print(f"File {line} not found in directory.")
        
        print(f"All files saved to {zip_path}")

create_zip_files()
