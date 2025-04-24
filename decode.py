# Base64_decode_and_more
# NANO IS GHost_NOT_Real
# Base64 decoding with the ability to choose how many times the code should be decoded.

import base64

# Input file name
file_name = input("Enter the file name: ").strip()
if not file_name:
    print("⚠️  Please enter a valid file name.")
    exit()

# Input number of decoding times
decode_input = input("Enter number of times to decode: ").strip()
if not decode_input.isdigit():
    print("⚠️  Please enter a valid number.")
    exit()

decode_times = int(decode_input)

# Read file content
try:
    with open(file_name, 'r') as file:
        encoded_content = file.read()
except FileNotFoundError:
    print("⚠️  File not found.")
    exit()

# Loop to decode
for i in range(decode_times):
    try:
        encoded_content = base64.b64decode(encoded_content).decode('utf-8')
        print(f"Step {i+1}: {encoded_content}")
    except Exception as e:
        print(f"❌ Error at step {i+1}: {e}")
        exit()

# Save result
with open('Dcode.txt', 'w') as result_file:
    result_file.write(encoded_content)

print("✅ Decoded result saved in 'Dcode.txt'.")
# NANO IS GHOST FROM MY TINKING IS NOT REAL 
