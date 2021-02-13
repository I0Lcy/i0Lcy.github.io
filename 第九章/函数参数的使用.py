# 在函数名的后面的小括号内部填写 参数
# 多个参数之间使用 , 逗号分隔


def sum2_2_num(num1,num2):
    result = num1 + num2
    print("%d + %d = %d" % (num1,num2,result))

sum2_2_num(20,30)

# 参数的作用
# 函数 把 具有独立功能的代码块 组织为一个小模块，在需要的时候调用
# 函数的参数，增加函数的通用性，针对相同的数据处理逻辑，能够使用更多的数据

# 1.在函数内部，吧参数当作变量使用，进行需要数据处理
# 2.函数调用时，按照函数定义的参数顺序，把希望在函数内部处理的数据，通过参数传递
