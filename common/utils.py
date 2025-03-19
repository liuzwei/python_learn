import random
import string

# 生成一个随机字符串
def randomStr():    
    return ''.join(random.sample(string.ascii_letters + string.digits, 5))

def randomStudentInfo():
    return str.format('{0}, {1}, {2}', randomStr(), random.randint(10, 30), random.randint(50, 100))