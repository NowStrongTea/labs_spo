def encrypt(text, shift):
    result = ""
    for char in text:
        shifted_char = chr(ord(char) + shift)
        result += shifted_char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

text = input("Введите строку для шифрования/расшифровки: ")
shift = int(input("Введите коэффициент сдвига: "))
mode = input("Выберите режим работы (encrypt/decrypt): ")

if mode.lower() == "encrypt":
    encrypted_text = encrypt(text, shift)
    print("Encrypted text:", encrypted_text)
elif mode.lower() == "decrypt":
    decrypted_text = decrypt(text, shift)
    print("Decrypted text:", decrypted_text)
else:
    print("Error: Incorrect mode selected.")

