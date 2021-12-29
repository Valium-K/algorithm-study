import re, heapq

def solution(info, query):
    # [-score, [lang  work   work_exp   food]]
    db = []
    for row in info:
        r = list(re.findall("[a-z]+|\d+", row))
        heapq.heappush(db, ([-int(r[4])] + [r[:4]]))

    output = []
    for q in query:
        cur = 0
        lang, work, work_exp, food_score = q.split(" and ")
        food, score = food_score.split()

        for neg_score, row in db:
            print(row, -neg_score)
            if int(score) > -int(neg_score):
                continue
            if (row[0] == lang or lang == '-') and \
                    (row[1] == work or work == '-') and \
                    (row[2] == work_exp or work_exp == '-') and \
                    (row[3] == food or food == '-'):
                cur += 1

        output.append(cur)
    return output


if __name__ == '__main__':
    print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
             ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))