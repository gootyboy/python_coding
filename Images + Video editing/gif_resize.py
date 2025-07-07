from PIL import Image, ImageSequence

def resize_gif(input_path, output_path, scale):
    with Image.open(input_path) as img:
        frames = []
        for frame in ImageSequence.Iterator(img):
            frame = frame.convert("RGBA")
            new_size = (int(frame.width * scale), int(frame.height * scale))
            resized_frame = frame.resize(new_size, Image.LANCZOS)
            # Create a new blank image with the same size as the resized frame
            new_frame = Image.new("RGBA", resized_frame.size)
            new_frame.paste(resized_frame, (0, 0), resized_frame)
            frames.append(new_frame)

        frames[0].save(output_path, save_all=True, append_images=frames[1:], loop=0, disposal=2)

input_path = r"C:\Projects\boy\pygame_game\adventure_game\images\star.gif"
output_path = r"C:\Projects\boy\pygame_game\adventure_game\images\star.gif"

scale = 0.50

resize_gif(input_path, output_path, scale)