import re

def get_multi_list_of(s):
    pattern = '[a-z][a-z]'
    temp = []

    for i in range(len(s)-1):
        target_str = str.lower(s[i:i+2])
        # 특수문자면 스킵
        if not re.match(pattern, target_str):
            continue

        temp.append(target_str)

    return temp

if __name__ == '__main__':
    str1 = 'aa1+aa2'
    str2 = 'AAAA12'

    multi_str1 = get_multi_list_of(str1)
    multi_str2 = get_multi_list_of(str2)
    u_set = set(multi_str1)
    u_set = u_set.union(set(multi_str2))

    a = 0
    b = 0
    for cur_str in u_set:
        s1_count = multi_str1.count(cur_str)
        s2_count = multi_str2.count(cur_str)

        a += min(s1_count, s2_count)
        b += max(s1_count, s2_count)

    if a == 0 and b == 0:
        print(65536)
    else:
        print(int((a / b) * 65536))