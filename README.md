# midi2str
A crappy tool to convert your MIDI files to notes-length pair

## Limitation of this tool
This tool can only convert a MIDI file (preferably single track, multi-track midi files are not tested) that has no chords, polyphony or any notes stacked on each other.

## What does this do?
As stated in the description, this tool will convert your MIDI files to a notes-length pair and prints it in json, you can also preview the sound (if you don't mind listening to sine waves)

The notes will be expressed as MIDI Notes (E.g. A4 = 69, B4 = 70, etc..), lengths will be expressed in ms.

## Usage
`midi2str.py midi_file [BPM] [Octave_shift]`

`midi_file` --> Required. Path to the MIDI file to be converted

`[BPM]` --> Optional. Manually specify BPM. This overrides the automatic BPM detection logic

`[Octave_shift]` --> Optional. Shift how many octaves (E.g. 1 will shift the notes by +1 octave, -1 will shift the notes by -1 octave)

## Example:
```
C:\Users\usr\Repository\midi2str>py readmsg.py ex1.mid
MIDI File: ex1.mid, BPM: 85
Preview sound using:
    WinSound API's beep (type 'win')
    Generate a waveform and playing it (type 'wav')
    Don't preview (type 'n')
Preview with [win]/wav/n? n
Generating Note and Length pair
|████████████████████████████████████████| 51/51 [100%] in 0.1s (441.48/s) 0s (0.0/s, eta: -)
Note and length generation complete
|████████████████████████████████████████| 30/30 [100%] in 0.1s (285.15/s) 0s (0.0/s, eta: -)
MIDI note to frequency conversion complete
{"notes":[96,0,95,96,91,0,95,96,103,0,101,100,96,0,98,100,0,103,0,98,0,96,98,96,96,95,91,96,98,95],"notes_length":[353,353,353,353,353,706,176,176,353,353,353,353,353,353,706,353,353,353,353,353,706,176,176,706,353,353,353,353,353,353]}
Press Enter to exit...

C:\Users\usr\Repository\midi2str>▃
```

```
C:\Users\usr\Repository\midi2str>py readmsg.py ex2.mid 84 1
BPM overrided: 84
Notes will be shifted by 1.0 octave
MIDI File: ex2.mid, BPM: 84
Preview sound using:
    WinSound API's beep (type 'win')
    Generate a waveform and playing it (type 'wav')
    Don't preview (type 'n')
Preview with [win]/wav/n? n
Generating Note and Length pair
|████████████████████████████████████████| 785/785 [100%] in 0.0s (37688.77/s)s (392481.7/s, eta: 0s)
Note and length generation complete
|████████████████████████████████████████| 446/446 [100%] in 0.0s (16476.21/s)s (315936.4/s, eta: 0s)
MIDI note to frequency conversion complete
{"notes":[76,79,12,76,79,12,78,74,12,76,79,12,78,79,12,76,72,71,12,69,69,69,69,72,71,71,71,12,76,71,12,69,69,69,69,72,72,71,71,12,72,72,72,71,74,72,71,74,72,12,72,72,72,72,78,78,79,79,78,12,76,12,79,81,79,78,78,78,79,78,76,76,12,79,81,79,78,78,78,79,78,76,76,12,79,81,79,78,78,78,78,79,78,76,83,83,81,81,81,79,79,78,79,78,76,76,12,79,81,79,78,78,78,79,78,76,76,12,79,81,79,78,78,78,79,78,76,76,12,79,81,79,78,78,78,78,79,78,76,83,83,81,81,81,79,79,78,79,78,76,76,79,12,76,12,78,74,12,76,12,76,79,12,78,79,12,79,78,76,74,76,12,79,78,76,74,76,12,78,76,74,71,74,12,76,12,76,79,12,76,79,12,76,76,79,78,12,78,76,74,71,74,12,76,79,12,76,71,71,12,69,69,69,72,71,71,71,12,76,71,12,69,69,69,72,71,71,71,12,69,72,72,72,71,74,72,71,74,72,12,71,74,74,74,74,74,74,74,79,81,79,78,12,76,12,79,81,79,78,78,78,79,78,76,76,12,79,81,79,78,78,78,79,78,76,76,12,79,81,79,78,78,78,78,79,78,76,83,83,81,81,81,79,79,78,79,78,76,76,12,79,81,79,78,78,78,79,78,76,76,12,79,81,79,78,78,78,79,78,76,76,12,79,81,79,78,78,78,78,79,78,76,83,83,81,81,81,79,79,78,79,78,76,76,12,76,12,76,12,76,12,76,12,76,12,76,12,79,81,79,78,78,78,79,78,76,76,12,79,81,79,78,78,78,79,78,76,76,12,79,81,79,78,78,78,78,79,78,76,83,83,81,81,81,79,79,78,79,78,76,76,12,79,81,79,78,78,78,79,78,76,76,12,79,81,79,78,78,78,79,78,76,76,12,79,81,79,78,78,78,78,79,78,76,83,83,81,81,81,79,79,78,79,78,76,76],"notes_length":[179,357,2321,179,357,2321,179,714,1964,179,357,893,179,893,23214,357,357,357,179,179,179,179,179,179,179,179,357,357,357,357,179,179,179,179,179,179,179,179,357,357,179,179,357,179,357,357,179,357,357,357,179,179,357,179,357,357,179,179,357,179,179,179,179,179,357,357,179,357,179,357,357,179,179,179,179,357,357,179,357,179,357,357,179,179,179,179,179,357,179,179,357,179,357,357,179,357,179,357,179,179,357,357,179,357,179,179,179,179,179,357,357,179,357,179,357,357,179,179,179,179,357,357,179,357,179,357,357,179,179,179,179,179,357,179,179,357,179,357,357,179,357,179,357,179,179,357,357,179,357,179,179,357,893,179,1250,179,893,357,179,1250,179,357,893,179,714,3393,179,179,179,179,179,179,179,179,179,179,179,893,179,179,179,179,357,357,179,1250,179,357,179,179,357,179,179,0,357,179,714,179,179,179,179,357,357,179,714,536,357,357,536,179,179,179,179,179,179,179,357,357,357,357,357,179,179,179,179,179,179,357,179,179,179,179,357,179,357,357,179,357,357,179,179,179,179,357,179,179,179,179,179,179,357,179,179,179,179,179,179,357,357,179,357,179,357,357,179,179,179,179,357,357,179,357,179,357,357,179,179,179,179,179,357,179,179,357,179,357,357,179,357,179,357,179,179,357,357,179,357,179,179,179,179,179,357,357,179,357,179,357,357,179,179,179,179,357,357,179,357,179,357,357,179,179,179,179,179,357,179,179,357,179,357,357,179,357,179,357,179,179,357,357,179,357,179,179,2679,179,2679,179,5536,179,2679,179,2679,179,16964,179,179,179,179,357,357,179,357,179,357,357,179,179,179,179,357,357,179,357,179,357,357,179,179,179,179,179,357,179,179,357,179,357,357,179,357,179,357,179,179,357,357,179,357,179,179,179,179,179,357,357,179,357,179,357,357,179,179,179,179,357,357,179,357,179,357,357,179,179,179,179,179,357,179,179,357,179,357,357,179,357,179,357,179,179,357,357,179,357,179,179]}
Press Enter to exit...

C:\Users\usr\Repository\midi2str>▃
```

## Dependencies
Third-party libraries: `alive_progress` (PyPi), `mido` (PyPi), `wav_create` (included, special thanks to this [stackoverflow response](https://stackoverflow.com/questions/33879523/python-how-can-i-generate-a-wav-file-with-beeps)

Built-in libraries: `copy`, `time`, `winsound` **(Windows Only)**, `os`, `sys`

wav_create: built-in libraries: `math`, `wave`, `struct`. Third-party libraries: `alive_progress` (PyPi)
