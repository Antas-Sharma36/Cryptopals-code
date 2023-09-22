import base64
import string

# Define the set of possible alphabets
ALPHABET = string.ascii_uppercase + string.ascii_lowercase + string.digits + "+" + "/"
# print(ALPHABET)

# Take hex input and convert it into text format  
hex_plain_text = input("Enter data to encode\n")
plain_text = bytearray.fromhex(hex_plain_text).decode()

# Initialize cipher text and padding variable 
cipher_text=""
padding=0

# Convert to binary
binary_stream = "".join(format(ord(i),"08b") for i in plain_text)
# print("Data in binary format is "+binary_stream)

# create groups of 6 bytes and convert them back into ASCII
while len(binary_stream) % 6:
    binary_stream += "0"
    padding+=1;

padding = int(padding/2)

print("Data in binary format is "+binary_stream)
for i in range(0,len(binary_stream),6):
    ascii_val = int(binary_stream[i:i+6],2)
    cipher_text += ALPHABET[ascii_val]

for i in range(padding):
    cipher_text+="="

print(cipher_text)
  


