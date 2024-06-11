##################################################################################
#                                                                                #
#              Karma-X Inc. - DJB2 Shellcode Collision Generator                 #
#                                                                                #
#                                                                                #
##################################################################################

import random
import string

def djb2(s: str) -> int:
    hash_val = 5381
    for char in s:
        hash_val = ((hash_val << 5) + hash_val) + ord(char)
    return hash_val & 0xFFFFFFFF

def next_string(s: str) -> str:
    charset = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_'
    if not s:
        return charset[0]
    s_list = list(s)
    idx = len(s_list) - 1
    while idx >= 0:
        char_idx = charset.index(s_list[idx])
        if char_idx < len(charset) - 1:
            s_list[idx] = charset[char_idx + 1]
            return ''.join(s_list)
        else:
            s_list[idx] = charset[0]
            idx -= 1
    return charset[0] + ''.join(s_list)

def find_collision(target_hashes):
    s = ''
    collisions = {}

    while len(collisions) < len(target_hashes):
        fuzzed_string = s
        hash_val = djb2(fuzzed_string)
        if hash_val in target_hashes and hash_val not in collisions:
            print(f"Found collision: '{fuzzed_string}' hashes to {hash_val:08x}")
            collisions[hash_val] = fuzzed_string
        s = next_string(s)
    return collisions

target_hashes = [0x7040ee75, 0x5fbff0fb, 0x668fcf2e, 0x382c0f97]
collisions = find_collision(target_hashes)

for hash_val, coll_str in collisions.items():
    print(f"Found collision: '{coll_str}' hashes to {hash_val:08x}")
