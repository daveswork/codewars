import re


'''
def abbreviate(s):
    test = []
    letter_count = 0
    position = 0
    word_count = 0
    sentence = s.split()
    for word in sentence:
        if len(word)>4:
            for char in word:
                if char.isalpha():
                    if letter_count == 0:
                        test.append(char)
                    letter_count += 1
                    last_alpha = char
                    if position == len(word)-1:
                        test.append(str(letter_count-2))
                        test.append(last_alpha)
                else:
                    test.append(str(letter_count-2))
                    test.append(last_alpha)
                    letter_count = 0
                    test.append(char)
                position += 1
            position = 0
        else:
            test.append(word)
        if word_count != len(sentence) -1:
            test.append(" ")
        word_count += 1
    return ''.join(test)
'''
'''
doggy; is-monolithic; on; mat-sat; double-barreled. the; : 'd3y; i0s-m8c; on; m1t-s1t; d4e-b6d. the;' 
should equal 'd3y; is-m8c; on; mat-sat; d4e-b6d. the;
'''

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

