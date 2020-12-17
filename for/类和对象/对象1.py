# class hero(object):#新式定义类
#     def move(self):
#         print("会走")
#
# wukong = hero()
# wukong.move()
# wukong.name = "悟空"
# wukong.hp = 3000
# wukong.atk = 400
# print("英雄%s的攻击力为%d"%(wukong.name,wukong.atk))
# class Dog(object):
#     def __init__(self):
#         self.name = "旺财"
#         self.color = "白色"
#
#     def eat(self):
#         print("会吃骨头")
#
#     def info(self):
#         print("名字:%s"%self.name)
#         print("颜色:%s" % self.color)
# wangcai = Dog()
# wangcai.info()
# wangcai.eat()
# class Hero(object):
#     def __init__(self,name,hp,atk,skill):
#         self.name = name
#         self.hp = hp
#         self.atk = atk
#         self.skill = skill
#
#     def move(self):
#         print("%s还有5秒钟到达战场.."%self.name)
#
#     def attack(self):
#         print("释放了一招%s"%self.skill)
#     def __str__(self):
#         return "英雄%s,生命值%d,攻击力%d,技能%s"%(self.name,
#                                             self.hp,
#                                             self.atk,
#                                             self.skill
#                                             )
#     def __del__(self):
#         print("bye")
# # 实例化英雄对象时，参数会传递到对象的__init__()方法里
# wukong = Hero("亚瑟",3000,400,"大宝剑")
#
# monkey1 = wukong
# monkey2 = wukong
#
# print("%d 被删除1次" % id(wukong))
# del(wukong)
#
# print("%d 被删除1次" % id(monkey1))
# del(monkey1)
#
# print("%d 被删除1次" % id(monkey2))
# del(monkey2)
class shifu(object):
    # def __init__(self):
    #     self.kongfu = "古法煎饼果子"
    def make_cake(self):
        print("按照<古法>制作煎饼果子")
class peixun(object):
    # def __init__(self):
    #     self.kongfu = "现代煎饼果子"

    def make_cake(self):
        print("按照<现代>制作煎饼果子")

class tudi(peixun,shifu):
    def __init__(self):
        self.kongfu = "猫式煎饼果子"
    def make_cake(self):
        print("按照<%s>制作煎饼果子" % self.kongfu)
    def make_newcake(self):

        # peixun.make_cake(self)

        # super(tudi, self).make_cake()
        super().make_cake()
    # def make_oldcake(self):
    #     shifu.make_cake(self)


damao = tudi()
damao.make_cake()
# damao.make_oldcake()
damao.make_newcake()
# damao.make_cake()
# damao = shifu()
# damao.make_cake()
# print(damao.kongfu)
#
# damao = peixun()
# damao.make_cake1()
# print(damao.kongfu1)















