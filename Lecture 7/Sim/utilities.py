import soundfile as sf
import numpy as np

class AudioIOUtility:
    """
    Audio IU utility class
    """
    @staticmethod
    def save_audio(filename: str, output: str, data: np.float64, fs: int, FORMAT: str) -> None:
      """
      Save an audio signal to an audio file.
      
      Parameters:
      -----------
      - filesNo: Number of files to be created.
      - filename: Name of the output audio file.
      - output: Output path for the saved audio.
      - data: The audio signal data to be saved.
      - fs: The sample rate of the audio data.
      - format: The format of the saved audio (e.g. wav, mp3)
      """ 
      try:
          sf.write(str(f"{output}{filename}.{FORMAT}"), data, samplerate=fs)
          print(f"Audio successfully saved as {filename}.{FORMAT}")
      except Exception as e:
          print(f"Error: {e}")