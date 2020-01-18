import random

def randomindex(index_list, rest_len):
    i = random.randint(0, rest_len)
    while i in index_list:
        i += 1
    return i
    

def generator(text, sep=' ', option=None):
    li = str.split(text, sep)
    if option == None:
        for word in li:
            yield word
    elif option == 'ordered':
        li.sort()
        for word in li:
            yield word
    elif option == 'unique':
        for i, word in enumerate(li):
            if word not in li[:i]:
                yield word
    elif option == 'random':
        nb_words = len(li)
        rest_len = nb_words - 1
        index_list = []
        for i in range(nb_words):
            rani = randomindex(index_list, rest_len)
            index_list.append(rani)
            rest_len -= 1
            yield li[rani]


for word in generator("Le Lorem Ipsum est simplement du faux texte. du", option='random'):
    print(word)
