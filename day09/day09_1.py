from common.utils import randomStudentInfo
from fileutils.file_save import writeToFile
import json

def generateStudentInfo():
    with open(file='test.txt', mode='w+', encoding="utf-8") as f:
        f.write('name,age,score\n')
        f.writelines([str(randomStudentInfo()) + '\n' for i in range(100)])

        # 读取文件内容
        f.seek(0)
        l = f.readline().strip().split(',')
        # 读取下一行，并根据第一行的头构建json对象
        while True:
            data = f.readline().strip().split(',')
            if len(data) != len(l):
                break
            # 构建json对象
            json_obj = {l[i]: data[i] for i in range(len(l))}
            json_str = json.dumps(json_obj, indent=4)
            writeToFile('test.json', json_str)

    print('write success')





