# 字符串常见操作

# mystr = 'hello world itcastw'
#
# # a = mystr.find('itcast')
#
# # b = mystr.index('hello')
# # c = mystr.count('w')
# d = mystr.replace('hello','Hello')
# e = mystr.title()
# print(e)

#列表的循环遍历
strlist = ['xiaowang','xiaozhang','xiaohua']

# for list in strlist:
#     print(list)

length = len(strlist)

# i = 0
# while i<length:
#     print(strlist[i])
#     i = i+1

#列表的常见操作，增，删，改
#添加一个元素
mylist = ['xiaowang','xiaozhang','xiaohua']
# mylist.append('xiaoer')
# b=[1,3]
# mylist.extend(b)
# mylist.insert(1,'xiaoming')
# mylist[1] = 'xiaogang'
# for a in mylist:
#     print(a)
a = 'xiaqang'
if  a in mylist:
    print(a)
else:
    print('没有找到')

del mylist[2]

print(mylist)
a=[1,2,3,4,5]
a.sort(reverse=True)
print(a)

