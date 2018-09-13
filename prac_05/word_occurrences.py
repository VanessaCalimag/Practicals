duplicate_words = {}
sentence = input("Write the sentence: ")
# Susie works in a shoeshine shop. Where she shines she sits, and where she sits she shines

words = sentence.split()
for word in words:
    occurrence = duplicate_words.get(word, 0)
    duplicate_words[word] = occurrence + 1

words = list(duplicate_words.keys())
words.sort()
max_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, duplicate_words[word]))