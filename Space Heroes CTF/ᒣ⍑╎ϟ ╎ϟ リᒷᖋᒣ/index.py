import binascii
from Crypto.Cipher import AES

def xor(a, b):
  return bytes([i^j for i, j in zip(a, b)])

key = b"3153153153153153"
enc = binascii.unhexlify("2a21c725b4c3a33f151be9dc694cb1cfd06ef74a3eccbf28e506bf22e8346998952895b6b35c8faa68fac52ed796694f62840c51884666321004535834dd16b1")

ecb_cipher = AES.new(key, AES.MODE_ECB)

ciphertext = ecb_cipher.decrypt(enc[:16])
iv = xor(ciphertext, b'Mortimer_McMire:')

cbc_cipher = AES.new(key, AES.MODE_CBC, iv)
print(cbc_cipher.decrypt(enc))