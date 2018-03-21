#encrypt a message
def encrypt(message, key):
	encrypted = ""
	for ch in message:
		if ch == " ":
			encrypted += " "
		else:
			encrypted += chr(ord(ch) + key)
	return encrypted

def main():
	message = input("Enter message to encrypt: ")
	key = int(input("Enter a key (1-5): "))

	while(key < 1 or key > 5):
		key = int(input("Enter a valid key (1-5): "))

	encrypted = encrypt(message, key)
	print(encrypted)

main()