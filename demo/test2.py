import re
data = [('城市', '日期', '质量等级', 'AQI指数', '当天AQI排名', 'PM2.5', 'PM10', 'So2', 'No2', 'Co', 'O3'),
('杭州', '2019-01-01', '良', '73', '205', '53', '72', '8', '39', '0.90', '20'),
('杭州', '2019-01-02', '良', '90', '202', '66', '90', '9', '48', '0.95', '21')]

x = list(map(lambda x: str(x).strip("()"), data))
print(type(x))
print(x)

#
# dataset = \
# """色泽 根蒂 敲声 纹理 脐部 触感 密度 含糖率 好瓜
# 青绿 蜷缩 浊响 清晰 凹陷 硬滑 0.697 0.460 是
# 乌黑 蜷缩 沉闷 清晰 凹陷 硬滑 0.774 0.376 是
# 乌黑 蜷缩 浊响 清晰 凹陷 硬滑 0.634 0.264 是
# 青绿 蜷缩 沉闷 清晰 凹陷 硬滑 0.608 0.318 是
# 浅白 蜷缩 浊响 清晰 凹陷 硬滑 0.556 0.215 是
# 青绿 稍蜷 浊响 清晰 稍凹 软粘 0.403 0.237 是
# 乌黑 稍蜷 浊响 稍糊 稍凹 软粘 0.481 0.149 是
# 乌黑 稍蜷 浊响 清晰 稍凹 硬滑 0.437 0.211 是
# 乌黑 稍蜷 沉闷 稍糊 稍凹 硬滑 0.666 0.091 否
# 青绿 硬挺 清脆 清晰 平坦 软粘 0.243 0.267 否
# 浅白 硬挺 清脆 模糊 平坦 硬滑 0.245 0.057 否
# 浅白 蜷缩 浊响 模糊 平坦 软粘 0.343 0.099 否
# 青绿 稍蜷 浊响 稍糊 凹陷 硬滑 0.639 0.161 否
# 浅白 稍蜷 沉闷 稍糊 凹陷 硬滑 0.657 0.198 否
# 乌黑 稍蜷 浊响 清晰 稍凹 软粘 0.360 0.370 否
# 浅白 蜷缩 浊响 模糊 平坦 硬滑 0.593 0.042 否
# 青绿 蜷缩 沉闷 稍糊 稍凹 硬滑 0.719 0.103 否"""
#
# if __name__ == '__main__':
#     x = dataset.replace(" ",",").split("\n")
#     # list(x[0])
#     # x[0][0] = '编号'
#     # print(x)