# 定义鸟的基类

class birds:
    def __init__(self,name,color,skill_description):
        self.name = name
        self.color = color
        self.skill_description = skill_description

    def fly(self):
        pass
    def call(self):
        pass
    def use_skill(self):
        print(f"{self.name}使用了技能:{self.skill_description}")

class YellowBirds(birds):
    def __init__(self):
        super().__init__("黄蜂","黄色","瞬间加速，穿透障碍物")

    def fly(self):
        print("红鸟以加速向前飞行")
    def call(self):
        print("黄蜂发出:渣渣...的叫声")

class BlueBirds(birds):
    def __init__(self):
        super().__init__("蓝冰","蓝色","分裂成三只，分散攻击")

    def fly(self):
        print("蓝冰分裂向前飞行")
    def call(self):
        print("蓝冰发出:哇呜...的叫声")

class RedBirds(birds):
    def __init__(self):
        super().__init__("红火","红色","撞击前方障碍物，造成大量伤害")

    def fly(self):
        print("红鸟以稳定的速度进行飞行")
    def call(self):
        print("红火发出:wei呀...的叫声")



class Obstacle:
    def __init__(self,name,streng):
        self.name = name
        self.streng = streng
    # 多态的体现-参数多态
    def be_attack(self,birds):
        print(f"{birds.name}向{self.name}发起了攻击")
        # 多态的体现-方法调用多态
        birds.use_skill()

        if isinstance(birds,RedBirds):
            damage = 50
        elif isinstance(birds,YellowBirds):
            damage = 80
        else:
            damage = 30 * 3

        self.streng -= damage

        if self.streng < 0:
            print("障碍物被摧毁了")
        else:
            print(f"障碍物收到攻击，还剩余生命值{self.streng}")

# 创建一个障碍物对象

o1 = Obstacle("石头房子",100)

# 创建红鸟对象
Red = RedBirds()
o1.be_attack(Red)

# 创建黄鸟对象
Yellow = YellowBirds()
o1.be_attack(Yellow)