#-*- coding: utf-8 -*-
#Edited by bighead 28-12-26

def save(file_name, datas):
    with open(file_name, 'w', encoding='utf-8')as f:
        for data in datas:
            f.write(data+'\n')
    print("save successfully")
