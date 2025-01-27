def create_playfair_matrix(key):
    # إزالة الحروف المتكررة في المفتاح
    key = ''.join(dict.fromkeys(key.upper()))  # إزالة التكرار
    matrix = key + ''.join([chr(i) for i in range(65, 91) if chr(i) not in key and chr(i) != 'J'])
    return [matrix[i:i+5] for i in range(0, len(matrix), 5)]  # تقسيم الجدول إلى 5x5

def prepare_text(text):
    text = text.upper().replace('J', 'I')  # تحويل إلى أحرف كبيرة واستبدال J بـ I
    pairs = []  # قائمة لتخزين الأزواج
    i = 0
    while i < len(text):
        if i + 1 < len(text) and text[i] != text[i+1]:
            # إذا كان الحرفين متنوعين (مختلفين)، نضيف الزوج
            pairs.append(text[i:i+2])
            i += 2  # ننتقل للزوج التالي
        else:
            # إذا كان الحرفين متشابهين، نضيف حرف X بينهما
            pairs.append(text[i] + 'X')
            i += 1  # ننتقل إلى الحرف التالي
    return pairs

def find_position(matrix, char):
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)

def encrypt(text, key):
    matrix = create_playfair_matrix(key)
    pairs = prepare_text(text)
    encrypted_text = ''
    
    for pair in pairs:
        row1, col1 = find_position(matrix, pair[0])
        row2, col2 = find_position(matrix, pair[1])
        
        if row1 == row2:  # نفس الصف
            encrypted_text += matrix[row1][(col1 + 1) % 5]
            encrypted_text += matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:  # نفس العمود
            encrypted_text += matrix[(row1 + 1) % 5][col1]
            encrypted_text += matrix[(row2 + 1) % 5][col2]
        else:  # صفوف وأعمدة مختلفة
            encrypted_text += matrix[row1][col2]
            encrypted_text += matrix[row2][col1]
    
    return encrypted_text

# مثال:
key = "KEYWORD"
text = "HELLO"
encrypted_text = encrypt(text, key)
print("النص المشفر:", encrypted_text)
