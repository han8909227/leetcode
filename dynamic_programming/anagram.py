"""Given list of words, print all anagrams together."""


def anagram(words):
    """."""
    word_dic = {}
    for word in words:
        word_str = ''.join(sorted(word))
        word_dic.setdefault(word_str, [])
        word_dic[word_str].append(word)
    print(word_dic)

if __name__ == '__main__':
    w = ['anagram', 'gramana', 'coke', 'eokc', 'mop', 'pom']
    anagram(w)
