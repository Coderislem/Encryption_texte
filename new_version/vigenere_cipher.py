def vigenere_cipher(text, key, mode='encrypt'):
    result = ""  # النص الناتج
    key = key.upper()  # تحويل كلمة المفتاح إلى حروف كبيرة
    key_index = 0  # مؤشر لتتبع حرف المفتاح الحالي

    for char in text:
        if char.isalpha():  # إذا كان الحرف أبجديًا فقط
            shift = 65 if char.isupper() else 97  # تحديد إذا كان الحرف كبيرًا أو صغيرًا
            char_value = ord(char) - shift  # تحويل الحرف إلى رقم

            key_value = ord(key[key_index % len(key)]) - 65  # قيمة الحرف من المفتاح
            key_index += 1  # الانتقال إلى الحرف التالي من المفتاح

            # إذا كان الوضع "تشفير"، نضيف القيم، وإذا كان "فك التشفير"، نطرحها
            if mode == 'encrypt':
                new_char = chr((char_value + key_value) % 26 + shift)
            elif mode == 'decrypt':
                new_char = chr((char_value - key_value) % 26 + shift)

            result += new_char
        else:
            result += char  # إذا كان الحرف غير أبجدي، نضيفه كما هو

    return result


# أمثلة على الاستخدام:
# النص الأصلي
original_text = "ATTACK AT DOWN"
key = "KEY"

# تشفير النص
encrypted_text = vigenere_cipher(original_text, key, mode='encrypt')
print("النص المشفر:", encrypted_text)

# فك التشفير
decrypted_text = vigenere_cipher(encrypted_text, key, mode='decrypt')
print("النص المفكوك:", decrypted_text)
