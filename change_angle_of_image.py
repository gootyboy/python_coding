from PIL import Image

def change_angle(angle, ipnut_path, output_path):
    Image.open(ipnut_path).rotate(angle).save(output_path)
