import numpy as np
from scipy.io import wavfile
from scipy.signal import resample

# Parameters
mic_distance = 0.2  # Distance between microphones (in meters)
angle = np.radians(45)  # Assume the sound source is at a 45-degree angle (adjust as needed)
temperature = 20  # Temperature in Celsius
sound_speed = 331.5 + 0.61 * temperature  # Speed of sound (m/s) based on temperature

# Calculate time delay
delay_time = mic_distance * np.cos(angle) / sound_speed  # Delay time in seconds

# Read audio files (assuming two audio files: mic1.wav and mic2.wav)
sample_rate1, mic1_signal = wavfile.read("mic1.wav")
sample_rate2, mic2_signal = wavfile.read("mic2.wav")

# Ensure the sample rates are the same
assert sample_rate1 == sample_rate2, "Sample rates of the two audio files do not match."
sample_rate = sample_rate1

# Convert delay time to number of samples
delay_samples = int(delay_time * sample_rate)

# Apply delay to the signal from mic2
mic2_signal_delayed = np.pad(mic2_signal, (delay_samples, 0), 'constant')[:len(mic1_signal)]

# Combine signals to implement beam forming
beamformed_signal = mic1_signal + mic2_signal_delayed

# Output the beam formed audio
wavfile.write("beam_formed_output.wav", sample_rate, beamformed_signal.astype(np.int16))

print("Beam forming completed. Output saved as 'beam_formed_output.wav'")
