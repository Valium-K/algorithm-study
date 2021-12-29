from itertools import combinations

def solution(relation):
    output = []
    to_visit_index = []
    for i in range(1, len(relation[0]) + 1):
        for j in combinations(range(len(relation[0])), i):
            to_visit_index.append(set(j))

    visited = [False] * len(to_visit_index)
    for tvi, cur_indexes in enumerate(to_visit_index):
        if visited[tvi]:
            continue
        visited[tvi] = True
        unique_set = set()
        flag = False
        for i in range(len(relation)):
            cur_values = ""
            for cur_index in cur_indexes:
                cur_values += str(relation[i][cur_index])


            # 중복아니면
            if cur_values not in unique_set:
                unique_set.add(cur_values)
            else:
                # 중복이면
                flag = True
                break

        if not flag:
            output.append(cur_indexes)
            for cur in range(tvi, len(to_visit_index)):
                if cur_indexes.issubset(to_visit_index[cur]):
                    visited[cur] = True

    return len(output)
if __name__ == '__main__':
    solution([["100","ryan","music","2"],
              ["200","apeach","math","2"],
              ["300","tube","computer","3"],
              ["400","con","computer","4"],
              ["500","muzi","music","3"],
              ["600","apeach","music","2"]])