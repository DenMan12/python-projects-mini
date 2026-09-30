def en_coder(message, key):
    code_message = ''
    for ch in message:
        if ch.islower():
            code = ord(ch) + key
            if code > 122:
                code -= 26
        elif ch.isupper():
            code = ord(ch) + key
            if code > 90:
                code -= 26
        else:
            code_message += ch
            continue
        code_message += chr(code)
    return code_message

def en_decoder(message, key):
    decode_message = ''
    for ch in message:
        if ch.islower():
            decode = ord(ch) - key
            if decode < 97:
                decode += 26
            decode_message += chr(decode)
        elif ch.isupper():
            decode = ord(ch) - key
            if decode < 65:
                decode += 26
            decode_message += chr(decode)
        else:
            decode_message += ch
            continue
    return decode_message

def ru_coder(message, key):
    code_message = ''
    for ch in message:
        if ch.islower():
            code = ord(ch) + key
            if code > 1103:
                code -= 32
            code_message += chr(code)
        elif ch.isupper():
            code = ord(ch) + key
            if code > 1071:
                code -= 32
            code_message += chr(code)
        else:
            code_message += ch
    return code_message

def ru_decoder(message, key):
    decode_message = ''
    for ch in message:
        if ch.islower():
            decode = ord(ch) - key
            if decode < 1072:
                decode += 32
            decode_message += chr(decode)
        elif ch.isupper():
            decode = ord(ch) - key
            if decode < 1040:
                decode += 32
            decode_message += chr(decode)
        else:
            decode_message += ch
    return decode_message

language = input('Выберите, пожалуйста, язык (ru = Russian, en = English):')
code_or_decode = input('Вы хотите зашифровать или расшифровать сообщение? (з = зашифровать, р = расшифровать):')
message = input('Введите шифруемое сообщение:')
key = int(input('Введите ключ для сообщения:'))

if language == 'en':
    if code_or_decode == 'з':
        print(en_coder(message, key))
    elif code_or_decode == 'р':
        print(en_decoder(message, key))
    else:
        print('Ошибка: Неизвестная команда!')
elif language == 'ru':
    if code_or_decode == 'з':
        print(ru_coder(message, key))
    elif code_or_decode == 'р':
        print(ru_decoder(message, key))
    else:
        print('Ошибка: Неизвестная команда!')
else:
    print('Ошибка: Неизвестный язык!')
