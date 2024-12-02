#!/usr/bin/env python
import hashlib
import os
import sys

def calculate_hash(file_path, hash_func):
    """Calculate the hash of a file using the specified hash function."""
    hash_obj = hash_func()
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            hash_obj.update(chunk)
    return hash_obj.hexdigest()

def modify_image_to_match_prefix(input_file, output_file, prefix, hash_func=hashlib.sha512):
    """
    Adjust an image file to produce a hash starting with a given prefix.
    """
    # Read the original file
    with open(input_file, 'rb') as f:
        image_data = f.read()
        

    # Attempt to modify the file
    print(f"Modifying {input_file} to match hash prefix: {prefix}")
    for nonce in range(2**32):  # Brute force by appending a nonce
        modified_data = image_data + nonce.to_bytes(4, 'big')
        temp_path = f"{output_file}.temp"
        with open(temp_path, 'wb') as temp_file:
            temp_file.write(modified_data)
        
        # Check hash
        current_hash = calculate_hash(temp_path, hash_func)
        if current_hash.startswith(prefix):
            os.rename(temp_path, output_file)
            print(f"Success! File saved as {output_file} with hash: {current_hash}")
            return

        os.remove(temp_path)  # Clean up temporary file

    print("Failed to find a matching hash prefix.")
    return

# Command-line Interface
if __name__ == "__main__":
    if len(sys.argv) != 4:
        '''How to use ...'''
        print("Usage: spoof <hex_prefix> <original_image> <altered_image>")
        sys.exit(1)

    prefix = sys.argv[1].lstrip("0x")
    original_image = sys.argv[2]
    altered_image = sys.argv[3]
    modify_image_to_match_prefix(original_image, altered_image, prefix)
