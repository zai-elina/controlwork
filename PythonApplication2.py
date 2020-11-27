def frequency(file,n):
    with open(file, encoding='utf-8') as f:
        text=(f.read()).lower()

    import string
    symbols=string.punctuation+"\n"+" "
    numbers="123456789"
    for i in numbers:
        symbols+=i

    text = "".join([ch for ch in text if ch not in symbols])
    
    d=dict()
    for ch in text[:n+1]:
        if ch not in d:
            d.setdefault(ch,1)
        else:
            d[ch]+=1

    len_text=len(text)
    for letters in d:
        d[letters]=d[letters]/len_text
    
    sorted_d=sorted(d, key=d.get, reverse=True)
    return sorted_d



def get_key(new_cipher,ch):
    for k,v in new_cipher.items():
        if v==ch:
            return k


def dec(new_cipher):
    en_text=input('\n'+'Введите зашифрованное сообщение:'+'\n')
    en_text=en_text
    if en_text==" ":
        return print('Вы ничего не ввели')

    
    import string
    symbols=string.punctuation+"\n"+" "
    numbers="123456789"
    for i in numbers:
        symbols+=i
    
    text=''
    for ch in en_text:
            if(ch not in symbols):
                if(ch.isupper()):
                    position=get_key(new_cipher,ch.lower())
                    text+=position.upper()
                else:
                    position=get_key(new_cipher,ch)
                    text+=position
            else:
                text+=ch
    print()
    print("Разшиврованное сообщение:")
    print(text)
    print()


def cipher():
    #with open("1.csv", 'a') as f:
    #    f.write("word count"+";"+"Efficiency percentage"+"\n")
    a=1000
    b=20000
    for n in range(a,b+1,1000):
        sorted_g=frequency("text1.txt",n)
        sorted_h=frequency("text2.txt",n)
    
        new_cipher=dict(zip(sorted_g,sorted_h))


        with open("cipher.txt", encoding='utf-8') as f:
                alphabet=(f.readline()).split()
                encoder=(f.readline()).split()
        cipher=dict()
        for i in range(len(encoder)):
            cipher.setdefault(alphabet[i],encoder[i])


        count=0
        for i in cipher:
            if i in new_cipher:
                if cipher[i]==new_cipher[i]:
                    count+=1
        count=round((count/33)*100)
   
        #with open("1.csv", 'a') as f:
        #    f.write(str(n)+";"+str(count)+"\n")
    return new_cipher

def swap(new_cipher,letter):
    
 




new_cipher=cipher()
dec(new_cipher)
while True:
    print("Введите замену букв:")
    letter= input()
    if letter!="-1":
        letter=letter.split()
        new_cipher=swap(new_cipher,letter)
        dec(new_cipher)
    else:
        break
