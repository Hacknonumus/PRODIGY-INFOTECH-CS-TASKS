#!/usr/bin/python3.12

''' Simple image encryption tool using pixel manipulation '''
from PIL import Image
import numpy as np
import argparse

def encrypt_image(image_path, key):

    image = Image.open(image_path)
    img_array = np.array(image)
    # Ensure the key is within the valid range for uint8
    key = key % 256
    # XOR operation for encryption
    encrypted_array = img_array ^ key
    encrypted_image = Image.fromarray(encrypted_array.astype(np.uint8))
    encrypted_image.save(f"encrypted_{image_path}")

def decrypt_image(encrypted_image_path, key):
   
    encrypted_image = Image.open(encrypted_image_path)
    encrypted_array = np.array(encrypted_image)
    # Ensure the key is within the valid range for uint8
    key = key % 256
    # XOR operation for decryption (same as encryption)
    decrypted_array = encrypted_array ^ key
    decrypted_image = Image.fromarray(decrypted_array.astype(np.uint8))
    decrypted_image.save(f"decrypted_{encrypted_image_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple image encryption tool using pixel manipulation",
                                     usage="python PRODIGY_CS_02.py test.png 123 e")
    
    parser.add_argument("image_path", type=str, help="Enter image path")
    parser.add_argument("key", type=int, help="Enter your key")
    parser.add_argument("mode", choices=["e", "d"], help="Specify whether to encrypt (e) or decrypt (d) the image.")
    args = parser.parse_args()

    if args.mode == "e":
        encrypt_image(args.image_path, args.key)
    else:
        decrypt_image(args.image_path, args.key)
