import re

def solution(s):
    semantic_num = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    found_s = re.findall('one|two|three|four|five|six|seven|eight|nine|[0-9]', s)

    for i in range(len(found_s)):
        if found_s[i] in semantic_num:
            found_s[i] = semantic_num[found_s[i]]

    return ''.join(found_s)

if __name__ == '__main__':
    print(solution('123'))