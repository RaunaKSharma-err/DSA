def checkParanthesis(string):
    smlBrc = curBrc = bigBrc = 0
    for i in string:
        if i == "(":
            smlBrc += 1
            if i + 1 == "]" or i + 1 == "}":
                return False
        elif i == "{":
            curBrc += 1
            if i + 1 == ")" or i + 1 == "]":
                return False
        elif i == "[":
            bigBrc += 1
            if i + 1 == ")" or i + 1 == "}":
                return False
        else:
            if i == ")":
                smlBrc -= 1
            elif i == "}":
                curBrc -= 1
            else:
                bigBrc -= 1
    return curBrc == curBrc == bigBrc == 0


checkParanthesis("()")