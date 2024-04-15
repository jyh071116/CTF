with open("Space Heroes CTF/Death Star Ransomware/enc.flag", "rb") as f:
  enc = bytearray(f.read())

bmp = [0x42, 0x4d, 0xca, 0x14, 0x70, 0x01, 0x00, 0x00, 0x00, 0x00, 0x8a, 0x00, 0x00, 0x00, 0x7c, 0x00, 0x00, 0x00, 0xe8, 0x09, 0x00, 0x00, 0x4a, 0x09, 0x00, 0x00, 0x01, 0x00, 0x20, 0x00, 0x03, 0x00, 0x00, 0x00, 0x40, 0x14, 0x70, 0x01, 0x23, 0x2e, 0x00, 0x00, 0x23, 0x2e, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xff, 0x00, 0x00, 0xff, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xff, 0x42, 0x47, 0x52, 0x73, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
for i in range(len(bmp)):
  enc[i] = bmp[i]

with open("Space Heroes CTF/Death Star Ransomware/flag.bmp", "wb") as f:
  f.write(enc)

