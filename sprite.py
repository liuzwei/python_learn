import mysql.connector

class Sprite:
    def __init__(self, weight, color, height, power):
        self.weight = weight
        self.color = color
        self.height = height
        self.power = power

    # 精灵行走功能
    def move(self):
        if self.power > 0:
            self.power -= 1
            print("精灵正在行走")
        else:
            print("精灵体力不支，无法行走")
        mysql.connector.connect(host="localhost", user="root", password="123456", database="pokemon")
    # 精灵跳跃功能
    def jump(self):
        if self.power > 0:
            self.power -= 1
            print("精灵正在跳跃")
        else:
            print("精灵体力不支，无法跳跃")
    #精灵进食功能
    def eat(self, food):
        self.power += food
        print("精灵正在进食")

    def toString(self):
        print("weight:%s, color:%s, height:%s, power:%s" % (self.weight, self.color, self.height, self.power))
    
sp = Sprite(weight=100, color="red", height=1.8, power=100)
sp.move()
sp.jump()
sp.eat(10)
sp.toString()
