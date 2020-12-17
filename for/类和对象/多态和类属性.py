# class Person(object):
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def eat(self):
#         # print(self.name)
#         # print(self.age)
#         print("肯德基")
#
#
# class Dog(object):
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def eat(self):
#         # print(self.name)
#         # print(self.age)
#         print("肯德基")
#
# def func(object):
#     print(object.name)
#     print(object.age)
#     object.eat()
#     print("=="*10)
#
#
# xiaoming = Person("小明",20)
# wangcai = Dog("旺财",2)
# func(xiaoming)
# func(wangcai)
# class person(object):
#     address = "上海"
#     __age = 20
#     def __init__(self):
#         self.name = "xiaowang"
#         self.age = 20
#
#
# p = person()
# print(person.address)
# print(p.address)
# # p.name = "xiaoming"
# # p.age = 30
# p.address = "北京"
# print(p.address)
# # print(p.name)
# # # print(p.age)
# print(person.address)
# # print(person.name)
# # print(person.age)

#类方法中的属性可以使用对象调用不能用类名调用，类里的属性两者都可以调用
class People(object):
    country = 'china' #类属性


print(People.country)
p = People()
print(p.country)
p.country = 'japan'
print(p.country)  # 实例属性会屏蔽掉同名的类属性
print(People.country)
del p.country  # 删除实例属性
print(p.country)




