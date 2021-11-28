# Singing Dalek
Turns your Dalek into a multi-talented carol singer. The basic voice is generated using eSpeak Text to Speech and then the Sox program is used to alter the pitch, volume and tempo to make it sound like the Dalek is attempting to sing.

## Pre-requisites
Python 3 should be installed. The program expects the eSpeak and Sox command line programs to be installed and available from the command line.

    sudo apt update
    sudo apt-get install sox
    sudo apt-get install espeak

## Usage
### As a Python Module
Import and use the module as per the module-test.py file:

    import singing_dalek as Dalek
    Dalek.sing('filename of song.csv')

### Command line

    python3 singing_dalek.py -i filename_of_song.csv

## Input file format
The program expects to read data from a four column CSV file. Each row in the CSV file corresponds to  a note/pause and/or a syllable.

The format of each column is as follows:
|Column 1 - note|Column 2 - duration|Column 3 - word| Column 4 - emphasis
|---|---|---|---|
Mandatory: A note from A to G. Optionally prefix with a '+' for every octave above middle C or '-' for each octave below e.g. ++A, C, -G.  Alternatively can be a 'P' to indicate a pause|Mandatory: the duration of the note or pause in terms of beats e.g. 0.5, 1, 1.5, 2 - will be treated as a float|Optional: the syllable or word sung on that note|Optional: using a > will raise the volume of that note and using a < will lower it.

Irrespective of whether a column is used on a particular row, all four columns must be specified e.g. 'P,2,,' is a valid row, whereas 'A+,1,we' is not, as it misses the fourth (empty) column.

### Example file extract
The following extract is the beginning of the chorus for 'Jingle Bells'

    B,1,jin,
    B,1,gell,
    B,1,bells,>
    P,1,,
    B,1,jin,
    B,1,gell,
    B,1,bells,>
    P,1,,
    B,1,jin,
    D,1,gell,>
    -G,1.5,all,
    A,0.5,the,
    B,2,whey,<
    P,2,,