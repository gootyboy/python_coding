from PIL import Image, ImageFilter

img = Image.open("your_image.png") # Change this name to the name of the png file you want to blur

# Define your custom blur radius (e.g., 5 for a mild blur)
custom_radius = 8
blurred_image = img.filter(ImageFilter.GaussianBlur(radius=custom_radius))

blurred_image.save("blurred_image.png") #change the name to what name you want for the blurred image
