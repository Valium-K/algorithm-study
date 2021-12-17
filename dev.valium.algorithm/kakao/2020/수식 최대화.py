import copy
import re
from itertools import permutations
def proc(num1, op, num2):
    if op == '-':
        return num1 - num2
    elif op == "+":
        return num1 + num2
    elif op == "*":
        return num1 * num2
    else:
        if num2 == 0:
            return 0
        else:
            return num1 / num2
def solution(expression):
    nums = list(map(int, (re.findall('[\d]+', expression))))
    chars = list((re.findall('[^\d]+', expression)))
    char_permutations = list(permutations(set(chars), len(set(chars))))

    stack = []
    for i in range(len(chars)):
        stack.append(nums[i])
        stack.append(chars[i])
    stack.append(nums[-1])

    print(stack)
    output = 0
    # (-, +, *)
    for char_permutation in char_permutations:
        cur = 0
        tempStack = copy.deepcopy(stack)

        for op in char_permutation:
            for i in range(len(tempStack)):
                if op == tempStack[i]:
                    temp = proc(tempStack[i - 1], op, tempStack[i + 1])
                    tempStack[i - 1] = temp
                    tempStack[i + 1] = temp
                    cur += temp

        if abs(cur) > output:
            output = abs(cur)

    return output
if __name__ == '__main__':
    print(solution("50*6-3*2"))