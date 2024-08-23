from PIL import Image, ImageSequence
import numpy as np

def remove_background(input_path, output_path):
    gif = Image.open(input_path)
    frames = []

    for frame in ImageSequence.Iterator(gif):
        frame = frame.convert("RGBA")
        datas = np.array(frame)

        # Define the background color range
        lower_bound = np.array([30, 30, 30, 255])
        upper_bound = np.array([100, 100, 100, 255])

        # Create a mask for the background
        mask = np.all((datas >= lower_bound) & (datas <= upper_bound), axis=-1)

        # Set the background pixels to transparent
        datas[mask] = [255, 255, 255, 0]

        new_frame = Image.fromarray(datas, 'RGBA')
        frames.append(new_frame)

    # Ensure all frames have the same size and alignment
    max_width = max(frame.width for frame in frames)
    max_height = max(frame.height for frame in frames)
    aligned_frames = []

    for frame in frames:
        aligned_frame = Image.new("RGBA", (max_width, max_height), (255, 255, 255, 0))
        aligned_frame.paste(frame, (0, 0))
        aligned_frames.append(aligned_frame)

    aligned_frames[0].save(output_path, save_all=True, append_images=aligned_frames[1:], loop=0, optimize=False, quality=95)

input_path = r"C:\Projects\boy\pygame_game\smore_game\images\fire_scaled.gif"
output_path = r"C:\Projects\boy\pygame_game\smore_game\images\fire.gif"
remove_background(input_path, output_path)