import os
import glob

def file_merge():
    os.chdir(path='./files')
    files_list = []
    for file in glob.glob('*.txt'):
        if file != 'result.txt':
            files_list.append(file)
    res = []
    for file_name in files_list:
        with open(file_name, 'r', encoding='utf-8') as f:
            line = f.readlines()
            str_count = len(line)
            res.append([file_name, str_count, ''.join(line)])
            res.sort(key=lambda x: x[1])
    with open('result.txt', 'w', encoding='utf-8') as f:
        for item in res:
            f.write(item[0] + '\n')
            f.write(str(item[1]) + '\n')
            f.write(item[2] + '\n\n')
    return res


file_merge()