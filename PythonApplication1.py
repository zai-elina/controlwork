print('1)Шифрование')
print('2)Разшифрование')
print('3)Генерация таблицы шифра')
print('4)Выйти'+'\n')

def symbol():
    import string
    symbols=string.punctuation+"\n"+" "
    numbers="123456789"
    for i in numbers:
        symbols+=i
    return symbols

def chifer():
    with open("cipher.txt", encoding='utf-8') as f:
        alphabet=(f.readline()).split()
        encoder=(f.readline()).split()
    return alphabet,encoder
        
def enc():
    text=input('\n'+'Введите сообщение:'+'\n')
    text=text
    if text==" ":
        return print('Вы ничего не ввели')
    elif text=="текст в файле":
        with open("text.txt", encoding='utf-8') as f:
            text=f.read()   

    symbols=symbol()
    alphabet,encoder=chifer()

    en_text=''
    for ch in text:
            if(ch not in symbols):
                if(ch.isupper()):
                    position=alphabet.index(ch.lower())
                    en_text+=encoder[position].upper()
                else:
                    position=alphabet.index(ch)
                    en_text+=encoder[position]
            else:
                en_text+=ch
    print()
    if len(en_text)>510:
        with open("text1.txt",'w', encoding='utf-8') as f:
            f.write(en_text)
            print("Зашифрованный текст в файле text1.text.")
    else:
        print('Зашифрованное сообщение:')
        print(en_text)
    print()


def dec():
    en_text=input('\n'+'Введите зашифрованное сообщение:'+'\n')
    en_text=en_text
    if en_text==" ":
        return print('Вы ничего не ввели')
    elif en_text=="текст в файле":
        with open("text1.txt", encoding='utf-8') as f:
            en_text=f.read()   
    
    symbols=symbol()
    alphabet,encoder=chifer()

    text=''
    for ch in en_text:
            if(ch not in symbols):
                if(ch.isupper()):
                    position=encoder.index(ch.lower())
                    text+=(alphabet[position].upper())
                else:
                    position=encoder.index(ch)
                    text+=(alphabet[position])
            else:
                text+=ch
    print()
    if len(text)>510:
        with open("text2.txt",'w', encoding='utf-8') as f:
            f.write(text)
            print("Зашифрованный текст в файле text2.text.")
    else:
        print("Разшиврованное сообщение:")
        print(text)
    
    print()

def chifer_print():
    alphabet,encoder=chifer()
    for i in range(len(alphabet)):
        print(alphabet[i]+'->'+encoder[i])


while True:
    text_vybor = input('Выберите действие:'+'\n')
    if text_vybor == "1":
        enc()
    elif text_vybor == "2":
        dec()
    elif text_vybor == "3":
        chifer_print()
    elif text_vybor == "4":
        print('Нажмите Enter')
        break
    else:
        print('Введите 1,2,3 или 4')