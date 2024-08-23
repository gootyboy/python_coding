from PIL import Image, ImageSequence

def resize_gif(input_path, output_path, scale):
    gif = Image.open(input_path)
    frames = []

    for frame in ImageSequence.Iterator(gif):
        frame = frame.convert("RGBA")
        new_size = (int(frame.width * scale), int(frame.height * scale))
        resized_frame = frame.resize(new_size, Image.LANCZOS)
        frames.append(resized_frame)

    frames[0].save(output_path, save_all=True, append_images=frames[1:], loop=0, optimize=True)


input_path = r"C:\Projects\boy\pygame_game\smore_game\images\fire_ORG.gif"
output_path = r"C:\Projects\boy\pygame_game\smore_game\images\fire_scaled.gif"
scale = 0.75  # Scale down to 75%
resize_gif(input_path, output_path, scale)