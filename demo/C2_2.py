# l1 = [1, 2, 3, 4]
# for x in l1:
#     if x < 3:
#         print(x)
#     else:
#         print("error")
# print("----------")

##
# while-loop
# i = 0
# while i < 4:
#     print(i)
#     i += 1

##
# for-loop
# list1, list2, list3 = [], [], []
# for i in range(10):
#     list1.append(i)
# print("l1 = " + list1.__str__())
#
# # range(start, end)
# for b in range(10, 20):
#     list2.append(b)
# print("l2 = " + list2.__str__())


##
# range
# range(start, end, step = 2)
# for c in range(1, 10, 2):
#     list3.append(c)
# print("l3 = " + list3.__str__())

##
# iter迭代器
# a = list(range(1, 10))
# ite = iter(a)
# print(next(ite))
# print(next(ite))

##
# iter迭代器
# b = range(1, 10)
# ite = iter(b)
# x = next(ite)
# while x is not None:
#     print(x)
#     x = next(ite)

##
# 列表解析
# x = [2 ** i for i in range(5, 10)]
# print(x)

# income = [1, 2, 3, 4, 5, 6, 7]
# expend = [2, 3, 4, 3, 2, 1, 3]

##
# 作业1
# income = []
# expend = []
# for i in range(1, 15):
#     if i <= 7:
#         income.append(int(input('输入第' + str(i) + '天的收入: ')))
#     else:
#         expend.append(int(input('输入第' + str(i - 7) + '天的支出: ')))
# print("7天的收入：", str(income).strip('[').strip(']'))
# print("7天的支出：", str(expend).strip('[').strip(']'))
# daily_balance = [(income[i] - expend[i]) for i in range(7)]
# daily_dict = dict(zip(range(1, 8), daily_balance))
# print("每天的结余(list形式)：", daily_balance)
# print("每天的结余(dict形式)：", daily_dict)
# for i, balance in daily_dict.items():
#     print("第", i, "天的结余为", balance)
# print("最终的结余：", sum(daily_balance))

##
# 作业2
# is_login = {0: "登录账户", 1: "退出账户"}
# option = {0: "查询余额", 1: "存款", 2: "取款", 3: "退出"}
# bank = {"张三": 2000, "李四": 0, "王五": 30000}
# while True:
#     print("请选择账户操作：")
#     print("0:登录账户\n1:退出账户/结束会话")
#     # 账户登录操作确认
#     login = input()
#     if login == '0':
#         print("请输入您的账户名：")
#         account = input()
#         # 账户名正确
#         while account in bank:
#             print("请选择您的资金操作：")
#             print("0:查询余额\n1:存款\n2:取款\n3:退出")
#             action = input()
#             # 查询余额
#             if action == '0':
#                 print("您的账户余额为：", bank[account])
#                 continue
#             # 存款
#             elif action == '1':
#                 print("请输入您要存款的金额：")
#                 store = int(input())
#                 if store > 0:
#                     bank[account] += store
#                     print("存款成功！您的现余额为：", bank[account])
#                 continue
#             # 取款
#             elif action == '2':
#                 print("请输入您要取款的金额：")
#                 fetch = int(input())
#                 if fetch <= bank[account]:
#                     bank[account] -= fetch
#                     print("取款成功！您的现余额为：", bank[account])
#                 else:
#                     print("余额不足或输入错误，请重新操作！")
#                 continue
#             # 退出
#             elif action == '3':
#                 break
#             # 输如其他也退出
#             else:
#                 print("*** 输入有误，请重新输入 ***")
#                 continue
#             break
#         # 账户名错误
#         else:
#             print("*** 账户名错误，请重新操作！ ***")
#     # 不登录，退出
#     elif login == '1':
#         break
#     # 其他操作，不登录，退出
#     else:
#         print("*** 输入有误，请重新操作 ***")
#         continue

##
# 作业3
# 将文本生成词汇表(单词list)，单词对应ID的dict，以及ID对应单词的dict。
# 将你的程序变成一个盒子，输入就是上面一段文本，盒子内部：首先将文本转换成单词列表，再得到统计的单词表(去重)，然后得到单词ID相互对应的字典。
# 效果如下:
#
# vocab = ['大家', '中国', '捍卫', ...]
# word2id = {'大家': 0, '中国': 1, '捍卫': 2, ...}
# id2word = {0: '大家', 1: '中国', 2: '捍卫', ...}
text = '2019 年 十月 一日 上午 ， 庆祝 中华人民共和国 成立 70 周年 阅兵式 在 首都北京 盛大举行 ， 59 个 阅兵 方阵 ， 580 台受 阅 装备 ， 1.5 万人 的 参阅 队伍 接受 了 全国 人民 ' \
       '的 检阅 。 阅兵 装备 方队 展示 的 武器装备 皆 为 国产 现役 主战 装备 ， 40% 为 首次 展示 。 其中 近些年来 广受 全球 关注 的 东风 41 洲际 弹道导弹 ， 巨浪 二潜射 弹道导弹 ， 东风 ' \
       '17 高超音速 武器 系统 终于 揭幕 亮剑 ， 以 " 不怒 自威 " 的 形象 向 世界 展示 中国 捍卫 和平 的 意志 与 力量 。 相较 于 其他 首度 公开 亮相 的 武器装备 ， 这 三款 武器 多年 来 ' \
       '传闻 不断 ， 备受 关注 ， 并 因 其 " 大国 基石 " 的 地位 而 被 公众 赋予 特殊 的 期待 ， 这 三款 武器装备 实力 究竟 如何 ， 又 各自 承担 着 怎样 的 历史 " 使命 " 呢 ？ 本报 ' \
       '特约 相关 领域 军事 专家 ， 为 大家 详细 解读 这 三款 彰显 国威 ， 震撼 世界 的 国 之 重器 。 '
# vocab = text.split()
# # 统计的单词表：去重
# voc_new = list(set(vocab))
# # 按照索引再次排序，保证原始顺序
# voc_new.sort(key=vocab.index)
# print("未去重的词汇数：", len(vocab))
# print("去重后的词汇数：", len(voc_new))
# print("vocab = ", vocab)
# order = list(range(0, len(voc_new)))
# word2id = dict(zip(voc_new, order))
# id2word = dict(zip(order, voc_new))
# print("word2id = ", word2id)
# print("id2word = ", id2word)
