# class Lijing:  # 李靖
#     # 初始化函数，为每个实例创建4个参数（其中有3个参数有默认值）
#     def __init__(self, name, weapons=[], power=10):
#         self.name = name
#         self.weapons = weapons
#         self.power = power
#
#     def count_fight(self, weapon, weapon_power):
#         self.weapons.append(weapon)
#         self.power += weapon_power  # 总战力=武器战力之和
#
#
# class Nezha(Lijing):  # 哪吒
#     def __init__(self, name='哪吒', weapons=['混天绫', '乾坤圈'], power=50):
#         super(Nezha, self).__init__(name=name, weapons=weapons, power=power)
#
#     def count_fight(self, weapon, weapon_power):
#         super().count_fight(weapon, weapon_power)
#
#
# class Muzha(Lijing):  # 木吒
#     def __init__(self, name, weapons=['木剑'], power=5):
#         super(Muzha, self).__init__(name, weapons=weapons, power=power)
#
#     def count_fight(self, weapon, weapon_power):
#         super().count_fight(weapon, weapon_power)

# format
# if __name__ == '__main__':
#     lijing = Lijing('李靖', weapons='宝塔')
#     nezha = Nezha()
#     print(lijing.power, lijing.weapons)
#     print(nezha.weapons, nezha.name)

# print('{1} {0} {0}'.format('aaa', 1))
# print('{} {}'.format('aaa', 1))
# print('{name} {age}'.format(age=5, name='QHL'))
#
# class person:
#     name = 'Helo'
#     age = 32
# print('{person.name} {person.age}'.format(person=person))

# f-string
# def mult_two_num(a):
#     print(10 + a)
# f"{mult_two_num(9)}"
#
# a = "f-"
# b = "string"
# print(f"{80*10},{{80*10}},{a + b}")

# map
# l = [2, 3, 4, 5, 6]
# def func(e):
#     return e * 2
# print(list(map(func, l)))
# print(list(map(lambda e: e * 2, l)))
# help(map)
# x = set([1, 2, 3, 4, 5])
# y = set([2, 3, 4, 5, 6])
# z = x & y
# print(' '.join(map(str,z)))

# reduce
# from functools import reduce
# l = [23, 6, 7, 34, 2]
# print('列表和为：', reduce(lambda x, y: x + y, l))
# help(reduce)

# filter
# def isEmpty(obj):
#     return obj != '' and obj != ' ' and obj != None
# print(list(filter(isEmpty, ['', '1', 2, None, ' ', 'b'])))

# a = [('app', 3), ('a', 16), ('bob', 34), ('crowley', 8), ('david', 12), ('eva', 5)]
# b = sorted(a, key=lambda x:x[1])
# print(b)

# Decorator
# from datetime import datetime
# def log(func):
#     def wrapper(*args, **kw):  # 固定写法
#         print('calling function:', func.__name__, '\t at ', datetime.now())
#         return func(*args, **kw)
#
#     return wrapper
#
# @log
# def add_user(name):
#     # some code
#     print('create user:', name)
#
# @log
# def remove_user(name):
#     # some code
#     print('remove user:', name)
#
# if __name__ == '__main__':
#     add_user('chen'), remove_user('song')
#
#

# 1，正则&爬虫&文件处理
# import re
# import requests
# from bs4 import BeautifulSoup
#
# # 以前遇到过的函数
# def build_url(city_coding, year=None, month=None):
#     """
#     创建网页链接
#     paramters:
#         city_coding: 城市名称(英文)
#         year: 年份
#         month: 月份
#     return:
#         url: 可访问的链接
#     """
#     BASE = 'http://www.tianqihoubao.com/aqi/'
#     city_base_url = BASE + '{}.html'
#     city_date_base_url = BASE + '{}-{}{}.html'
#
#     if year is not None and month is not None:
#         month = str(month) if month >= 10 else '0' + str(month)
#         return city_date_base_url.format(city_coding, year, month)
#     else:
#         return city_base_url.format(city_coding)
#
#
# def parse(url, city_name):
#     """
#     抓取网页信息
#     parameters:
#         url: 需要抓取的网页链接
#         city_name: 城市名称(用于数据标识)
#     returns:
#         result: 抓取的信息
#     """
#     response = requests.get(url)
#     if response.ok:
#         html = response.text
#
#         soup = BeautifulSoup(html)
#         data_table = soup.table
#
#         content = data_table.contents
#
#         result = []
#         for index, c in enumerate(content[1::2]):
#             if index == 0:
#                 result.append(tuple(['城市'] + c.text.split()))
#             else:
#                 result.append(tuple([city_name] + c.text.split()))
#         return result
#
#     else:
#         if response.status_code == 403:
#             print('403 Forbidden! 抓取太快你被拉黑啦~')
#
#
def save(data, file):
    # 完成数据保存到文件
    # your code here
    # 提示：用什么方法将数据写入文件？
    with open(file, 'a') as f:
        for data in data:
            x = str(data).strip("()")
        #     x = re.sub("[(|)]", "", str(data))  # 每条数据由元组转为字符串格式，删除元组转为字符串后的括号
        #     y = re.sub(",", " ", x)  # 将逗号替换为空格
        #     f.write(y + "\n")  # 写入文件
    print('Data has saved in ', file)
