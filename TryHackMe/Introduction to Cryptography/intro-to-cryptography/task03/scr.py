from Crypto.PublicKey import RSA
import binascii

# Load the RSA private key
private_key_data = open('private-key-bob.pem', 'rb').read()
private_key = RSA.import_key(private_key_data)

# Extract the last byte of the private key
last_byte = private_key.d.to_bytes((private_key.bit_length() + 7) // 8, byteorder='big')[-1]

# Print the last byte in hexadecimal format
print(f"Last byte of RSA private key: {binascii.hexlify(bytes([last_byte]))}")