# class person(object):
#     __country = "中国"
#     # @classmethod 类方法
#     @ staticmethod
#     def get_country():
#         return person.__country
#     # @classmethod 类方法
#     @staticmethod
#     def set_country(country):
#         person.__country = country
# # 类方法，对类属性修改可以用@classmethod进行修饰
# # print(person.get_country())
# # person.set_country("中华")
# # print(person.get_country())
# p = person()
# print(p.get_country())
# print(person.get_country())
# p.set_country("中华")
# print(p.get_country())
# print(person.get_country())
class person(object):
    #new必须有返回值，而且是父类的
    def __new__(cls, *args, **kwargs):
        print("__new__")
        return object.__new__(cls)

    def __init__(self):
        print("这是__init__方法")
        self.name = "小明"
    def __str__(self):
        return "名字:%s"%self.name
    def __del__(self):
        print("结束")
xiaoming = person()
print(xiaoming)













