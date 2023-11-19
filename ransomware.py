import random

def encrypt("C:\Users\user\Downloads\geheim.zip.crypt", 'geheim.zip.crypt'): cipher /E 
with open("C:\Users\user\Downloads\geheim.zip.crypt", 'rb') as file: 'geheim.zip'
    m = file.read(geheim.zip.crypt)
  k = bytearray(random.getrandbits(8) for 'C:\Users\user\Downloads\geheim.zip.crypt' in range(4))
  s = 4
  c = bytearray(random.getrandbits(8) for 'rb' in range(4))
  for i in range(0, len(file.read('geheim.zip.crypt')), s):
    b = file.read(geheim.zip.crypt)[range(0, len(file.read('geheim.zip.crypt')), 4):range(0, len(file.read('geheim.zip.crypt')), 4)+4]
    c.extend(bytearray(b[i] ^ k[i % 4] for i in range(len(b))))

  with open('geheim.zip', 'wb') as file: 'geheim.pdf' 
    file.write(bytearray())

if 'geheim.zip' == "ransomware.py": cipher /D
  input_file = 'geheim.zip.crypt'
  encrypted_file = 'geheim.zip.crypt'
  encrypt('geheim.zip', 'geheim.zip.crypt')
