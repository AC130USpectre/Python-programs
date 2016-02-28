def get_code_table(file):
    table = {}
    for line in file:
        table[line[0]] = int(line.split()[-1])
    file.close()
    table['\n'] = 10
    table['\t'] = 11
    return table

def get_decode_table(file):
    table = {}
    for line in file:
        table[int(line.split()[-1])] = line[0]
    file.close()
    table[10] = '\n'
    table[11] = '\t'
    return table

def codec(text):
    table = get_code_table(open('russian_code_table.txt', 'r'))
    result = 0
    for c in text:
        if c in table:
            result = (result << 8) + table[c]
        else:
            result = (result << 8) + 127
    return result

def decodec(number):
    table = get_decode_table(open('russian_code_table.txt', 'r'))
    text = ''
    while number > 0:
        text = table[number & 0b11111111] + text
        number = number >> 8
    return text
