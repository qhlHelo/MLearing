class People:
    def __init__(self, name, damage, hp):
        self.name = name
        self.damage = damage
        self.hp = hp


# 英雄
class Hero(People):
    def __init__(self, name, damage, hp, country):
        People.__init__(self, name, damage, hp)
        self.country = country

    # 获取信息
    def get_inf(self):
        print("姓名：{}".format(self.name))
        print("攻击力：{}".format(self.damage))
        print("当前血量：{}".format(self.hp))
        print("阵营：{}".format(self.country))

    # 攻击
    def attack(self, enemy):
        print("{}攻击力为：{}".format(self.name, self.damage))
        print("{}目前血量为：{}".format(enemy.name, enemy.hp))
        print("{}攻击{}".format(self.name, enemy.name))
        enemy.hp -= self.damage
        print("{}剩余血量为：{}".format(enemy.name, enemy.hp))

    # 回复血量
    def recover(self):
        print("【 回复血量 】")
        print("{}当前血量：{}".format(self.name, self.hp))
        self.hp += 15
        if 0 < self.hp < 70:
            print("回复后血量为：{}".format(self.hp))
        if self.hp >= 70:
            # 重置血量为满血
            self.hp == 70
            print("血量已回满")


# 武器
class Weapon:
    def __init__(self, name, damage):
        """武器基础属性"""
        self.name = name
        self.damage = damage

    def take_weapon(self, hro):
        """将武器给予英雄，英雄攻击力提升"""
        print("【 英雄武装 】")
        print("将武器-{}装备给英雄{}".format(self.name, hro.name))
        hro.damage += self.damage
        print("{}的攻击力变为{}".format(hro.name, hro.damage))


"""
主题：群英战吕布
回合设定：
  众英雄逐一与吕布持续战斗，当英雄1血量小于吕布攻击时，英雄1失败逃跑，同时加入英雄2，与吕布持续战斗；
  每当下个英雄上阵，前一个失败英雄回复的血量为15，如此持续战斗，直到吕布血量不足而逃跑
属性设定：吕布20攻200血，使用武器方天画戟，攻击力为10；众英雄各8攻70血，使用武器刀、枪、剑、戟、矛、棍、棒等，攻击力为10
"""

if __name__ == '__main__':
    """ 初始设定 """
    print("**** 初始化开始 ****")
    LB = Hero("吕布", 20, 200, "群雄")
    ZF = Hero("张飞", 10, 80, "蜀国")
    # 吕布武器
    lb = Weapon("方天画戟", 10)
    lb.take_weapon(LB)
    # 张飞武器
    zf = Weapon("丈八蛇矛", 5)
    zf.take_weapon(ZF)
    # 英雄池
    heros = {'ZF': ZF}
    # 武器库
    weapons = ['丈八蛇矛', '刀', '枪', '剑', '戟', '棍', '棒', '叉', '锤', '匕首']
    print("**** 初始化完成 ****")

    i = 0
    while 1:
        i += 1
        # 创建新英雄
        new_hero = Hero("hero" + str(i), 8, 70, "反吕联盟")
        # 给予新英雄武器
        print("--" * 6)
        new_wp = Weapon(weapons[i % len(weapons)], 10)
        new_wp.take_weapon(new_hero)
        heros["hero" + str(i)] = new_hero
        # 英雄出战
        print("【 战斗回合 】")
        print("第{}位英雄出战".format(i))
        # 持续作战：英雄血量大于吕布攻击且吕布血量大于英雄攻击
        try:
            while LB.hp > new_hero.damage:
                if new_hero.hp > LB.damage:
                    new_hero.attack(LB)
                    LB.attack(new_hero)
                if new_hero.hp < LB.damage:
                    print("英雄{}血量不足，逃跑成功，本回合结束......".format(new_hero.name))
                    break
            # 战斗结束，若之前已有出战英雄，则之前的英雄回复血量（张飞除外）
            if i >= 2:
                [heros["hero" + str(i)].recover() for i in range(1, i)]
            # 吕布血量小于英雄攻击，则吕布逃跑，剧情结束
            if LB.hp <= new_hero.damage:
                print("**** 终章 ****")
                print("吕布血量不足，落荒而逃，战斗结束！")
                break
        except ArithmeticError:
            print("程序出了一点小差，未知数据异常")
