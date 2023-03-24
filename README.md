# Gothic-Dialogue-Process-dataset
an semi automatic process of reusing the decomiled audio files and dialogue scripts from Gothic game to convert them into an usable audio dataset.

@title TEST
There are ultiple python files.

First use the tools GothicSourcerV3_14 to decompile gothic.dat to gain the dialogue script .d files and GothicVDFS to extract dialogue from the speech.VDF files. Place the .d files in 'Dialoge' subfolder and audio files in 'SPEECH' subfolder.

Copy the python files into the main folder.

place the '_dialogue_1_seperator_005a' in the 



###########################################################


use the files "audiofiles_" with the script "__duplicateFiles" to copy the wav files from a folder A to a folder B.

    _dialogue_1_seperator_005a.py
strips the entire script from non-dialogue lines to the "output_" text file, as well as form at it for better future audio training 
(it may require further text file edition to get format working with whatever file processing you wish to use) example here:

DIA_DiegoOw_Hallo_11_00.wav|Hey, I thought you were dead.
DIA_DiegoOw_Hallo_15_01.wav|Yes ... so I was.

    _dialogue_2_divider_002a.py
takes the above files, and split them between the dialogue lines of Player Character and the NPC:

output2_DIA_PC_ThiefOW_div_PC:
DIA_DiegoOw_Hallo_11_00.wav|Hey, I thought you were dead.

audiofiles_PC_ThiefOW_div_PC.txt:
DIA_DiegoOw_Hallo_15_01.wav|Yes ... so I was.

    _dialogue_3_audios_001b.py
takes the above files, and removes all the elements not referencing the .wav file, so it can be easier used with the __duplicateFiles.py code

