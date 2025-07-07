from PIL import Image, ImageOps

def mirror_image(image_path, output_path):
    image = Image.open(image_path)
    mirrored_image = ImageOps.mirror(image)
    mirrored_image.save(output_path)