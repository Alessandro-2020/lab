def shifrovka (word, key):
        result = ''
        for l,k in zip(word, key):
                new_l = ord(l.upper())+(ord(k.upper())-ord("A"))+1
                if new_l>90:
                    new_l-=26
                    
                result += chr(new_l)
        return result
def shifrovka_rus (word, key):
        result = ''
        for l,k in zip(word, key):
                new_l = ord(l.upper())+(ord(k.upper())-ord("А"))+1
                if new_l>1071:
                    new_l-=32
                    
                result += chr(new_l)
        return result
def deshifrovka (word, key):
    result = ''
    for l,k in zip(word, key):
            new_l = ord(l.upper())-(ord(k.upper())-ord("A"))-1
            if new_l<65:
                new_l+=26
                    
            result += chr(new_l)
    return result
def deshifrovka_rus (word, key):
    result = ''
    for l,k in zip(word, key):
            new_l = ord(l.upper())-(ord(k.upper())-ord("А"))-1
            if new_l<1040:
                new_l+=32
                    
            result += chr(new_l)
    return result
def kluch(word, key):
        size_word = len(word)
        while len(key) < size_word:
                key += key
        return key
lang = input('Введите язык шифрования(rus, eng):')
a = input('0=шифровка, 1=расшифровка:')               
word = input('Введите слово:  ')
key = input('ключ:  ')
new_key = kluch(word, key)
if lang==("rus"):  
   if a=="0":
       print ('Зашифрованное слово:', shifrovka_rus (word, new_key))
   else:
       print ('Расшифрованное слово:', deshifrovka_rus(word, new_key))
if lang==("eng"):
  if a=="0":
   print ('Зашифрованное слово:', shifrovka (word, new_key))
  else:
   print ('Расшифрованное слово:', deshifrovka (word, new_key))
else:
  print("Название языка набрано неверно, либо этот язык не был добавлен")

