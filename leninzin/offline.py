
import requests
import os
import binascii
import ecdsa
import hashlib
import base58
import time
import sys
from multiprocessing import Process, Queue



def privateKey(): # Generates random 256 bit private key in hex format
    return binascii.hexlify(os.urandom(32)).decode('utf-8')
def address(publickey): # Public Key -> Wallet Address
    alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    c = '0'; byte = '00'; zero = 0
    var = hashlib.new('ripemd160')
    var.update(hashlib.sha256(binascii.unhexlify(publickey.encode())).digest())
    a = (byte + var.hexdigest())
    doublehash = hashlib.sha256(hashlib.sha256(binascii.unhexlify(a.encode())).digest()).hexdigest()
    address = a + doublehash[0:8]
    for char in address:
        if (char != c):
            break
        zero += 1
    zero = zero // 2
    n = int(address, 16)
    output = []
    while (n > 0):
        n, remainder = divmod (n, 58)
        output.append(alphabet[remainder])
    count = 0
    while (count < zero):
        output.append(alphabet[0])
        count += 1
    return ''.join(output[::-1])

def publicKey(privatekey): # Private Key -> Public Key
    privatekey = binascii.unhexlify(privatekey)
    s = ecdsa.SigningKey.from_string(privatekey, curve = ecdsa.SECP256k1)
    return '04' + binascii.hexlify(s.verifying_key.to_string()).decode('utf-8')

def main():
        f = open("btcadresses.txt", 'r')
        x = [i[:-1] for i in f]
        n = 0
        while True:
            k = privateKey()
            if address(publicKey(k)) in x:
                print(k)
                e = open("vouchorar.txt", 'w')
                e.write(k)
                e.close()
            n += 1
            print(n)
            
if __name__ == "__main__":
    main()
