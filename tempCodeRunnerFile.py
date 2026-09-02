def letterCombination(index,digits,subset):
    if index >= len(digits):
        result.append("".join(subset))
        return
    for ch in use_map[digits[index]]:
        subset.append(ch)
        letterCombination(index+1,digits,subset)
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
result=[]
letterCombination(0,"46",[])
print(result)