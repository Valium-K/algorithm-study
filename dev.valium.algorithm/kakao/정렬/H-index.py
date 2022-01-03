def solution(citations):
    citations.sort()
    h_idxes = [0]
    for h in range(citations[-1]):
        if len(list(filter(lambda x: x >= h, citations))) >= h >= len(list(filter(lambda x: x < h, citations))):
            h_idxes.append(h)
        else:
            return h_idxes[-1]
    return h_idxes[-1]
if __name__ == '__main__':
    print(solution([0]))