# Beamforming Experiment

Author: Mux

## What is Beamforming?

Beamforming is a signal processing technique used with arrays of microphones to enhance or suppress sounds coming from specific directions. By adjusting for the time delays between signals captured by different microphones, it is possible to amplify the sound from a particular direction while reducing noise from others. This experiment demonstrates a simple Delay-and-Sum beamforming algorithm.

## Code Dependencies
* Audacity - for audio recording and editing
* Poetry - to set up the Python environment
* Experiment Text - provided by the school

## Experiment Steps

1. **Setup Microphones and Record Audio**:
   - Place microphones according to the experimental setup in the provided text.
   - Record audio for each microphone (e.g., using Audacity).

2. **Data Preprocessing**:
   - Ensure recordings are saved as WAV files.
   - Make sure both files have the same sample rate.

3. **Run the Beam forming Code**:
   - Adjust the parameters in `beamforming.py` based on your setup.
   - Execute the script to process the audio files.

4. **Check the Result**:
   - Listen to the output file `beamformed_output.wav` and compare it to the original recordings.
