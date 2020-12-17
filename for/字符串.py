# my_str = 'hello'
# # s = my_str[1]
# # print(s)
# l = len(my_str)
# index = 0
# while index < l:
#     s = my_str[index]
#     print(s)
#     index = index + 1
# 练习题提示用户进行输入数据，获取用户的数据数据（需要获取2个），
# 对获取的两个数字进行减法运行，并输出相应的结果
# data = input("请输入第一个数据")
# a = int(data)
# data2 = input("请输入第二个数据")
# b = int(data2)
# s = a - b
# print(s)
# print("==================================")
# name = input("姓名:")
# qq = input("QQ:")
# phone = input("手机号:")
# comAddr = input("公司地址：")
# print("==================================")

# name = input("用户名：")
# pwd = input("密码：")
# if name == "xx" and pwd == "xxx":
#     print("欢迎进入xxxx的世界")
# else:
#     print("用户名或密码错误")

# x = 0
# while x < 4:
#     y = 0
#     while y < x:
#         print("*", end=" ")
#         y = y + 1
#     print("*")
#     x = x + 1
# i = 4
# while 0 <= i <= 4:
#     j = 1
#     while 1 <= j <= i:
#         print("*", end=" ")
#         j = j + 1
#     print("*")
#     i = i - 1
str1 = '1234567890'
# print(str1[2])

# # print(str1[l-1])
# # print(l)
# i = 0
# while 0<=i <= l-1:
#     s = str1[i]
#     print(s,end=" ")
#     i = i + 2
l = len(str1)
# i = 1
# # 定义一个比较值
# b = str1[1]
# # 循环遍历所有元素
# while i <= l:
#     # 遍历比较选出最大值
#     for max in str1:
#         if b>max:
#             pass
#         else:
#             b = max
#     i += 1
# print(b)
str = "hello world"
i = 0
for s in str:
    print("%s:%d"%(s,i),end=" ")
    i= i+1
