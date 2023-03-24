# Gothic-Dialogue-Process-dataset
An semi automatic process of reusing the decomiled audio files and dialogue scripts from Gothic game to convert them into an usable audio dataset.

# Preperations
There are multiple python files.

### step 0
First use the tools GothicSourcerV3_14 to decompile gothic.dat to gain the dialogue script .d files and GothicVDFS to extract dialogue from the speech.VDF files. Place the .d files in 'Dialoge' subfolder and audio files in 'SPEECH' subfolder.

Copy the python files into the main folder.

# Processing the files

## Cleaning the .d dialogue
### step 1
place the "_dialogue_1_seperator_005a" in the "Dialoge" and run the script, move the generated "output_*.txt" files from suffolder to the main folder.

### step 2
in main folder, run the "_dialogue_2_divider_003a.py" to split the previous text into the npc lines and "*_PC.txt" text lines, use the __txt_decoder_force_001.py to make all the text files in a utf-8 encodings (no idea why but some files are saved as iso-8859-1 encodings).

### step 3
Move all the "*_PC.txt" to new subfolder, use the  __txt_merger_002.py to merge all of the main character lines into new  '_merged.txt' file, than move  '_merged.txt' back to main folder.

### step 4
Remove all the "output_*" text files as they are not needed anymore.

### step 5
Now you have a technically all the files needed to use those files as a training dataset. Here is example of the inside structure of the text file:
DIA_DiegoNW_NeedHelp_WhoAreYou_15_00.wav|Who are you?

## zip archive the audio
### step 6
Run the _dialogue_3_audios_001c.py to create a new text files "audiofiles_*", they will act as temporary anchor for the next script.

### step 7a
Run the _dialogue_4_zipManyFiles_006b.py, this code will use above "audiofiles_*" and dig thru the 'SPEECH' subfolder to add the wav files into new zip files named after the anchor text file inside new subfoder 'zipWavs'.

### step 7b
Remove the "audiofiles_*" text files.

Use some kind of batch rename program to change the name of  "output2_*.txt" files to just their filenames without the "output2_" (or dont if that doesn't bother you).

Run __txt_decoder_force_001.py one more time to see if everything is correct. 

Save and do whatever you want with your dataset files.

