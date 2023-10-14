# Import libraries
from data_processing import SignalProcessing, SpectrumProcessing
from scipy.signal import butter, lfilter, freqz, hilbert
import matplotlib.pyplot as plt
import soundfile as sf
import numpy as np

# Class that retrieves the audio properties of a given audio file
class AudioProperties:
    """
    The <AudioProperties class> retrieves relevant audio data
    from the specified audio file/files.
    
    Call print(<object>) to print out audio properties.
    """
    def __init__(self, audio_file: str) -> None:
        # Assign attributes
        self.audio_file = audio_file
        self.data, self.Fs, self.samples, self.channels, self.duration, self.time = self.get_properties()

    # Method to get audio properties data
    def get_properties(self) -> tuple[np.ndarray, int, int, int, float, np.ndarray]:
        """
        Retrieves audio properties from audio file such as the samples, samplerate, duration, channels.
        """
        # Retrieve audio properties
        self.data, self.Fs = sf.read(self.audio_file)
        self.samples = len(self.data)
        self.duration = self.samples / self.Fs
        self.time = np.arange(self.samples) / self.samples * self.duration

        if len(self.data.shape) > 1:
            self.channels = self.data.shape[1]
        else:
            self.channels = 1

        return self.data, self.Fs, self.samples, self.channels, self.duration, self.time

    def __str__(self):
        # Return audio properties
        header = f"Audio Properties for '{self.audio_file}':"
        sample_rate = f" - Sample Rate (Fs): {self.Fs} Hz"
        samples = f" - Samples: {self.samples}"
        channels = f" - Channels: {self.channels}"
        duration = f" - Duration: {self.duration} seconds"
    
        return '\n'.join([header, sample_rate, samples, channels, duration])
    
    
class SignalAnalyzer:
    """
    The <SignalAnalyzer> class provides the functionality of calculating the frequency, amplitude and phase of a given signal. Additionally, a plotting method has been provided in order to visualize the result.
    
    Methods:
    - analyze() -> None: Call method to retrieve frequency, amplitude and phase.
    - plot() -> None: Call method to plot a given signal.
    """
    def __init__(self, audio_properties: AudioProperties) -> None:
        # Assign attributes
        self.signal_processor = SignalProcessing(audio_properties)
        self.data = audio_properties.data
        self.time = audio_properties.time
        
    def analyze_data(self) -> None:
        # Calculate the dft, frequency, amplitude and phase
        self.freq, self.amplitude, self.phase = self.signal_processor.analyze_data()
        
    def plot(self) -> None:
        # Plotting the amplitude vs time vs frequency and phase response
        plt.figure(figsize=(12, 12))
        plt.subplot(3, 1, 1)
        plt.plot(self.time, self.data)
        plt.title("Amplitude vs. Time")
        plt.xlabel("Time (s)")
        plt.ylabel("Amplitude")
        plt.grid()
        plt.subplot(3, 1, 2)
        plt.semilogx(self.freq, 20 * np.log10(self.amplitude))
        plt.title("Amplitude vs. Frequency")
        plt.xlabel("Frequency (Hz)")
        plt.ylabel("Amplitude (dB)")
        plt.grid()
        plt.subplot(3, 1, 3)
        plt.semilogx(self.freq, self.phase)  # np.degrees(phase)
        plt.title("Phase Response vs. Frequency")
        plt.xlabel("Frequency (Hz)")
        plt.ylabel("Phase (radians)")
        plt.grid()
        plt.tight_layout()
        plt.show()
        
class SpectrumAnalyzer:
    """
    The <SpectrumAnalyzer> class provides the functionality of calculating the frequency and envelope of a given signal. In addition, a lowpass filter, plotting and saving of filtered data method has been provided.
    
    Methods:
    - analyze() -> None: Call method to retrieve frequency, amplitude and phase.
    - plot() -> None: Call method to plot a given signal.
    """
    def __init__(self, audio_properties: AudioProperties) -> None:
        # Assign attributes
        self.spectrum_processing = SpectrumProcessing(audio_properties)
        self.data = audio_properties.data
        self.Fs = audio_properties.Fs
        
    def analyze_data(self, data) -> tuple[np.ndarray, np.ndarray]:
        freq, envelope = self.spectrum_processing.analyze_data(data)
        
        return freq, envelope
        
    def butter_lowpass_filter(self, cutoff, order = 5) -> list:
        filtered_data = self.spectrum_processing.butter_lowpass_filter(cutoff,order)
        
        return filtered_data
            
    def analyze_and_plot(self, data, cutoff):
        for i in range(len(cutoff)):
            # Calculate frequency and envelope, then plot it
            freq, envelope = self.analyze_data(data[i])
            self.plot(freq,envelope,f"Cutoff: {cutoff[i]} Hz")
        
    def plot(self,freq,envelope,title) -> None:
        # Plot the envelope spectrum
        plt.plot(freq, envelope)
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Envelope Amplitude')
        plt.title(f'Envelope Spectrum ({title})')
        plt.show()
        
        