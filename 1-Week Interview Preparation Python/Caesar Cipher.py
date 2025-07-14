"""

Julius Caesar protected his confidential information by encrypting it using a cipher. Caesar's cipher shifts each letter by a number of letters. If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet. In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.

Original alphabet:      abcdefghijklmnopqrstuvwxyz
Alphabet rotated +3:    defghijklmnopqrstuvwxyzabc

Sample Input

11
middle-Outz
2

Sample Output

okffng-Qwvb

"""

import os

def shiftAlphabet(c, k):
    if 65 <= c <= 90:
        c += k
        if c < 65:
            c += 26
        elif c > 90:
            c -= 26
    elif 97 <= c <= 122:
        c += k
        if c < 97:
            c += 26
        elif c > 122:
            c -= 26

    return chr(c)

def caesarCipher(s, k):
    ret = []
    k %= 26
    for i in s:
        ret.append(shiftAlphabet(ord(i), k))

    return ''.join(ret)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    s = input()
    k = int(input())

    result = caesarCipher(s, k)

    fptr.write(result)
    fptr.close()
