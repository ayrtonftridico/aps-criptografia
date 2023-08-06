from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_message(key, message):
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    return encrypted_message

def decrypt_message(key, encrypted_message):
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message).decode()
    return decrypted_message

if __name__ == "__main__":
    key = generate_key()
    print("Chave gerada:", key.decode())

    while True:
        print("\nEscolha uma opção:")
        print("1. Criptografar mensagem")
        print("2. Descriptografar mensagem")
        print("3. Sair")
        
        choice = input("Opção: ")

        if choice == "1":
            mensagem_original = input("Digite a mensagem a ser criptografada: ")
            mensagem_criptografada = encrypt_message(key, mensagem_original)
            print("Mensagem criptografada:", mensagem_criptografada.decode())
        elif choice == "2":
            mensagem_criptografada = input("Digite a mensagem criptografada: ").encode()
            mensagem_descriptografada = decrypt_message(key, mensagem_criptografada)
            print("Mensagem descriptografada:", mensagem_descriptografada)
        elif choice == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
