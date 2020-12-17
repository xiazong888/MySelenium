# # 01 创建一个a文件，写入hello world,先打开给权限后写入
# a_f = open("a.txt","w")
# a_f.write("hello world")
# # 02 打开a文件，读取a文件内容，先打开给权限，后读取
# a_f = open("a.txt","r")
# result = a_f.read()
# # 03 创建一个b文件，写入hello附件，先打开给权限后写入
# b_f = open("b.txt","w")
# b_f.write("hello附件")
# # 04 把b文件写入到a文件中
# b_f.write(result)
# # 04 关闭文件
# a_f.close()
# b_f.close()
#准备一个文件
#1,打开文件,2，写文件，关闭文件
# h = open("hm.txt","w")
# h.write("hello world!!!!!\nhello world!!!!!\nhello world!!!!!")
# h.close()
#制作文件的备份，1，打开源文件，2读取源文件，3创建备份文件，4把源文件写入到备份文件，关闭文件
# x = open("hm.txt","r")
# result = x.read()
# copy = open("cp.txt","w")
# copy.write(result)
# x.close()

import os
#文件重命名
# os.rename("a.txt","a_cp.txt")
#删除文件
# os.remove("a_cp.txt")
#创建文件夹
# os.mkdir("asd")
#删除文件夹
# os.rmdir("asd")
#获取当前目录
# r = os.getcwd()
# print(r)
#获取目录列表
# o = os.listdir("./")
# print(o)

#1，创建一个文件夹，2，进入文件夹，在文件夹里创建10个文件（循环）
# os.chdir("asd")
# print(os.getcwd())
# for i in range(1,11):
#     f = open("hm%d.txt"%i,"w")
#     f.close()

# for i in range(1,11):
#     os.remove("hm%d"%i)
# os.chdir("asd")
#批量修改文件名,1,获取当前目录列表 2，遍历my_list,
my_list = os.listdir()
# print(my_list)
for file_name in my_list:
    new_file_name = file_name.replace(".txt","[中国].txt")
    # 修改文件名
    os.rename(file_name,new_file_name)















