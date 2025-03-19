import os

def writeToFile(fileName, data):
    last_content = ''
    # 判断文件是否存在
    if not os.path.exists(fileName):
        with open(file=fileName, mode='w', encoding="utf-8") as f:
            f.write('['+data+']')
        return
    with open(file=fileName, mode='r+', encoding="utf-8") as f:
        content = f.read()
        if content == '':
            last_content = '['+data+']'
        else:
            last_content = content[:-1] +","+ data + ']'
    with open(file=fileName, mode='w', encoding="utf-8") as f:
        f.write(last_content)