from PIL import Image, ImageOps

def mirror_image(image_path, output_path):
    image = Image.open(image_path)
    mirrored_image = ImageOps.mirror(image)
    mirrored_image.save(output_path)

mirror_image(r'C:\Projects\boy\pygame_game\adventure_game\images\hedgehog_right.png', r'C:\Projects\boy\pygame_game\adventure_game\images\hedgehog_left.png')