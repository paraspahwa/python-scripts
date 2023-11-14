# Process images using the Pillow library

from PIL import Image

# Open an image file
image = Image.open('example.jpg')

# Resize the image
resized_image = image.resize((300, 200))

# Save the resized image
resized_image.save('resized_example.jpg')

print("Image processing completed.")
