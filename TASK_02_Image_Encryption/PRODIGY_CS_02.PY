from PIL import Image
import numpy as np

def encrypt_image(input_path, output_path):
    image = Image.open(input_path)
    pixels = np.array(image)
    encrypted_pixels = (pixels + 50) % 256  # Example of a simple encryption
    encrypted_image = Image.fromarray(encrypted_pixels.astype(np.uint8))
    encrypted_image.save(output_path)
    print(f"Image saved to {output_path}")

def decrypt_image(input_path, output_path):
    image = Image.open(input_path)
    pixels = np.array(image)
    decrypted_pixels = (pixels - 50) % 256
    decrypted_image = Image.fromarray(decrypted_pixels.astype(np.uint8))
    decrypted_image.save(output_path)
    print(f"Image saved to {output_path}")

if __name__ == "__main__":
    print("Image Encryption Tool")
    choice = input("Choose an option: (1) Encrypt (2) Decrypt: ")
    input_path = input("Enter the input image path: ")
    output_path = input("Enter the output image path: ")

    if choice == '1':
        encrypt_image(input_path, output_path)
    elif choice == '2':
        decrypt_image(input_path, output_path)
    else:
        print("Invalid Option.")
