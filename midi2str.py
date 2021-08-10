import copy
import mido
import time
import winsound
import wav_create
import os
import sys
from alive_progress import alive_bar

# Generating note list and length list from MIDI

def tick2time(bpm, tick):
    '''Calculating note sustain time based on BPM (returns ms)'''
    t = 60*1000/bpm  # 拍时
    return round(tick/mid.ticks_per_beat*t)

def midi2hz(midi, octave_shift=0):
    # http://www.phys.unsw.edu.au/jw/notes.html
    # Based on fm = 440 * 2^((m-69)/12)
    # fm is frequency, m is midi number (i.e. A4: fm = 440 Hz, m = 69)
    # Note: octave can be shifted, this is useful when dealing with certain MIDI files, whose base octave is 4 (i.e. C4, D4, E4...) for some reason
    # The updated formula (written in Python) is: 440 * 2**((midi+(12*octave_shift)-69)/12)
    # Written the other way: fm = 440 * 2^((m-69)/12)
    frequency = 440 * 2**((midi+(12*octave_shift)-69)/12)
    # Nice.
    return frequency

def GenerateNoteLengthPairFromMIDI():
    print("Generating Note and Length pair")
    msg_total = 0 # Just calculating how many MIDI messages there are to workout the progress bar
    for i in mid.tracks: 
        for j in range(len(i)): msg_total += 1
    
    with alive_bar(msg_total) as bar:
        for track_n, track in enumerate(mid.tracks): # Iterate each MIDI tracks
            #print("----- Track {} -----".format(track_n))
            for msg in track: # Iterate every message in a track
                #if msg.type == "note_on" or msg.type == "note_off": print("Event {}: ".format(i), end="")
                if msg.type == "note_on": # Records what note is triggered
                    if msg.time != 0:
                        #print("added space: {}ms".format(tick2time(bpm, msg.time)))
                        note_list.append(0)
                        note_length.append(tick2time(bpm, msg.time))
                    #print("Note On: note {}, since last {} ms ({} ticks)".format(msg.note, tick2time(bpm, msg.time), msg.time))
                    note_list.append(msg.note)
                elif msg.type == "note_off": # Records how long the note was pressed, note: https://mido.readthedocs.io/en/latest/midi_files.html#tempo-and-beat-resolution
                    #print("Note Off: note {}, since last {} ms ({} ticks)".format(msg.note, tick2time(bpm, msg.time), msg.time))
                    note_length.append(tick2time(bpm, msg.time))
                bar()
    print("Note and length generation complete")

def ConvertMIDINotesToFrequency(octave_shift):
    with alive_bar(len(note_list)) as bar:
        for i in range(len(note_list)):
            if note_list[i] != 0:
                note_list[i] = midi2hz(note_list[i], octave_shift)
            bar()
    print("MIDI note to frequency conversion complete")

## Now let's try playing it

def PlayWinSound():
    for sound, length in zip(note_list, note_length):
        if sound == 0:
            print("No notes for {}ms".format(length))
            time.sleep(length / 1000) # ms to s
            continue
        print("Playing {}hz for {}ms".format(int(sound), length))
        winsound.Beep(int(sound), length)

def GenWaveForm():
    if not os.path.isfile(file_name + ".wav"):
        print("Generating data for waveform...")
        with alive_bar(len(note_list)) as bar:
            for sound, length in zip(note_list, note_length):
                wav_create.append_sinewave(sound, length, 0.25)
                bar()

        print("Rendering waveform to {}.wav".format(file_name))
        wav_create.save_wav(file_name + ".wav")

        print("Create successful, now playing...")
    else:
        print("A pre-generated file was found, now playing...")

    winsound.PlaySound(file_name + ".wav", winsound.SND_ASYNC)

    for sound, length in zip(note_list, note_length):
        if sound == 0:
            print("No notes for {}ms".format(length))
            time.sleep(length / 1000) # ms to s
            continue
        print("Playing {}hz for {}ms".format(int(sound), length))
        time.sleep(length / 1000)

def EncodeAndOutputNotes():
    import json
    dat = {"notes": note_list_midi, "notes_length": note_length}
    dat = json.dumps(dat, separators=(',', ':'))
    return dat

#PlayWinSound()
#GenWaveForm()

if __name__ == '__main__':
    try:
        if not os.path.isfile(sys.argv[1]): raise Exception()
        file_name = sys.argv[1]
    except:
        print("Usage: %s midi_file_name [tempo in BPM] [Octave]" % sys.argv[0])
        sys.exit(-255)

    mid = mido.MidiFile(file_name)
    bpm = None
    # Autodetecting BPM:
    for msg in mid:
        if msg.type == "set_tempo":
            bpm = int(mido.tempo2bpm(msg.tempo))
    if bpm == None:
        try:
            bpm = int(sys.argv[2])
        except: bpm = int(input("Unable to detect BPM. Please enter BPM manually: "))
    try:
        bpm = int(sys.argv[2])
        print("BPM overrided:", bpm)
    except ValueError:
        print("Error: invalid BPM override")
        sys.exit(-255)
    except:
        pass

    try:
        octave_shift = float(sys.argv[3])
        print("Notes will be shifted by {} octave".format(octave_shift))
    except ValueError:
        print("Error: invalid octave shift: {}".format(sys.argv[3]))
        sys.exit(-255)
    except:
        octave_shift = 0

    print("MIDI File: {}, BPM: {}".format(file_name, bpm))

    note_list = [] # In MIDI 'note'
    note_length = [] # In miliseconds

    u_input = input("Preview sound using:\n    WinSound API's beep (type 'win')\n    Generate a waveform and playing it (type 'wav')\n    Don't preview (type 'n')\nPreview with [win]/wav/n? ")
    GenerateNoteLengthPairFromMIDI()
    note_list_midi = copy.deepcopy(note_list)
    for i in range(len(note_list_midi)):
        note_list_midi[i] = int(note_list_midi[i] + octave_shift*12) # Shifting octaves for notes in MIDI
    ConvertMIDINotesToFrequency(octave_shift)

    encoded = EncodeAndOutputNotes()
    print(encoded)

    if u_input.upper() == "WAV":
        GenWaveForm()
    elif u_input.upper() == "N":
        pass
    else:
        PlayWinSound()
    
    try:
        input("Press Enter to exit...")
    except KeyboardInterrupt:
        sys.exit(0)