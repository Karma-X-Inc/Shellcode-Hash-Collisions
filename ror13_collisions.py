##################################################################################
#                                                                                #
#              Karma-X Inc. - ROR13 Shellcode Collision Generator                #
#                                                                                #
#                                                                                #
##################################################################################

import random
import string


def ror13hash(s):
    hashvalue = 0
    for char in s:
        hashvalue = (hashvalue >> 13) | (hashvalue << (32 - 13)) 
        hashvalue = (hashvalue + ord(char)) & 0xFFFFFFFF  # Add the character's ASCII value
    return hashvalue


def randomstring(length):
    return ''.join(random.choices(string.asciiletters + string.digits, k=length))


def findcollisions(targethash, maxattempts=1000000, stringlength=10):
    collisions = []
    attempts = 0
    while attempts < maxattempts:
        s = randomstring(stringlength)
        if ror13hash(s) == targethash:
            collisions.append(s)
            print(f"Collision found: {s}")
        attempts += 1
    return collisions


targethash = ror13hash("example")
collisions = findcollisions(targethash)


print(f"Collisions for hash {targethash}: {collisions}")
