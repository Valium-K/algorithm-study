output = 123456789
def can_transfer(begin, word):
    nmc = 0
    for i in range(len(word)):
        if nmc <= 1:
            if begin[i] != word[i]:
                nmc += 1
        else:
            return False
    if nmc >= 2:
        return False
    else:
        return True
def proc(begin, target, visited, words, depth):
    global output

    if begin == target:
        if depth < output:
            output = depth
        return

    for i, word in enumerate(words):
        if not visited[i] and can_transfer(begin, word):
            visited[i] = True
            proc(word, target, visited, words, depth + 1)
            visited[i] = False

def solution(begin, target, words):
    global output

    proc(begin, target, [False] * len(words), words, 0)

    if output == 123456789:
        return 0
    else:
        return output

if __name__ == '__main__':
    solution("hit" ,	"cog" ,	["hot", "dot", "dog", "lot", "log", "cog"])
    print(output)
