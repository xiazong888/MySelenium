#学生管理系统
# 定一个列表，用来存储所有的学生信息(每个学生是一个字典)
info_list = []

def menu_info():
    print("---------------------------")
    print("      学生管理系统 V1.0")
    print(" 1:添加学生")
    print(" 2:删除学生")
    print(" 3:修改学生")
    print(" 4:查询学生")
    print(" 5:显示所有学生")
    print(" 6:退出系统")
    print("---------------------------")

def add_new_info():
    """添加学生信息"""
    global info_list

    new_name = input("请输入姓名:")
    new_tel = input("请输入手机号:")
    new_qq = input("请输入QQ:")

    for stu_list in info_list:
        if stu_list["name"]==new_name:
            print("用户名已存在")
            return  # 如果一个函数只有return就相当于让函数结束，没有返回值

    # 定义一个字典，用来存储用户的学生信息(这是一个字典)
    info={}

    # 向字典中添加数据
    info["name"] = new_name
    info["tel"] = new_tel
    info["qq"] = new_qq
    # 向列表中添加这个字典
    s = info_list.append(info)
    # print(s)
# add_new_info()
# def update_stu():
#
#
# def del_stu():
#
#
# def search_stu():
#
# #控制整个流程
# def main():