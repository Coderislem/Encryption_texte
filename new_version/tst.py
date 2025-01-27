txt = "AB"

key = 3

# for char in txt:
#     if char.isalpha():
#         shift = 65 if char.isupper() else 97
#         new_char = chr((ord(char) - shift + key) % 26 + shift)
#         print(new_char)
#     else:
#         print(char)
shift = 65 if "M".isupper() else 97
print(shift)
print(ord('B'))
print(chr(77))
print(ord('H')-65)
print(chr(30 % 26 + 65))
key = "momo"
print(''.join(dict.fromkeys(key.upper())))