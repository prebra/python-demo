# 面向过程
# user1 = {'name': 'zhy', 'ph': 100}
# user2 = {'name': 'dmq', 'ph': 90}
#
#
# def print_role(rolename):
#     print('name is %s, ph is %s' % (rolename['name'], rolename['ph']))
#
#
# print_role(user1)
# print_role(user2)

# 面向对象
class Player():
    def __init__(self, name, ph):
        self.name = name
        self.ph = ph

    def print_role(self):
        print('%s: %s' % (self.name, self.ph))


user1 = Player('zhy', 100)
user2 = Player('dmq', 90)
user1.print_role()
user2.print_role()
