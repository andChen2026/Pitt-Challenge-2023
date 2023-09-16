#!/usr/bin/env python3

from pytesseract import image_to_string
import pytesseract
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from PIL import Image
import argparse

# Download necessary nltk datasets if they aren't already
if not nltk.data.find("corpora/stopwords"):
    nltk.download("stopwords")
if not nltk.data.find("tokenizers/punkt"):
    nltk.download("punkt")

myconfig = r"--psm 6 --oem 3"

# Use argparse to get the image filename from the command line argument
parser = argparse.ArgumentParser(description='Process an image and extract text using pytesseract.')
parser.add_argument('image_name', type=str, help='The exact name/path of your image file.')
args = parser.parse_args()

image = Image.open(args.image_name)
output_text = pytesseract.image_to_string(image, config=myconfig)

# Pre-process the OCR output
stop_words = set(stopwords.words("english"))
tokens = word_tokenize(output_text)
tokens = [t for t in tokens if t.lower() not in stop_words and t.isalnum()]  # Added t.isalnum() to remove punctuation

# Save the pre-processed text to files as per user's choice
while True:
    message = input("Enter the name of the text file to save the processed content or 'quit' to exit: ")
    if message == "quit":
        break
    with open(message, "w") as file:
        file.write(' '.join(tokens))
    print(f"Processed content saved to {message}.")
