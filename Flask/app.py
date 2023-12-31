from PIL import Image, ImageDraw, ImageFont

def process_image(image_file):
    # Open the image
    image = Image.open(image_file)

    # Create an ImageDraw object
    draw = ImageDraw.Draw(image)

    # Choose a font and font size
    font_path = '/path/to/font.ttf'  # Replace with the actual path to your font file
    font_size = 36
    font = ImageFont.truetype(font_path, font_size)

    # Get the size of the text
    text = 'My Poster'
    text_width, text_height = draw.textsize(text, font=font)

    # Calculate the x and y coordinates for the text
    x = (image.width - text_width) / 2
    y = (image.height - text_height) / 2

    # Set the text color
    color = (0, 0, 0)

    # Draw the text on the image
    draw.text((x, y), text, font=font, fill=color)

    # Save the image
    output_image_path = '/path/to/output_image.png'  # Replace with the desired output image path
    image.save(output_image_path)
