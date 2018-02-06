# Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
# For example,

# Given:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log","cog"]
# As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.

# Note:
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.


def bfs(begin, end, word_list):
    """LC127 with bfs
    type str: begin
    type str: end
    type set: word_list
    return int.
    """
    word_list.add(end)
    depth = 0
    curr_level = [begin]
    n = len(begin)
    next_level = []

    while curr_level:
        for val in curr_level:
            if val == end:
                return depth

            for i in range(n):
                for l in 'abcdefghijklmnopqrstuvwxyz':
                    w = val[:i] + l + val[i + 1:]  # assess every combonations
                    if w in word_list:  # if it's valid
                        word_list.remove(w)  # ensure not use it again
                        next_level.append(w)  # w become part of transfromation
        depth += 1
        curr_level = next_level
        next_level = []
    return 0


if __name__ == "__main__":
    assert bfs("hit", "cog", {"hot", "dot", "dog", "lot", "log"}) == 5
