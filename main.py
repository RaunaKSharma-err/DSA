class solution:
    def rotateMatrix(self, s):
        result = []
        balance = 0

        for ch in s:
            if ch == "(":
                balance += 1
                result.append(ch)
            elif ch == ")":
                if balance > 0:
                    balance -= 1
                    result.append(ch)
            else:
                result.append(ch)

        final = []
        for ch in reversed(result):
            if ch == "(" and balance > 0:
                balance -= 1
            else:
                final.append(ch)

        return "".join(reversed(final))


s = "a)b(c)d"
c = solution()
r = c.rotateMatrix(s)
print(r)
