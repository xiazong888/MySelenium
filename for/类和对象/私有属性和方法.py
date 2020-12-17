# class Master(object):
#     def __init__(self):
#         self.kongfu = "古法煎饼果子配方"
#
#     def make_cake(self):
#
#         print("使用<%s>制作煎饼果子"%self.kongfu)
#
# class Prentice(Master):
#     def __init__(self):
#         self.kongfu = "猫式煎饼果子配方"
#         self.__monkey = 10000
#     def make_cake(self):
#         print(self.__monkey)
#         print("使用<%s>制作煎饼果子" % self.kongfu)
#
#     def __info(self):
#         print(self.kongfu)
#         print(self.__monkey)
#     #
#     def make_oldcake(self):
#         # Master.make_cake(self)
#         # School.make_cake(self)
#         # super(Prentice, self).make_cake()
#         self.__info()
#
#
# damao = Prentice()
# damao.make_cake()
# damao.make_oldcake()
class person(object):
    def __init__(self):
        self.__age = 20

    def get_age(self):
        return self.__age
    def set_age(self,age):
        self.__age = age

damao = person()
damao.get_age()
print(damao.get_age())
damao.set_age(30)
print(damao.get_age())

