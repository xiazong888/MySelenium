# 行1-9，列1-9
# x = 1
# while x <= 9:
#     y = 1
#     while y <= x:
#         print("%d*%d=%-2d" % (x, y, x * y), end=" ")
#         y = y + 1
#     print()
#     x = x + 1
# 打印三角形*
x = 1
while x <= 5:
    y = 1
    while y < x:
        print("*", end=" ")
        y = y + 1
    print("*")
    x = x + 1


