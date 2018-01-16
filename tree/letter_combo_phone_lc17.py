# Given a digit string, return all possible letter combinations that the number could represent.

# A mapping of digit to letters (just like on the telephone buttons) is given below.

# Input:Digit string "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# Note:
# Although the above answer is in lexicographical order, your answer could be in any order you want.


def letter_combinations(self, digits):
    """LC17 in Python."""
    if not digits:
        return []
    dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    res = []
    dfs(digits, dic, 0, "", res)
    return res


def dfs(self, digits, dic, index, path, res):
    """DFS."""
    if len(path) == len(digits):
        res.append(path)
        return
    for i in xrange(index, len(digits)):
        for j in dic[digits[i]]:
            dfs(digits, dic, i + 1, path + j, res)

