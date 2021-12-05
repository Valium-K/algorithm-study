import re

if __name__ == '__main__':
    dart_result = '1T2D3D#'
    pattern = re.compile('[0-9]+[SDT][*#]?')
    output = 0

    for i in pattern.findall(dart_result):
        i_list = list(i)

        bonus = -1
        bonus_index = -1
        if 'S' in i:
            bonus = 1
            bonus_index = i_list.index('S')
        elif 'D' in i:
            bonus = 2
            bonus_index = i_list.index('D')
        else:
            bonus = 3
            bonus_index = i_list.index('T')

        option = 1
        if len(i[bonus_index:]) > 1:
            if i[-1] == '*':
                output *= 2
                option = 2
            elif i[-1] == '#':
                option = -1

        output += (int(i[:bonus_index]) ** bonus) * option

    print(output)