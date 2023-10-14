from audio_analysis import AudioProperties, SignalAnalyzer, SpectrumAnalyzer
from utilities import AudioIOUtility

def signal_analyzing(audio_properties):
    signal_analyzer = SignalAnalyzer(audio_properties)
    signal_analyzer.analyze_data()
    signal_analyzer.plot()
    
def spectrum_analyzing(audio_properties, cutoff_freqs):
    spectrum_analyzer = SpectrumAnalyzer(audio_properties)
    freq, envelope = spectrum_analyzer.analyze_data(spectrum_analyzer.data)
    spectrum_analyzer.plot(freq, envelope, "Original")
    filtered_data = spectrum_analyzer.butter_lowpass_filter(cutoff_freqs)
    spectrum_analyzer.analyze_and_plot(filtered_data, cutoff_freqs)
    
    return filtered_data
    
def save_filtered_data(filtered_data, filename, output, cutoff, format):
    audioIO = AudioIOUtility()
    for i in range(len(filtered_data)):
        audioIO.save_audio(f"{filename}{cutoff[i]}", output, filtered_data[i], 48000, format)
 
if __name__ == "__main__":
    # Data paths
    audio_file_1 = "Recordings/danish_recording.mp3"
    audio_file_2 = "Recordings/vikki_greek.mp3"
    path_output = "Filtered Recordings/"
    audio_files = [audio_file_1, audio_file_2]
    
    filtered_data = []
    cutoff_freqs = [20000,15000,10000,8000,6000,4000,2000,1000]
    for audio in audio_files:
        # Instantiate audio properties class
        audio_properties = AudioProperties(audio)
        print(audio_properties)
        
        # Analyze signals
        signal_analyzing(audio_properties)
        
        # Analyze signal spectrums
        filtered_data.append(spectrum_analyzing(audio_properties, cutoff_freqs))

    # Save each filtered data at different cutoffs
    save_filtered_data(filtered_data[0], "filtered_simon_", path_output, cutoff_freqs, "wav")
    save_filtered_data(filtered_data[1], "filtered_vikki_", path_output, cutoff_freqs, "wav")
        
        