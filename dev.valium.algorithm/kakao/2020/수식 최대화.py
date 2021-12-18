from itertools import permutations

def proc(sub_expression, ops):
    if len(ops) == 1:
        return sub_expression

    output = ""
    for exp in sub_expression.split(ops[0]):
        output = output + ops[0] + "(" + proc(exp, ops[1:]) + ")"

    return output[1:]

def solution(expression):
    op_permutations = list(permutations(['*', '-', '+'], 3))

    output = 0
    for ops_priority in op_permutations:
        op_set = []
        for op in ops_priority:
            if op in expression:
                op_set.append(op)

        cur = abs(eval(proc(expression, list(reversed(op_set)))))

        if cur > output:
            output = cur

    return output
if __name__ == '__main__':
    print(solution("100-200*300-500+20"))