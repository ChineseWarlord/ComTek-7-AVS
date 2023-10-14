# Import libraries
from scipy.signal import butter, lfilter, freqz, hilbert
import matplotlib.pyplot as plt
import typing as Tuple
import numpy as np

class SignalProcessing:
    def __init__(self, audio_properties) -> None:
        # Assign attributes
        self.audio_properties = audio_properties
           
    def analyze_data(self) -> tuple[np.ndarray, np.ndarray, np.ndarray | int]:
        # Extract relevant audio data from audio_properties
        data = self.audio_properties.data
        samples = self.audio_properties.samples
        Fs = self.audio_properties.Fs
        
        # Calculate the dft, frequency, amplitude and phase
        dft = np.fft.rfft(data, axis=0)
        freq = np.fft.rfftfreq(samples, d=1 / Fs)
        amplitude = np.abs(dft)
        phase = np.angle(dft)
        
        return freq, amplitude, phase
    
class SpectrumProcessing:
    def __init__(self, audio_properties) -> None:
        # Assign attributes
        self.audio_properties = audio_properties
        self.data = self.audio_properties.data
        self.Fs = self.audio_properties.Fs
        
    def analyze_data(self,data) -> tuple[np.ndarray, np.ndarray]:
        # Calculate the analytic signal using the Hilbert transform
        analytic_signal = hilbert(data)
        
        # Extract samples
        n = len(data)
        
        # Compute the magnitude of the analytic signal - for only positive values apply [:n//2]
        envelope = np.abs(analytic_signal)[:n//2]
        
        # Calculate the frequency axis - for only positive values apply [:n//2]
        freq = np.fft.fftfreq(n, 1/self.Fs)[:n//2]
        
        return freq, envelope
    
    def butter_lowpass_filter(self,cutoff: list[int],order) -> list:
        filtered_data = []
        for i in range(len(cutoff)):
            # Design Butterworth LP filter
            b, a = butter(order, cutoff[i], fs=self.Fs, btype='low', analog=False)
            
            # Apply filter to data
            filtered_data.append(lfilter(b, a, self.data))
        
        return filtered_data
            