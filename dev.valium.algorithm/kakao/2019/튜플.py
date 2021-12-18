import re

def solution(s):
    out_dict = {}

    for ns in re.findall("\d+", s):
        try:
            out_dict[int(ns)] += 1
        except Exception:
            out_dict[int(ns)] = 1

    return list(map(lambda x: x[0], sorted(out_dict.items(), key=lambda x: x[1], reverse=True)))