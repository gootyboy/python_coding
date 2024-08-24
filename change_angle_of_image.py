from PIL import Image

def change_angle(angle, ipnut_path, output_path):
    Image.open(ipnut_path).rotate(angle).save(output_path)
     
change_angle(-45, r"C:\Projects\boy\pygame_game\smore_game\images\cracker.png", r"C:\Projects\boy\pygame_game\smore_game\images\gfh.png")