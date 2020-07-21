# s = "{name:'澳门', geoCoord:[113.54, 22.19]}"
#
# import re
#
# city = re.findall("\'(\w+)\'", s)
# geo = re.findall("\[(\d+.\d+),\s(\d+.\d+)\]", s)


social_network = {
    '小张': ['小刘', '小王', '小红'],
    '小王': ['六六', '娇娇', '小曲'],
    '娇娇': ['宝宝', '花花', '喵喵'],
    '六六': ['小罗', '奥巴马']
}


def search_gragh(graph, start, position):
    topology = []  # all
    nodes = [start]
    while nodes:
        person = nodes.pop(position)
        if person in topology: continue
        nodes += graph.get(person, [])
        topology.append(person)
    return topology


def dfs(graph, start):
    return search_gragh(graph, start, -1)


def bfs(gragh, start):
    return search_gragh(gragh, start, 0)


s2 = (
    ('小张', '小刘', '小王', '小红'),
    ('小王', '六六', '娇娇', '小曲'),
    ('娇娇', '宝宝', '花花', '喵喵'),
    ('六六', '小罗', '奥巴马'),
)

for person in s2:
    if '小刘' in person: print()




if __name__ == '__main__':
    # topo1 = dfs(social_network, '小王')
    # topo2 = bfs(social_network, '小王')
    # print(topo1)
    # print(topo2)
    print()