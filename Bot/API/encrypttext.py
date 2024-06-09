from cryptography.fernet import Fernet

key= b'gAAAAABhJ9Zzv6J9'

def encrypt_text(text):
    f = Fernet(key)
    return f.encrypt(text.encode()).decode()
  
