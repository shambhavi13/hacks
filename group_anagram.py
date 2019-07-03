from collections import defaultdict

def group_anagram(words):

    group_list = []
    group_words = defaultdict(list)
    for word in words:
        group_words["".join(sorted(word))].append(word)

    for groups in group_words.values():
        print(groups)
        group_list.append(groups)
        print(group_list)

    return group_list

if __name__ == "main":
    words = ['eat', 'tea', 'tan', 'ate', 'tan']
    group_anagram(words)