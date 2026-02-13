def generate_hamming_code(data):
    # Генерирует код Хемминга для заданного сообщения
    m = len(data)
    r = 0
    while 2 ** r < m + r + 1:
        r += 1

    # Позиции проверочных бит
    check_bit_positions = [2 ** i for i in range(r)]

    # Создание кодового слова
    codeword = [0] * (m + r)
    codeword_index = 0
    data_index = 0
    for i in range(len(codeword)):
        if i + 1 in check_bit_positions:
            codeword[i] = 0  # Проверочный бит
        else:
            codeword[i] = int(data[data_index])
            data_index += 1

    # Вычисление проверочных бит
    for i in range(r):
        check_bit_position = check_bit_positions[i]
        check_bit_value = 0
        for j in range(len(codeword)):
            if (j + 1) & check_bit_position:
                check_bit_value ^= codeword[j]
        codeword[check_bit_position - 1] = check_bit_value

    return codeword

# Исходное сообщение
data = '0000010101000000111'

# Создание кодового слова
codeword = generate_hamming_code(data)
# Извлечение данных из кодового слова

print("Исходные данные:", data)
print("Полученное кодовое слово:", *codeword)