with open('referat.txt', 'r', encoding='utf-8') as myfile:
    text = myfile.read()
    print('Длина строки: ' + str(len(text)))
    print('Количество слов в тексте: ' + str(len(text.split())))
    new_text = text.replace('.','!')
    print(new_text)

with open('referat2.txt', 'w', encoding='utf-8') as myfile2:
    myfile2.write(new_text)