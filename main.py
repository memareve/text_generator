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
    with open(name, 'r', encoding="utf8") as f_in:
        a = []
        for i in f_in:
            i = i.replace('\n', '').replace('!', '').replace('?', '').replace('.', '').replace('(','').replace(')','')\
                .replace('<','').replace('>','').replace('\'','').replace('"','').replace('«','').replace('»','')\
                .replace('-','').replace('—','').replace(';','').lower().split()
            a += i
    d = {}
    for i in range(len(a)-1):
        if a[i] not in d:
            d[a[i]] = []
            d.setdefault(a[i], []).append(i+1)
        else:
            d.setdefault(a[i], []).append(i+1)
    d.setdefault(a[-1], []).append(0)
    return a, d


def generation(array, dicti, n_sent):
    sent = []
    text = []
    cap = 1
    for i in range(int(n_sent)):
        word = random.choice(array)
        word = array.index(word)
        if cap == 1:
            sent.append(array[word].capitalize())
        else:
            sent.append(array[word])
        n_words = random.randint(6,22)
        for j in range(n_words):
            list = dicti[str(array[int(word)])]
            word = array[random.choice(list)]
            sent.append(word)
            word = array.index(word)
        if sent[-1][-1] not in ',:;-':
            sent[-1] += random.choice(['.','!','?'])
            cap = 1
        else:
            cap = 0
        text += sent
        sent = []
    lenn = 0
    for i in text:
        if lenn + len(i) > 96:
            print('')
            print(i, end=' ')
            lenn = len(i) + 1
            continue
        print(i, end=' ')
        lenn += len(i) + 1


fil, numb = main()
ar, di = dictionary(fil)
generation(ar, di, numb)

