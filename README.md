# Gothic-Dialogue-Process-dataset
An semi automatic process of reusing the decomiled audio files and dialogue scripts from Gothic game to convert them into an usable audio dataset.
(some handholding will be required as there are some mistakes and duplicates lines in the orginal Gothic script that mess with runing this code)
The output of this will be series of text files ('audio-filename.wav|dialogue-transcript') and folder "zipWavs" containing the coresponding the zips to the text files (with exception for the "_PlayerC", for unknow readon text and zip file are not name the same, so you will need to fix that by hand)

# Preperations
There are multiple python files in here, but before that, you will need to install desired version of Gothic on your pc.
Then donload this github python files, as well as the program 'GothicSourcerV3_14' and 'GothicVDFS'.

Additionally get yourself some kind programm to rename files in the whole batch, the one I would recommend is 'Bulk Rename Utility'.

### step 0
First use the tools GothicSourcerV3_14 to decompile gothic.dat to gain the dialogue script .d files and GothicVDFS to extract dialogue from the speech.VDF files. 
Place the .d files in 'Dialoge' subfolder and move the audio files folder 'SPEECH' to become a subfolder inside the 'Dialoge' folder.

e.g. C:\wipFolder\Dialoge\SPEECH

Copy the python files into the main 'Dialoge' folder.

# Processing the files

## Cleaning the .d dialogue
### step 1

IF you are working with German or English version of the game, run the code below:
Run "_dialogue_1_seperator_005a" in the "Dialoge" folder, to generate "output_*.txt" files.

IF you are working with Polish version of the game, run this (ignore instructions regarding the "_dialogue_1b_letters_convert_POL", that code is outdated.):
Run "_dialogue_1_seperator_005b_POL"

IF you are working with Russian version of the game, run this:
Run "_dialogue_1_seperator_005b_RUS"




step 1b
IF you are converting files from Polish, you will notice that the dialogue lines have many strnge looking characters, as the text file editor is not able to decode the text correcly, so run the "_dialogue_1b_letters_convert_POL" python code to bute force swap the incorrect symbols to correct Polish letters.
I curretly do not have an supporting file for the German, Russian or any other language version. However the code is just a simple symbol dictionary that is pretty easy to edit.

### step 2
Run the "_dialogue_2_divider_003a.py" to split the previous text into the npc lines and "*_PlayerC.txt" text lines.
(if you run in problem of the decoder not being able to upen the file use the __txt_decoder_force_001.py to make all the text files into a utf-8 encodings. no idea why but some files are saved as iso-8859-1 encodings).

### step 3
Create new folder, and move all the  "*_PlayerC.txt" files into it, along with the  "__txt_merger_002" than run that python code inside to create and "_merged.txt" file.
Remove other files and rename the "_merged.txt" to "Output2_merged_G_PlayerC.txt", as the 'Output2_' is used in the next steps code (it breakes  thecode if it's not changed!).
Move the "Output2_merged_G_PlayerC.txt" back with the rest of the text files.

### step 4
Remove all the "output_*" text files as they are not needed anymore.

### step 5
Now you have a technically all the files needed to use those files as a training dataset. Here is example of the inside structure of the text file:
DIA_DiegoNW_NeedHelp_WhoAreYou_15_00.wav|Who are you?

Here are following steps to clean it up and packaged it into more managabe format.

## Zip archive the audio
### step 6
Run the _dialogue_3_audios_001c.py to create a new text files "audiofiles_*", they will act as temporary anchor for the next script.

### step 7a
Run the _dialogue_4_zipManyFiles_006b.py, this code will use above "audiofiles_*" and dig thru the 'SPEECH' subfolder to add the wav files into new zip files named after the anchor text file inside new subfoder 'zipWavs'.

### step 7b
Remove the "audiofiles_*" text files.

### step 7c
Use some kind of batch rename program to change the name of  "output2_*.txt" files to just their filenames without the "output2_" (or dont if that doesn't bother you).
Move the edited text files into their own folder.


(you may want to run __txt_decoder_force_001.py one more time to see if everything is correct)

Save and do whatever you want with your dataset files.

