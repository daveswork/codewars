import re

def abbreviate(s):
    sentence = s.split()
    test = []
    for word in sentence:
        abbv = word[0]+str(len(word)-2)+word[-1]
        test.append(abbv)
    return ' '.join(test)


string = "internationalization"

print(abbreviate(string))
