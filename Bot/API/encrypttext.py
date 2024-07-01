from cryptography.fernet import Fernet

key= Fernet.generate_key()

with open("key.key", "wb") as key_file:
    key_file.write(key)
    
def load_key():
    return open("key.key", "rb").read



def encrypt_text(text):
    key = load_key()
    f = Fernet(key)
    return f.encrypt(text.encode()).decode()


def decrypt_text(text):
    key = load_key()
    f = Fernet(key)
    return f.decrypt(text.encode()).decode()


def encrypt_image(image):
    key = load_key()
    f = Fernet(key)
    with open(image, "rb") as file:
        return f.encrypt(file.read()).decode()
    

def decrypt_image(image):
    key = load_key()
    f = Fernet(key)
    with open(image, "rb") as file:
        return f.decrypt(file.read()).decode()

  
