def shifr(t):
    d = {'а':'a','б':'b','в':'v','г':'g','д':'d','е':'e','ё':'e',
         'ж':'zh','з':'z','и':'i','й':'y','к':'k','л':'l','м':'m',
         'н':'n','о':'o','п':'p','р':'r','с':'s','т':'t','у':'u',
         'ф':'f','х':'h','ц':'ts','ч':'ch','ш':'sh','щ':'sch',
         'ъ':'','ы':'y','ь':'','э':'e','ю':'yu','я':'ya',
         'А':'A','Б':'B','В':'V','Г':'G','Д':'D','Е':'E','Ё':'E',
         'Ж':'ZH','З':'Z','И':'I','Й':'Y','К':'K','Л':'L','М':'M',
         'Н':'N','О':'O','П':'P','Р':'R','С':'S','Т':'T','У':'U',
         'Ф':'F','Х':'H','Ц':'TS','Ч':'CH','Ш':'SH','Щ':'SCH',
         'Ъ':'','Ы':'Y','Ь':'','Э':'E','Ю':'YU','Я':'YA'}
    r = ''
    for c in t:
        if c in d:
            r += d[c]
        else:
            r += c
    return r

def deshifr(t):
    d = {'a':'а','b':'б','v':'в','g':'г','d':'д','e':'е',
         'zh':'ж','z':'з','i':'и','y':'й','k':'к','l':'л','m':'м',
         'n':'н','o':'о','p':'п','r':'р','s':'с','t':'т','u':'у',
         'f':'ф','h':'х','ts':'ц','ch':'ч','sh':'ш','sch':'щ',
         'yu':'ю','ya':'я','A':'А','B':'Б','V':'В','G':'Г','D':'Д',
         'E':'Е','ZH':'Ж','Z':'З','I':'И','Y':'Й','K':'К','L':'Л',
         'M':'М','N':'Н','O':'О','P':'П','R':'Р','S':'С','T':'Т',
         'U':'У','F':'Ф','H':'Х','TS':'Ц','CH':'Ч','SH':'Ш','SCH':'Щ',
         'YU':'Ю','YA':'Я'}
    r = ''
    i = 0
    while i < len(t):
        if i < len(t)-3 and t[i:i+3].lower() == 'sch':
            if t[i:i+3] in d:
                r += d[t[i:i+3]]
            else:
                r += d[t[i:i+3].lower()]
            i += 3
        elif i < len(t)-2 and t[i:i+2].lower() in ['zh','ts','ch','sh','yu','ya']:
            if t[i:i+2] in d:
                r += d[t[i:i+2]]
            else:
                r += d[t[i:i+2].lower()]
            i += 2
        elif t[i] in d:
            r += d[t[i]]
            i += 1
        else:
            r += t[i]
            i += 1
    return r

while True:
    print('\n1 - зашифровать encoded.txt')
    print('2 - расшифровать encoded.txt')
    print('3 - показать содержимое encoded.txt')
    print('4 - выйти')
    c = input('выбери: ')

    if c == '1':
        try:
            with open('encoded.txt', 'r', encoding='utf-8') as f:
                t = f.read()
            print('\nбыло:')
            print(t)
            res = shifr(t)
            with open('encoded.txt', 'w', encoding='utf-8') as f:
                f.write(res)
            print('\nстало:')
            print(res)
            print('\nготово')
        except:
            print('ошибка')

    elif c == '2':
        try:
            with open('encoded.txt', 'r', encoding='utf-8') as f:
                t = f.read()
            print('\nбыло:')
            print(t)
            res = deshifr(t)
            with open('encoded.txt', 'w', encoding='utf-8') as f:
                f.write(res)
            print('\nстало:')
            print(res)
            print('\nготово')
        except:
            print('ошибка')

    elif c == '3':
        try:
            with open('encoded.txt', 'r', encoding='utf-8') as f:
                print('\n' + f.read())
        except:
            print('ошибка')

    elif c == '4':
        print('пока')
        break

    else:
        print('неверно')
