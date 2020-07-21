# enumate 函数的介绍
# def dictVarArgs(arg1, arg2='default_parameters', *args):
#     """
#     This function is a sample of input parameters.
#     """
#     print('-' * 10)
#     print('formal arg1:', arg1)
#     print('formal arg2:', arg2)
#     for xth, eachXtrArg in enumerate(args):
#         print(xth + 3, 'th args:', eachXtrArg)
#
#
# dictVarArgs('China', 'USA')
# dictVarArgs(10, 20, 30, 40, '?')

# 顺序：必选（位置）参数、默认参数、可变参数、命名关键字参数、关键字参数

# your code here
# def print_string(*args, sep=' ', end='\n'):
#     """
#     输入多参并返回字符串
#     parameters:
#         args: 多参数输入
#         sep: 连接符，默认为一个空格
#         end: 结束符，默认为一个换行
#     return:
#         resp: 最终返回的字符串
#     """
#     resp = ''
#     length = len(args)
#     if length == 1:
#         return args[0] + end
#     else:
#         for i, arg in enumerate(args):
#             if i < length - 1:
#                 resp += arg + sep
#             else:
#                 resp += arg + end
#         return resp
#
#
# print(print_string('sss'))
# print(print_string('sss', 'aaa'))
# print(print_string('sss', 'aaa', ','))
# print(print_string('sss', 'aaa', ',', sep='-'))
# print(print_string('sss', 'aaa', ',', sep='-', end='***'))

# 斐波那契
# def fibonacci(n):
#     """
#     输入任意整数n，打印前n项的斐波那契数列
#     斐波那契数列：1、1、2、3、5、8、13、21、34……
#     parameter:
#         n: 输入的任意整数n
#     return:
#         f: 前n个斐波那契数列
#     """
#     if not isinstance(n, int) or n <= 0:
#         return "请输入正整数"
#     f = [1, 1]
#     if n == 1:
#         return f[n - 1]
#     if n == 2:
#         return f
#     for i in range(2, n):
#         f.append(f[i - 1] + f[i - 2])
#     return f
#
#
# print(fibonacci(12))
