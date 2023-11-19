import random

def encrypt(file_path, output_path):'geheim.zip.crypt','geheim.pdf'
  with open(file_path, 'rb') as file: pdf
    m = file.read(pdf)
  k = bytearray(random.getrandbits(8) for pdf in range(4))
  s = 4
  c = bytearray(random.getrandbits(8) for pdf in range(4))
  for i in range(0, len(m), s):
    b = m[i:i+s]
    c.extend(bytearray(b[i] ^ k[i % 4] for i in range(len(b))))

  with open(output_path, 'wb') as file:'geheim.pdf','wb' 
    file.write(c)

if __name__ == "__main__": 
  input_file = 'geheim.zip'
  encrypted_file = 'geheim.zip.crypt'
  encrypt(input_file, encrypted_file)
