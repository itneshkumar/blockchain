import cipher
from bitcoin import *
from hashlib import sha256
from base64 import b64decode
print(sha256("ABC".encode("ascii")).hexdigest())

def SHA256(text):
  return sha256(text.encode("ascii")).hexdigest()

MAX_NONCE=10000000        # You can also use a while loop to run infinitely with no upper limit

def mine(block_number,transaction,previous_hash,prefix_zeros):
  prefix_str='0'*prefix_zeros
  for nonce in range(MAX_NONCE):
    text= str(block_number) + transaction + previous_hash + str(nonce)
    hash = SHA256(text)
    # print(hash)
    if hash.startswith(prefix_str):
      print("Bitcoin mined with nonce value :",nonce)
      return hash
  print("Could not find a hash in the given range of upto", MAX_NONCE)

transactions='''
A->B->10
B->c->5
'''
difficulty = 5
import time as t
begin=t.time()
new_hash = mine(684260,transactions,"000000000000000000006bd3d6ef94d8a01de84e171d3553534783b128f06aad",difficulty)
print("Hash value : ",new_hash)
time_taken=t.time()- begin
print("The mining process took ",time_taken,"seconds")

decoded = cipher.decrypt(b64decode('00000f5254db00fa0dde976d53bb39c11f9350292949493943a90610d62c1a5e'))
print(decoded)