import base64
import string

# Define the set of possible alphabets
ALPHABET = string.ascii_uppercase + string.ascii_lowercase + string.digits + "+" + "/"
# print(ALPHABET)

plain_text = input("Enter data to encode\n")
cipher_text=""

# Convert to binary
binary_stream = "".join(format(ord(i),"08b") for i in plain_text)
# print("Data in binary format is "+binary_stream)

# create groups of 6 bytes and convert them back into ASCII
while len(binary_stream) % 6:
    binary_stream += "0"

print("Data in binary format is "+binary_stream)
for i in range(0,len(binary_stream),6):
    ascii_val = int(binary_stream[i:i+6],2)
    cipher_text += ALPHABET[ascii_val]

print(cipher_text)
  

