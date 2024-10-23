from PIL import Image
import random

def swap_pixels(image, key):
    """
    Encrypts the image by swapping pixels randomly based on the key.
    """
    random.seed(key)
    pixels = list(image.getdata())
    width, height = image.size

    # Generate pairs of random indices to swap pixels
    for _ in range(len(pixels)):
        i = random.randint(0, len(pixels) - 1)
        j = random.randint(0, len(pixels) - 1)
        pixels[i], pixels[j] = pixels[j], pixels[i]

    encrypted_image = Image.new(image.mode, image.size)
    encrypted_image.putdata(pixels)
    return encrypted_image


def apply_operation(image, key, operation):
    """
    Encrypts the image by applying a mathematical operation to each pixel based on the key.
    Supported operations: 'add', 'xor'
    """
    pixels = list(image.getdata())
    width, height = image.size
    new_pixels = []

    for pixel in pixels:
        new_pixel = []
        for value in pixel:
            if operation == 'add':
                new_pixel.append((value + key) % 256)
            elif operation == 'xor':
                new_pixel.append(value ^ key)
        new_pixels.append(tuple(new_pixel))

    encrypted_image = Image.new(image.mode, image.size)
    encrypted_image.putdata(new_pixels)
    return encrypted_image


def main():
    print("Image Encryption Tool")
    image_path = input("Enter the path of the image: ")
    key = int(input("Enter a numeric key for encryption: "))
    
    # Open the image
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Error opening image: {e}")
        return

    print("Choose an encryption operation:")
    print("1. Swap pixels")
    print("2. Apply mathematical operation (add or XOR)")
    
    choice = input("Enter your choice (1/2): ")
    
    if choice == '1':
        encrypted_image = swap_pixels(image, key)
        encrypted_image.save("encrypted_image_swap.png")
        print("Image encrypted using pixel swapping. Saved as 'encrypted_image_swap.png'.")
    
    elif choice == '2':
        operation = input("Enter the operation (add/xor): ")
        if operation not in ['add', 'xor']:
            print("Invalid operation. Please choose either 'add' or 'xor'.")
            return
        encrypted_image = apply_operation(image, key, operation)
        encrypted_image.save(f"encrypted_image_{operation}.png")
        print(f"Image encrypted using {operation}. Saved as 'encrypted_image_{operation}.png'.")
    
    else:
        print("Invalid choice. Exiting.")


if __name__ == "__main__":
    main()