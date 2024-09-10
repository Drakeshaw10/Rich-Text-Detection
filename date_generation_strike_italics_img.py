from PIL import Image, ImageDraw, ImageFont
import os

# Path to the input text file containing 800 words
input_file = "chunk_1.txt"
# input_file = "chunk_2.txt"
# input_file = "chunk_3.txt"
# input_file = "chunk_4.txt"
# input_file = "chunk_5.txt"

# Path to the output directory where images will be saved
output_dir = "strikethrough_italics_images/"

# Create the output directory if it does not exist
os.makedirs(output_dir, exist_ok=True)

# Load the input text file and read the words
with open(input_file, 'r') as file:
    words = file.read().split()

# font_path = "fonts/georgiai.ttf"
font_path = "fonts/helvetica_italic.ttf"
# font_path = "calibrii.ttf"
# font_path = "ariali.ttf"
# font_path = "timesi.ttf"

# Font settings
font_size = 36
font = ImageFont.truetype(font_path, font_size)

# Semantic design settings
bold = False
italic = True
strikethrough = True

# Create an image for each word
for i, word in enumerate(words):
    if i < 200:
        # Create a new image with white background
        image = Image.new('RGB', (400, 100), color='white')
        draw = ImageDraw.Draw(image)

        # Apply semantic designs
        if bold:
            font = ImageFont.truetype(font_path, font_size)
        if italic:
            font = ImageFont.truetype(font_path, font_size)

        # Get the size of the text
        bbox = draw.textbbox((0, 0), word, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        # Draw the word on the image
        text_x = (400 - text_width) // 2
        text_y = (100 - text_height) // 2
        draw.text((text_x, text_y), word, fill='black', font=font)

        # Draw strikethrough if specified
        if strikethrough:
            strike_y = text_y + text_height / 1.5 # Position the strikethrough line in the middle of the text height
            draw.line((text_x, strike_y, text_x + text_width, strike_y), fill='black', width=1)

        # Save the image as PNG
        image.save(f"{output_dir}image_{i+801}.png")  # Change extension to .jpg for JPG files
    else:
        break

print("Images created successfully.")
