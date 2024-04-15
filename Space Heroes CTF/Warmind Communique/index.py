from gostcrypto import gostcipher

def xor(a, b):
  return bytes([i^j for i, j in zip(a, b)])

with open("Space Heroes CTF/Warmind Communique/encrypted.enc", "rb") as f:
  enc = f.read()
key = b'SKYSHOCKSKYSHOCKSKYSHOCKSKYSHOCK'

ecb_cipher = gostcipher.new("magma", key, gostcipher.MODE_ECB)

ciphertext = ecb_cipher.decrypt(enc[:16])
iv = xor(ciphertext, b'V150NLK747CLS000')

cbc_cipher = gostcipher.new("magma", key, gostcipher.MODE_CBC, init_vect = iv)

print(cbc_cipher.decrypt(enc))