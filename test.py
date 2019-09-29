# 网络带宽计算

bandwidth = 100
ratio = 8

# print(bandwidth/ratio)

# 记录生肖
chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'

# 切片操作 :
# print(chinese_zodiac[1:3])

year = 1994
# print(chinese_zodiac[year % 12])

# 成员关系操作符 [not] in
# print('猴' in chinese_zodiac)

# 连接操作 +
#  print(chinese_zodiac + chinese_zodiac)

# 重复操作 *
# print(chinese_zodiac * 3)

# 元组
zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座',
             u'巨蟹座', u'狮子座', u'处女座', u'天秤座', u'天蝎座', u'射手座')
zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22),
             (7, 23), (8, 23), (9, 23), (10, 23), (11, 22), (12, 22))

# (month, day) = (9, 18)
# zodiac_day = filter(lambda x: x<=(month, day), zodiac_days)
# zodiac_len = len(list(zodiac_day)) % 12
# print(zodiac_name[zodiac_len])

# 列表
# a_list = ['abc','zyx']
# a_list.append('x')
# a_list.remove('abc')
# print(a_list)

# for
# for year in range(2000, 2019):
#     print('%s 年的生肖是 %s' %(year, chinese_zodiac[year % 12]))

# while
# import time
# num = 5
# while True:
#     num = num + 1
#     if num == 7:
#         continue
#     if num > 10:
#         break
#     print(num)
#     time.sleep(1)

# int_month = int(input('请输入月份：'))
# int_day = int(input('请输入日期：'))
#
# for zd_num in range(len(zodiac_days)):
#     if zodiac_days[zd_num] >= (int_month, int_day):
#         print(zodiac_name[zd_num])
#         break
#     elif int_month == 12 and int_day > 23:
#         print(zodiac_name[0])
#         break

# 列表推导式
# alist = []
# for i in range(1, 11):
#     if (i % 2 == 0):
#         alist.append(i*i)
# print(alist)
# plist = [i*i for i in range(1, 11) if(i % 2) == 0]
# print(plist)

# 字典推导式
# z_num = {}
# for i in zodiac_name:
#     z_num[i] = 0
z_num = {i: 0 for i in zodiac_name }
print(z_num)