#
#
# if __name__ == '__main__':
#     datas = []
#     for i in range(1, 2):
#         url = build_url('hangzhou', 2019, i)
#         data = parse(url, '杭州')
#         datas.extend(data)
#     # 只保留质量等级优 良 数据
#     data = list(filter(lambda x: re.search('优|良', x[2]), datas[1:]))
#     data.insert(0, datas[0])  # 添加表头
#     # 保存数据
#     save(data, './data.txt')



"""
2，西瓜数据集
a.添加编号列，并将数据集写入到`machine_learning.csv`文件，使用pandas读取验证文件是否有效(无错即可)。
b.添加一条记录，`青绿 硬挺 浊响 稍糊 平坦 硬滑 0.666 0.111 好`
c.再使用普通文件读取将数据集读取出来，列名读取到`columns`，数据(带编号)读取到`datalist`
d.在所有数据中过滤出色泽='浅白'的数据
e.在所有数据中过滤出密度大于0.5的数据
"""
import pandas as pd

dataset = \
"""色泽 根蒂 敲声 纹理 脐部 触感 密度 含糖率 好瓜
青绿 蜷缩 浊响 清晰 凹陷 硬滑 0.697 0.460 是
乌黑 蜷缩 沉闷 清晰 凹陷 硬滑 0.774 0.376 是
乌黑 蜷缩 浊响 清晰 凹陷 硬滑 0.634 0.264 是
青绿 蜷缩 沉闷 清晰 凹陷 硬滑 0.608 0.318 是
浅白 蜷缩 浊响 清晰 凹陷 硬滑 0.556 0.215 是
青绿 稍蜷 浊响 清晰 稍凹 软粘 0.403 0.237 是
乌黑 稍蜷 浊响 稍糊 稍凹 软粘 0.481 0.149 是
乌黑 稍蜷 浊响 清晰 稍凹 硬滑 0.437 0.211 是
乌黑 稍蜷 沉闷 稍糊 稍凹 硬滑 0.666 0.091 否
青绿 硬挺 清脆 清晰 平坦 软粘 0.243 0.267 否
浅白 硬挺 清脆 模糊 平坦 硬滑 0.245 0.057 否
浅白 蜷缩 浊响 模糊 平坦 软粘 0.343 0.099 否
青绿 稍蜷 浊响 稍糊 凹陷 硬滑 0.639 0.161 否
浅白 稍蜷 沉闷 稍糊 凹陷 硬滑 0.657 0.198 否
乌黑 稍蜷 浊响 清晰 稍凹 软粘 0.360 0.370 否
浅白 蜷缩 浊响 模糊 平坦 硬滑 0.593 0.042 否
青绿 蜷缩 沉闷 稍糊 稍凹 硬滑 0.719 0.103 否"""

# 将数据写入csv文件
# your code here
file = r'machine_learning.csv' # 文件名称，学员可修改或不修改

# 向csv文件中加入一条新的数据（数据已给出）
# your code here
# 注意每一行数据的间隔符号是什么
inser_data = '18 青绿 硬挺 浊响 稍糊 平坦 硬滑 0.666 0.111 是'

# 查看全体数据
df = pd.read_csv(file)
print(df.head())

# 读取文件存储的数据
# your code here
# columns是指列标签
# datalist指全体数据内容，每一行数据应为一个列表
columns = []
datalist = []

# 验证数据信息是否相符
print(columns==['编号', '色泽', '根蒂', '敲声', '纹理', '脐部', '触感', '密度', '含糖率', '好瓜'])
print(datalist[-1]==['18', '青绿', '硬挺', '浊响', '稍糊', '平坦', '硬滑', '0.666', '0.111', '是'])

# 在所有数据中过滤出色泽='浅白'的数据
# 在所有数据中过滤出密度大于0.5的数据
# your code here
