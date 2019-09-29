# 将小说的主要人物记录在文件中
# file1 = open('name.txt', 'w')
# file1.write('诸葛亮')
# file1.close()
#
# file2 = open('name.txt')
# print(file2.read())
# file2.close()
#
# file3 = open('name.txt', 'a')
# file3.write('刘备')
# file3.close()

# 读取一行
# file4 = open('name.txt')
# print(file4.readline())
#
# # 逐行读取
# file5 = open('name.txt')
# for i in file5.readlines():
#     print(i)
#     print('=========')

file6 = open('name.txt')
print('当前文件指针的位置 %s' % file6.tell())
print('当前读取到的一个字符，字符内容是 %s' % file6.read(1))
print('当前文件指针的位置 %s' % file6.tell())
# 第一个参数代表偏移的位置， 第二个参数 0表示你从文件开头偏移、1表示从当前位置偏移、2从文件结尾
file6.seek(5, 1)
print('进行了seek操作')
print('当前文件指针的位置 %s' %file6.tell())
print('当前读取到的一个字符，字符内容是 %s' % file6.read(2))
file6.close()
