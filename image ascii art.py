from PIL import Image
import os

ASCII_CHARS = "@#S%?*+;:,. "

def resize_image(image, new_width=100):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width * 0.55)
    return image.resize((new_width, new_height))

def grayify(image):
    return image.convert("L")

def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = "".join([ASCII_CHARS[pixel * len(ASCII_CHARS) // 256] for pixel in pixels])
    return ascii_str

def image_to_ascii(image_path, new_width=100):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Unable to open image file: {image_path}. Error: {e}")
        return

    image = resize_image(image, new_width)
    image = grayify(image)
    ascii_str = pixels_to_ascii(image)

    img_width = image.width
    ascii_img = "\n".join(ascii_str[i:(i + img_width)] for i in range(0, len(ascii_str), img_width))
    
    print("\n" + ascii_img)

def main():
    image_path = input("Enter the path to the image file: ").strip()
    if not os.path.isfile(image_path):
        print("File not found. Please check the path and try again.")
        input("\nPress Enter to exit...")
        return

    try:
        new_width = int(input("Enter the new width (default is 100): ") or 100)
    except ValueError:
        print("Invalid width. Using default value of 100.")
        new_width = 100

    image_to_ascii(image_path, new_width)
    
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()