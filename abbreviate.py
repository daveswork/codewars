import re

def abbreviate(s):
    non_alpha = "[^a-zA-z]"
    words = re.split(non_alpha, s)
    non_words = re.findall(non_alpha, s)
    new_words = []
    for word in words:
        if len(word)>4:
            new_word = word[0]+str(len(word)-2)+word[-1]
            new_words.append(new_word)
        else:
            new_words.append(word)
    if len(non_words) < 1:
        sentence = new_words
    else:
        sentence = [j for i in zip(new_words, non_words) for j in i]
    return ''.join(sentence)

