# 尽管可以使用 for in 遍历元组
# 在开发中，更多的应用场景是：
# 函数的 参数 和 返回值 一个函数可以接受 任意多个参数，或者 依次返回多个数据
# 格式字符串，格式化字符串后面的()本质上就是一个元组
# 让列表不可以被修改，以保护数据的安全

info = ("zhangsan", 18)
print("%s 的年龄是 %d" % info)