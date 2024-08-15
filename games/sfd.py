from PIL import Image, ImageDraw

def draw_chessboard(size=8, square_size=50):
    # Create a new image with white background
    img = Image.new("RGB", (size * square_size, size * square_size), "white")
    draw = ImageDraw.Draw(img)

    # Draw the squares
    for row in range(size):
        for col in range(size):
            if (row + col) % 2 == 0:
                fill = "white"
            else:
                fill = "black"
            draw.rectangle(
                [col * square_size, row * square_size, (col + 1) * square_size, (row + 1) * square_size],
                fill=fill
            )

    # Save the image
    img.save("chessboard.png")

draw_chessboard()