# Case-study #3
# Developers: Marinkin O. (%),
# Seledtsov A. (%),
# Evdischenko M. (%)


import random



def main():
    name_file = input()
    number_of_sent = int(input())
    return name_file, number_of_sent


def dictionary(name):
    with open(name, 'r', encoding="utf8") as f_in:
        a = []
        for i in f_in:
            i = i.replace('\n','').replace('!','').replace('?','').replace('.','').split()
            a += i
    d = {}
    for i in range(len(a)-1):
        if a[i] not in d:
            d[a[i]] = []
            d.setdefault(a[i], []).append(i+1)
        else:
            d.setdefault(a[i], []).append(i+1)
    print(a)
    print(d)
    return a, d

def first(array):
    f = []
    for i in array:
        if i[0].isupper() == True:
            f.append(i)
    first_word = random.choice(f)
    return first_word

def generation(array, dicti, fiirst):
    sent = []
    text = []
    sent.append(fiirst)
    sent.append(random.choice(dicti))
    print(sent)


fil, numb = main()
ar, di = dictionary(fil)
ffirst = first(ar)
generation(ar,di,ffirst)

