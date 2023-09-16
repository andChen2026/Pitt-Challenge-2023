#!/usr/bin/env python3

from pytesseract import image_to_string
import pytesseract
import nltk
from nltk.tokenize import word_tokenize
from PIL import Image, ImageEnhance, ImageFilter
import argparse

# Download necessary nltk datasets if they aren't already
if not nltk.data.find("corpora/stopwords"):
    nltk.download("stopwords")
if not nltk.data.find("tokenizers/punkt"):
    nltk.download("punkt")

def preprocess_image(img_path):
    """Pre-process the image for better OCR output."""
    img = Image.open(img_path)
    
    # Resize the image
    img = img.resize((img.width*2, img.height*2), Image.LANCZOS)
    
    # Convert image to grayscale
    img = img.convert('L')
    
    # Enhance the contrast of the image
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(2)
    
    # Apply a sharpening filter
    img = img.filter(ImageFilter.SHARPEN)
    
    return img

# Use argparse to get the image filename from the command line argument
parser = argparse.ArgumentParser(description='Process an image and extract text using pytesseract.')
parser.add_argument('image_name', type=str, help='The exact name/path of your image file.')
args = parser.parse_args()

image = preprocess_image(args.image_name)

# Fine-tuned config for better OCR output
myconfig = r"--psm 1 --oem 3"

output_text = pytesseract.image_to_string(image, config=myconfig)

# Pre-process the OCR output
tokens = word_tokenize(output_text)
tokens = [t for t in tokens if t.isalnum()]  # Only keep alphanumeric tokens

# Save the pre-processed text to files as per user's choice
while True:
    message = input("Enter the name of the text file to save the processed content or 'quit' to exit: ")
    if message == "quit":
        break
    with open(message, "w") as file:
        file.write(' '.join(tokens))
    print(f"Processed content saved to {message}.")
