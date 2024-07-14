# Given a string formula representing a chemical formula, return the count of each atom.
#
# The atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.
#
# One or more digits representing that element's count may follow if the count is greater than 1. If the count is 1, no digits will follow.
#
# For example, "H2O" and "H2O2" are possible, but "H1O2" is impossible.
# Two formulas are concatenated together to produce another formula.
#
# For example, "H2O2He3Mg4" is also a formula.
# A formula placed in parentheses, and a count (optionally added) is also a formula.
#
# For example, "(H2O2)" and "(H2O2)3" are formulas.
# Return the count of all elements as a string in the following form: the first name (in sorted order), followed by its count (if that count is more than 1), followed by the second name (in sorted order), followed by its count (if that count is more than 1), and so on.

class Solution:
    def countOfAtoms(self, formula: str) -> str:

        tt = ""
        arr = []
        temp = ""
        for i in range(0, len(formula)):
            cu = formula[i]

            if temp == "":
                temp += cu
                continue
            if cu == "(" or cu == ")":
                if temp != "":
                    arr.append(temp)
                arr.append(cu)
                temp = ""
                continue

            if temp.isnumeric():
                if cu.isnumeric():
                    temp += cu
                else:
                    arr.append(temp)
                    temp = cu
            else:
                if cu.isnumeric():
                    arr.append(temp)
                    temp = cu
                else:
                    if cu.isupper():
                        arr.append(temp)
                        temp = cu
                    else:
                        temp += cu
        if temp != "":
            arr.append(temp)

        newarr = []
        i = 0
        while i < len(arr):
            cu = arr[i]
            if cu == "(":
                newarr.append((cu, 0))

            elif cu == ")":

                nexta = 1
                if i + 1 < len(arr):
                    temp = arr[i + 1]
                    if temp.isnumeric():
                        nexta = int(temp)
                        i += 1
                temparr = []
                while len(newarr) > 0 and newarr[-1][0] != "(":
                    f, c = newarr.pop()
                    temparr.append((f, c * nexta))
                newarr.pop()
                for k in range(0, len(temparr)):
                    newarr.append(temparr[k])
            elif cu.isalpha():
                nexta = 1
                if i + 1 < len(arr):
                    temp = arr[i + 1]
                    if temp.isnumeric():
                        nexta = int(temp)
                        i += 1
                newarr.append((cu, nexta))
            i += 1

        newarr.sort(key=lambda x: (x[0], x[1]))
