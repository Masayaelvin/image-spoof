# Image Hash Spoofing Tool

## Overview
This tool takes an image file and modifies it to create a new file with a hash that starts with a specified prefix. Despite the changes made to the file, the altered image will remain visually identical to the original when viewed.

The tool uses a brute-force approach by appending a **nonce** (a 4-byte number) to the image data and recalculating the hash until the desired prefix is achieved.

---

## Features
- Supports multiple hash algorithms (e.g., SHA-256, SHA-512).
- Ensures the output file looks identical to the original image.
- Allows users to specify the desired prefix for the hash.

---

## Requirements
- Python 3.8 or later (for the walrus operator `:=`).
- The `hashlib` module (built into Python).

---

## How It Works
1. The script reads the input image file in chunks to efficiently handle large files.
2. A **nonce** (4 bytes) is appended to the image data.
3. The hash of the modified data is calculated using the specified hash function.
4. This process repeats until the hash starts with the desired prefix.
5. The modified image is saved to the specified output file.

---

## Usage

### Command-Line Syntax
```bash
python spoof.py <prefix> <input_file> <output_file>
