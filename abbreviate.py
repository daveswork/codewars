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

