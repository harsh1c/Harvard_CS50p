import sys
import os
from PIL import Image, ImageOps

def main():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    else:
        input_image = sys.argv[1].lower()
        file_name1,extention_name1 = input_image.split(".")

        output_image = sys.argv[2].lower()
        file_name2,extention_name2 = output_image.split(".")

        if not input_image.endswith((".jpg",".jpeg",".png")) :
            sys.exit("Not a image file")
        elif not output_image.endswith((".jpg",".jpeg",".png")) :
            sys.exit("Not a image file")
        elif extention_name1 != extention_name2:
            sys.exit("Not the same extention file")
        elif not(os.path.exists(input_image)):
            sys.exit("File does not exist")
        else:
            edit(input_image , output_image)

def edit(input_image , output_image):
    shirt = Image.open("shirt.png")



    with Image.open(input_image) as im1:

        with Image.open(input_image) as im1:
            resized_image = ImageOps.fit(im1, shirt.size)

            # Create a new image with the same size as the shirt image
            combined = Image.new("RGBA", shirt.size)

            # Paste the resized input image onto the combined image
            combined.paste(resized_image, (0, 0))

            # Paste the shirt image on top of the combined image
            combined.paste(shirt, (0, 0), shirt)

            # Convert to RGB if saving as JPEG
            if output_image.lower().endswith(".jpg") or output_image.lower().endswith(".jpeg"):
                combined = combined.convert("RGB")

            combined.save(output_image)
main()