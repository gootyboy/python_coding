from PIL import Image, ImageSequence
import numpy as np

def remove_white_background(image_path, output_path, threshold=200):
    # Open the GIF
    gif = Image.open(image_path)
    frames = []

    for frame in ImageSequence.Iterator(gif):
        frame = frame.convert("RGBA")
        data = np.array(frame)

        # Replace white-ish background with transparency
        r, g, b, a = data.T
        white_areas = (r > threshold) & (g > threshold) & (b > threshold)
        data[white_areas.T] = (0, 0, 0, 0)  # Set to transparent

        new_frame = Image.fromarray(data)
        frames.append(new_frame)

    # Save the modified frames as a new GIF
    frames[0].save(output_path, save_all=True, append_images=frames[1:], loop=0, disposal=2)

# Example usage
input_path = r"C:\Projects\boy\pygame_game\adventure_game\images\star.gif"
output_path = r"C:\Projects\boy\pygame_game\adventure_game\images\star_2.gif"
remove_white_background(input_path, output_path)