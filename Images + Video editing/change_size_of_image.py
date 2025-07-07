from PIL import Image

def resize_image(width, height, org_path, new_path):
    with Image.open(org_path) as image:
        resized_img = image.resize((width, height))
        resized_img.save(new_path)

resize_image