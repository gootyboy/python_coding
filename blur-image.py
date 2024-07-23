from PIL import Image, ImageFilter
Image.open("stage.png").filter(ImageFilter.GaussianBlur(radius= 8)).save("stage-blurred.png")