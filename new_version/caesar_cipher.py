def caesar_cipher(text, key, mode='encrypt'):
    result = ""
    if mode == 'decrypt':
        key = -key  # المفتاح بالسالب لفك التشفير

    for char in text:
        if char.isalpha():
            shift = 65 if char.isupper() else 97  # تحديد الحروف الكبيرة أو الصغيرة
            char_position = ord(char) - shift
            new_position = (char_position + key) % 26
            new_char = chr(new_position + shift)
            result += new_char
        else:
            result += char  # الأحرف غير الأبجدية تُترك كما هي

    return result


# مثال على الاستخدام
print(caesar_cipher("HELLO WORLD", 3, 'encrypt'))  # تشفير
print(caesar_cipher("KHOOR ZRUOG", 3, 'decrypt'))  # فك التشفير
