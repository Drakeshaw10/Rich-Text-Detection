from PIL import Image, ImageDraw, ImageFont
import textwrap
import os

# Path to the input text file containing 800 words
input_file = "chunk_5.txt"

# Path to the output directory where images will be saved
output_dir = "normal_images/"

# Create the output directory if it does not exist
os.makedirs(output_dir, exist_ok=True)

# Load the input text file and read the words
with open(input_file, 'r') as file:
    words = file.read().split()


font_path = "fonts\helvetica.ttf"

# Font settings
font_size = 36
font = ImageFont.truetype(font_path, font_size)

# Semantic design settings
bold = False
italic = True

# Create an image for each word
for i, word in enumerate(words):
    # Create a new image with white background
    image = Image.new('RGB', (400, 100), color='white')
    draw = ImageDraw.Draw(image)

    # Apply semantic designs
    if bold:
        font = ImageFont.truetype(font_path, font_size)
    if italic:
        font = ImageFont.truetype(font_path, font_size)

    # Get the size of the text
    text_height = font_size
    text_width = len(word)*10

    # Draw the word on the image
    draw.text(((400 - text_width) // 2, (100 - text_height) // 2), word, fill='black', font=font)

    # Save the image as PNG/JPG
    image.save(f"{output_dir}image_{i+3201}.png")  # Change extension to .jpg for JPG files

print("Images created successfully.")