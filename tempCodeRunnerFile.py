
def findLetterCombination(index, subset):
    if index >= len(digit):
        result.append("".join(subset))
        return
    for ch in use_map[digit[index]]:
        subset.append(ch)
        findLetterCombination(index + 1, subset)
        subset.pop()


use_map = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}
digit = "46"
result = []
subset = []
findLetterCombination(0, [])
print(result)