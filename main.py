# Case-study #3
# Developers: Marinkin O. (%),
# Seledtsov A. (%),
# Evdischenko M. (%)


import random


def main():
    name_file = input('Имя файла: ')
    number_of_sent = int(input('Количество генерируемых предложений: '))
    return name_file, number_of_sent


def dictionary(name):
    try:
        with open(name, 'r', encoding="utf8") as f_in:
            a = []
            f = []
            for i in f_in:
                i = i.replace('\n', '').replace('!', '').replace('?', '').replace('.', '').replace('(', '')\
                    .replace(')', '').replace('<', '').replace('>', '').replace('\'', '').replace('"', '').replace('«', '')\
                    .replace('»', '').replace('-', '').replace('—', '').replace(';', '').split()
                a += i
            for j in a:
                if j[0].isupper():
                    f.append(j)
        a = [i.lower() for i in a]
        d = {}
        for i in range(len(a)-1):
            if a[i] not in d:
                d[a[i]] = []
                d.setdefault(a[i], []).append(i+1)
            else:
                d.setdefault(a[i], []).append(i+1)
        d.setdefault(a[-1], []).append(0)
        return a, d, f
    except FileNotFoundError:
        print('Неверное имя файла!')
        main()


def generation(array, dicti, n_sent, first):
    sent = []
    text = []
    cap = 1
    for i in range(int(n_sent)):
        word = random.choice(first)
        word = first.index(word)
        if cap == 0:
            sent.append(first[word].lower())
        elif cap == 1:
            sent.append(first[word])
        word = first[word].lower()
        word = array.index(word)
        n_words = random.randint(5, 20)
        for j in range(n_words):
            lis = dicti[str(array[int(word)])]
            word = array[random.choice(lis)]
            sent.append(word)
            word = array.index(word)
        if sent[-1][-1] not in ',:;-':
            sent[-1] += random.choice(['.', '!', '?'])
            cap = 1
        else:
            cap = 0
        text += sent
        sent = []
    if text[-1][-1] == ',':
        lis = dicti[str(array[int(word)])]
        word = array[random.choice(lis)]
        text += (word)
    output(text)


def output(t):
    with open('output.txt', 'w', encoding='utf-8') as f_out:
        lenn = 0
        for i in t:
            if lenn + len(i) > 96:
                print('', file=f_out)
                print(i, end=' ', file=f_out)
                lenn = len(i) + 1
                continue
            print(i, end=' ', file=f_out)
            lenn += len(i) + 1


fil, numb = main()
ar, di, fw = dictionary(fil)
generation(ar, di, numb, fw)
