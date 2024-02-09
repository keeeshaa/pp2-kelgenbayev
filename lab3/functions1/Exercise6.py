def reverse(sentence):
    words = sentence.split()
    reversed_words = ' '.join(reversed(words))
    return reversed_words

sentence = input()
reversed_sentence = reverse(sentence)
print(reversed_sentence)