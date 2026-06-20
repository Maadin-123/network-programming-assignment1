# File: url_encoder_decoder.py
import urllib.parse

text = input("Text: ")

encoded = urllib.parse.quote(text)
decoded = urllib.parse.unquote(encoded)

print("Encoded:", encoded)
print("Decoded:", decoded)