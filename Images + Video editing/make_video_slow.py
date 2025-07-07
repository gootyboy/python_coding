import cv2
from pydub import AudioSegment
import subprocess

# Define the input and output paths
input_path = r"/Users/gootyboy/Desktop/myrepos/python_coding/pygame_game/mini_movie/images/IMG_0542.MOV"
output_path = r"/Users/gootyboy/Desktop/myrepos/python_coding/pygame_game/mini_movie/images/A1.MOV"

# Load the video
cap = cv2.VideoCapture(input_path)

# Get the frames per second (fps) of the original video
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Define the codec and create a VideoWriter object for .MOV format
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 'mp4v' works well for .MOV format
out = cv2.VideoWriter(output_path, fourcc, fps / 2, (int(cap.get(3)), int(cap.get(4))))

# Process video frames
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    out.write(frame)

cap.release()
out.release()
cv2.destroyAllWindows()

# Slow down the audio
audio = AudioSegment.from_file(input_path)
slow_audio = audio._spawn(audio.raw_data, overrides={"frame_rate": int(audio.frame_rate / 2)})

# Create a silent audio track with the same duration as the slow_audio
silent_audio = AudioSegment.silent(duration=len(slow_audio))

# Export the silent audio
silent_audio.export("silent_audio.wav", format="wav")

# Use ffmpeg to merge the slow-motion video with the silent audio
subprocess.call([
    'ffmpeg', '-i', output_path, '-i', 'silent_audio.wav', '-c:v', 'copy', '-c:a', 'aac', '-strict', 'experimental', output_path
])