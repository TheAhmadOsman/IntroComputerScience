#decrypt a message
def decrypt(message, key):
	decrypted = ""
	for ch in message:
		if ch == " ":
			decrypted += " "
		else:
			decrypted += chr(ord(ch) - key)
	return decrypted

def main():
	message = input("Enter message to decrypt: ")
	key = int(input("Enter a key (1-5): "))

	while(key < 1 or key > 5):
		key = int(input("Enter a valid key (1-5): "))

	decrypted = decrypt(message, key)
	print(decrypted)

main()