# def add(a, b, c):
#     d = a + b
#     e = d - c
#     print(e)
#
# add(2,4,3)
# 有参数有返回值的函数，计算1--num的累计和,num:形参，传值用。定义两个变量，一个result计算和，一个i循环计算
# def add(num):
#     result = 0
#     i = 1
#     while i<=num:
#         result = result + i
#         i = i+1
#     return result
#
# result = add(100)
# print("1-100的积累和:%d"%result)
# 嵌套函数
# def tem1():
#     # 打印一行横线
#     print("-" * 30)
#
#
# # 打印n行横线
# def tem2(num):
#     i = 0
#     while i < num:
#         tem1()
#         i = i + 1
#
#
# tem2(3)
#写一个函数求三个数的和,写一个函数求三个数的平均值
# def addsum(a,b,c):
#     return a+b+c
#
# def avgsum(a,b,c):
#     avg1 = addsum(a,b,c)/3.0
#     return avg1
#
# result = avgsum(11,22,33)
# print(result)
# def hanshu(a,b):
#     for i in range(a,b):
#
#         print(i)
# hanshu(100,200)
# def runn():
#     b = int(input("请输入一个年份："))
#     if (b%400 ==0) or (b%4==0 and b%100 !=0) :
#         print("是闰年")
#     else:
#         print("不是闰年")
# runn()
# def printinfo(name,age = 35):
#     print("name:%s" %name)
#     print("age:%d"%age)
#
# printinfo(name="miki")
#
# printinfo(age=9,name="join")
# def get_my_info():
#     high = 24
#     weight = 10
#     age = 12
#     return high,weight,age
#
# my_high,my_weight,my_age = get_my_info()
# print(my_high,my_weight,my_age)

#函数作为参数在函数中传递
def addnum(a,b):
    return a+b

def sum(x,y,qwe):
    asd = qwe(x,y)
    print(asd)

sum(10,20,addnum)


