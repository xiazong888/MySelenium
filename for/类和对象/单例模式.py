class Singleton(object):
    __instance = None
    __is_first = True
    def __new__(cls,name,age):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self,name,age):
        if self.__is_first:
            self.name = name
            self.age = age
            Singleton.__is_first = False

a = Singleton("xiaoming",20)
b = Singleton("xiaohong",8)
print(a.name,a.age)
print(b.name,b.age)
print(id(a))
print(id(b))

print(a.age)
print(b.age)
a.age = 17
print(b.age)
# 单例对的好处就是节约内存