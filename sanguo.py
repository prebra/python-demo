# 读取人物名称
# f = open('name.txt')
# data = f.read()
# print(data.split('|'))
#
# # 读取兵器名称
# f2 = open('weapon.txt')
# i = 1
# for line in f2.readlines():
#     if i % 2 == 1:
#         print(line.strip('\n'))
#     i = i + 1
#
# f3 = open('sanguo_utf8.txt')
# print(f3.read().replace('\n', ''))

# 函数
import re


def find_item(hero):
    with open('sanguo_utf8.txt') as f:
        data = f.read().replace('\n', '')
        name_num = re.findall(hero, data)
        # print('主角 %s 出现 %s 次' %(hero, len(name_num)))
    return len(name_num)


# 读取人物名称
name_dict = {}
with open('name.txt') as f:
    for line in f:
        names = line.split('|')
        for n in names:
            name_num = find_item(n)
            name_dict[n] = name_num
name_sorted = sorted(name_dict.items(), key=lambda item: item[1], reverse=True)
print((name_sorted[0:10]))
