def single_root_words(root_word, *other_words):
    same_words = []
    root_word = root_word.lower()
    for word in other_words:
        word = word.lower()
        if root_word in word or word in root_word:
            same_words.append(word)
    return same_words

result = print (single_root_words())

